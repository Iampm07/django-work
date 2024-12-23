from django.db.models import F
from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from . forms import QuestionForm,ChoiceForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from . models import Question,Choice
from django.utils.timezone import now

def add_question(request):
    if request.method == "POST":
        question_form =QuestionForm(request.POST)
        choice_texts = request.POST.getlist('choices') 
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.pub_date = now()
            question.save()
            #save choices 
            for choice_text in choice_texts:
                if choice_text.strip():# it avoids empty choices
                    Choice.objects.create(question=question, choice_text=choice_text)
            return redirect('polls:index') #redirect to a succes or list page
    else:
        question_form  = QuestionForm()
        return render(request,'add_question.html',{'question_form' : question_form })
def index(request):
    latest_question_list=Question.objects.order_by("-pub_date")[:5]
    context ={
        "latest_question_list":latest_question_list,
             }
    return render(request,"polls/index.html",context)
def detail(request,pk):
    
    question= get_object_or_404(Question,pk=pk)
    return render(request,"polls/details.html",{"question":
            question })    
def results(request,question_id):
    question= get_object_or_404(Question,pk=question_id) 
    return render(request,"polls/results.html",{
        "question":question})

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        return render(
            request,"polls/details.html",
            {
                "question":question,
                "error_message": "you didnt select a choice",
            },
        )
    else:
        selected_choice.votes = F("votes")+1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse("polls:results",args=(question_id,)))
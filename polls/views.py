from django.db.models import F
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from . models import Question,Choice
def index(request):
    latest_question_list=Question.objects.order_by("-pub_date")[:5]
    context ={
        "latest_question_list":latest_question_list,
             }
    return render(request,"polls/index.html",context)
def detail(request,question_id):
    
    question= get_object_or_404(Question,pk=question_id)
    return render(request,"polls/details.html",{"question":
            question })    
def results(request,question_id):
    response ="you are looking at the result of the question %s" 
    return HttpResponse (response % question_id)

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
        return HttpResponseRedirect(reverse("polls:results",args=(question_id,)))
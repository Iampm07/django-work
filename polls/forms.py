from django import forms
from .models import Question,Choice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text"]
class ChoiceForm(forms.ModelForm):
    class meta:
        model = [Choice]
        fields = ["choice_text"]
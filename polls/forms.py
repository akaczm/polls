from django import forms


class QuestionForm(forms.Form):
    question_title = forms.CharField(label='Question',
                                     required=True,
                                     max_length=250)
    answer1 = forms.CharField(label='Answer 1', max_length=250)
    answer2 = forms.CharField(label='Answer 2', max_length=250)
    answer3 = forms.CharField(label='Answer 3', max_length=250, required=False)

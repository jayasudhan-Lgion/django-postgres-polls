from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice


def index(request):
    all_questions = Question.objects.order_by("-pub_date")
    context = {"all_questions": all_questions}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST["choice"])
    selected_choice.votes += 1
    selected_choice.save()
    return redirect("detail", question_id=question.id)

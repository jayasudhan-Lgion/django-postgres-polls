from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm


def index(request):
    all_questions = Question.objects.order_by("-pub_date")
    paginator = Paginator(all_questions, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "polls/index.html", {"page_obj": page_obj})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect("results", question_id=question.id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    total_votes = sum(choice.votes for choice in choices)

    choice_data = []
    for choice in choices:
        if total_votes > 0:
            percentage = round((choice.votes / total_votes) * 100)
        else:
            percentage = 0
        choice_data.append({"choice": choice, "percentage": percentage})

    return render(
        request,
        "polls/results.html",
        {
            "question": question,
            "choice_data": choice_data,
            "total_votes": total_votes,
        },
    )


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "polls/signup.html", {"form": form})

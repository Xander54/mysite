from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
     # ListView use 'polls/question_list.html' as default template when "appname/modelname_list.html"
    context_object_name = "latest_question_list"
    #by default ListView take data from database since know the models name here"Question" than store it in varable calld:question_list
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:1]
    
class DetailView(generic.DetailView):
    model=Question
    template_name="polls/detail.html"
    # DetailView use 'polls/question_detail.html' as default template when "appname/modelname_detail.html"
    #by default DetailView take data from database since know the models name here"Question" than store it in varable calld:question_list
class ResultsView(generic.DetailView):
    model=Question
    template_name="polls/results.html"

       


















def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
     # Redisplay the question voting form.
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
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
   

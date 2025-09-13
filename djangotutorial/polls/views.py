from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
# Create your views here.
def index(request, *args, **kwargs):
        
    try:
        question = Question.objects.order_by("-pub_date")
        # print(type(question))
        retrieved_questions = ", ".join([item.question_text for item in question])
        # print(question) # to be a lit
        retrieved_quest_array = []
        for item in question: # testing:working
            print("item") # testing:working
            print(item.question_text) # testing:working
            print("item_pub_date") # testing:working
            print(item.pub_date) # testing:working
            
            retrieved_quest_array.append({"id":item.id,  "question_name": item.question_text, "pub_date":item.pub_date})

        # print("retrieved_questions")
        # print(retrieved_questions)
        # print(type(retrieved_questions))
        mycontext = {
            'retrieved_questions': retrieved_quest_array
        }
        return render(request, "polls/index.html",mycontext )
        # passing polls/file_name.html 
        # by default template folder is recognized based on the templates in settings.py
    except Question.DoesNotExist: 
        raise Http404("Question Does Not Exists")
    
# question view: used to view question
def detail(request, question_id):
    # question_id is passed on the url
    # retrieve question details
    single_question = get_object_or_404(Question, pk=question_id)
    print('single_question')
    print(single_question)
    print(type(single_question))
    print("Hello Details is running")
    print(single_question.question_text)
    choice_result = single_question.choice_set.all()
    print("choice_result")
    print(choice_result)
    return render(request, "polls/details.html", {"question": single_question})


# looking at the results of the question
def results(request, question_id):
    print("Hello Results is running")

    return HttpResponse("You're looking at the result of question %s" % question_id)


# view for voting
def vote(request, question_id):
    print("Hello Vote is running")
    return HttpResponse("You're voting on question %s" % question_id)
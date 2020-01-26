"doc"
from django.http import HttpResponse

def index(request):
    "doc"
    return HttpResponse("esta es la pagina principar de la api del usuario")

def detail(request, question_id):
    "doc"
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    "doc"
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    "doc"
    return HttpResponse("You're voting on question %s." % question_id)
from django.http import HttpRequest, HttpResponse

def index(request: HttpResponse) -> HttpResponse:
    return HttpResponse("comments")

from django.http import HttpRequest, JsonResponse

from tehran.core.post.postservice import PostService


def index(request: HttpRequest) -> JsonResponse:
    posts = PostService.get_all()
    data = []
    for post in posts:
        data.append({
            'title': post.title,
            'desc': post.description,
        })
    return JsonResponse(data, safe=False)


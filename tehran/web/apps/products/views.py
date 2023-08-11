from django.http import HttpResponse, HttpRequest

from tehran.core.product.productservice import ProductService


def index(req: HttpRequest) -> HttpResponse:
    products = ProductService.get_all()
    return HttpResponse([product.name for product in products])

from tehran.core.servicebase import ServiceBase
from tehran.core.product.iproductservice import IProductService
from tehran.dal.product.productrepository import ProductRepository


class ProductService(ServiceBase, IProductService):
    _product_repository = ProductRepository

    @classmethod
    def get_all(cls):
        return cls._product_repository.get_all()

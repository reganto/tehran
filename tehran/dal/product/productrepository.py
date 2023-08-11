from tehran.dal.repositorybase import RepositoryBase
from tehran.dal.product.iproductrepository import IProductRepository
from tehran.web.apps.products.models import Product

class ProductRepository(RepositoryBase, IProductRepository):
    _product = Product
   
    @classmethod
    def get_all(cls):
        return cls._product.objects.all()

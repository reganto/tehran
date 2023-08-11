import abc

from tehran.dal.irepository import IRepository


class IProductRepository(IRepository, abc.ABCMeta):
    pass
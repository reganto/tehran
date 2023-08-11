from tehran.core.post.ipostservice import IPostService
from tehran.core.servicebase import ServiceBase
from tehran.dal.post.postrepository import PostRepository


class PostService(ServiceBase, IPostService):
    _post_repository = PostRepository

    @classmethod
    def get_all(cls):
        return cls._post_repository.get_all()    

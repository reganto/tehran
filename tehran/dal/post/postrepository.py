from tehran.dal.post.ipostrepository import IPostRepository
from tehran.dal.repositorybase import RepositoryBase
from tehran.web.apps.blog.models import Post


class PostRepository(RepositoryBase, IPostRepository):
    _post = Post

    @classmethod
    def get_all(cls):
        return cls._post.objects.all()
        
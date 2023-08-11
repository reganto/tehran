import abc


class IRepository(abc.ABCMeta):
    @classmethod
    def get_all(cls): ...

    @classmethod
    def remove(cls): ...

    @classmethod
    def create(cls): ...

    @classmethod
    def update(cls): ...

import abc


class IService(abc.ABCMeta):
    @classmethod
    def get_all(cls): ...

    @classmethod
    def create(cls): ...

    @classmethod
    def update(cls): ...

    @classmethod
    def remove(cls): ...

from abc import ABC, abstractmethod


class RepositoryFactory(ABC):
    @abstractmethod
    def create(self, repository_type):
        pass

    @abstractmethod
    def read(self, repository_type):
        pass

    @abstractmethod
    def update(self, repository_type):
        pass

    @abstractmethod
    def delete(self, repository_type):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def delete_all(self):
        pass
from repository_factory import RepositoryFactory

class UserRepository(RepositoryFactory):
    def __init__(self, database_helper):
        self.database_helper = database_helper

    def create(self, user):
        session = self.database_helper.Session()

        
        session.close()

    def read(self, user):
        pass

    def update(self, user):
        pass

    def delete(self, user):
        pass

    def read_all(self):
        pass

    def delete_all(self):
        pass
from use_case.repository.repository_interface import RepositoryInterface

class ReadProduct:
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, product_id):
        return self.repository.get_by_id(product_id)

from use_case.repository.repository_interface import RepositoryInterface

class DeleteProduct:
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def execute(self, product_id):
        return self.repository.delete(product_id)

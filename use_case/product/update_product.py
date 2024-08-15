from use_case.repository.repository_interface import RepositoryInterface

class UpdateProduct:
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def execute(self, product_id, data):
        return True if self.repository.update(product_id, data) else False

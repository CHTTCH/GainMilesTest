from abc import ABC, abstractmethod
from entity.product.product import Product

class RepositoryInterface(ABC):
    @abstractmethod
    def add(self, product: Product) -> Product:
        pass

    @abstractmethod
    def get_all(self) -> list:
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def update(self, product: Product) -> Product:
        pass

    @abstractmethod
    def delete(self, product_id: int) -> bool:
        pass
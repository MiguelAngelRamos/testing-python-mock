from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount: float, card_token: str) -> bool:
        pass

class InventorySystem(ABC):
    @abstractmethod
    def check_stock(self, product_id: int, quantity: int) -> bool:
        pass
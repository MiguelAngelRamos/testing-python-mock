import pytest 
from unittest.mock import MagicMock
from src.interfaces import PaymentGateway, InventorySystem
from src.processor import OrderProcessor

@pytest.fixture
def mock_payment_gateway():
    return MagicMock(spec=PaymentGateway)

@pytest.fixture
def mock_inventory_system():
    return MagicMock(spec=InventorySystem)

@pytest.fixture
def processor(mock_payment_gateway, mock_inventory_system):
    return OrderProcessor(payment_gateway=mock_payment_gateway, inventory_system=mock_inventory_system)

@pytest.fixture
def sample_order():
    return {
        "order_id": 101,
        "product_id": 50,
        "quantity": 2,
        "amount": 100.0,
        "card_token": "tok_visa_123"
    }
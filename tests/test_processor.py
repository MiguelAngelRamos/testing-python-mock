import pytest
from unittest.mock import call

@pytest.mark.unit
def test_process_order_sucess(processor, mock_inventory_system, mock_payment_gateway, sample_order):
    # GIVEN: Configuración del escenario (Arrange)
    # Configuramos los mocks en el mejor de los casos es decir que digan que "Si" a todo
    mock_inventory_system.check_stock.return_value = True
    mock_payment_gateway.charge.return_value = True

    # WHEN: Ejecución Act
    result = processor.process_order(sample_order)

    # Then: Verificación (Assert)

    assert result["status"] == "success"

    # Verificacion comportamiento: ¿Se llamó al inventario con los datos correctos?
    mock_inventory_system.check_stock.assert_called_once_with(50, 2)

    # ¿Se intentó cobrar el monto correcto?
    mock_payment_gateway.charge.assert_called_once_with(100.0, "tok_visa_123")


# @pytest.mark.unit
# def test_process_order_no_stock():
#     pass

# @pytest.mark.unit
# def test_payment_failure_scenarios():
#     pass
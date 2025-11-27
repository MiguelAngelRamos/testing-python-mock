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


@pytest.mark.unit
def test_process_order_no_stock(processor, mock_payment_gateway, mock_inventory_system, sample_order):
    ## GIVEN: El inventario no es suficiente fuerzo a que retorne False
    mock_inventory_system.check_stock.return_value = False

    # When / Then 
    # pytest.raises: Context manager que verifica que se lance una excepción
    # ValueError : tipo de excepcion esperada
    with pytest.raises(ValueError) as excinfo:
        processor.process_order(sample_order)

    assert "Stock insuficiente" in str(excinfo.value)

    ## Aseguramos que NO se intentó cobrar si no habia stock
    mock_payment_gateway.charge.assert_not_called()

@pytest.mark.unit
@pytest.mark.parametrize("amount, card_token", [
    (0, "tok_invalid"),
    (1000000, "tok_limit"),
    (-50, "tok_error")
    ])
def test_payment_failure_scenarios(processor, mock_payment_gateway,mock_inventory_system, sample_order, amount, card_token):
    # GIVEN Configuracion del escenario (Arrange)
    order_data = sample_order.copy()

    # Modificamos
    order_data["amount"] = amount
    order_data["card_token"] = card_token

    # Configuramos los mocks para simular el comportamiento esperado 
    mock_inventory_system.check_stock.return_value = True # Simula que si hay stock disponible
    mock_payment_gateway.charge.return_value = False # Simula que el pago Falla
    

    # When / Then : Ejecución y Verificación combinadas
    with pytest.raises(ValueError) as excinfo:
        processor.process_order(order_data)

    assert "El pago fue rechazado" in str(excinfo.value)

    



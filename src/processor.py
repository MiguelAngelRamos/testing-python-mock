from src.interfaces import PaymentGateway, InventorySystem

class OrderProcessor:
    def __init__(self, payment_gateway: PaymentGateway, inventory_system: InventorySystem):
        self.payment_gateway = payment_gateway
        self.inventory_system = inventory_system
    
    def process_order(self, order: dict) -> dict:
        product_id = order.get("product_id")
        quantity = order.get("quantity", 1)
        amount = order.get("amount")
        card_token = order.get("card_token")

        # 1. Validar el stock
        if not self.inventory.check_stock(product_id, quantity):
            raise ValueError(f"Stock insuficiente para el producto {product_id}")
        
        # 2. Procesar el pago
        payment_successful = self.payment_gw.charge(amount, card_token)

        if not payment_successful:
            raise ValueError("El pago fue rechazado por la pasarela.")     
        
        # Retornar éxito

        return {
            "status" : "success",
            "order_id": order.get("order_id"),
            "message": "Pedido procesado correctamente"
        }
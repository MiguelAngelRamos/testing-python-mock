from src.interfaces import PaymentGateway, InventorySystem
import time

class RealPaymentGateway(PaymentGateway):
    def charge(self, amount: float, card_token: str) -> bool:
        # Simulación de una llamada a API externa (lenta)
        time.sleep(1) 
        print(f"Cobrando ${amount} a la tarjeta {card_token}...")
        return True
    

class RealInventorySystem(InventorySystem):
    def check_stock(self, product_id: int, quantity: int) -> bool:
        # Simulación de consulta a Base de Datos
        print(f"Verificando stock para producto {product_id}...")
        return True
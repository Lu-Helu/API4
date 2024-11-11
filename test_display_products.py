import unittest
import requests
from typing import List, Dict

# URL con la estructura de datos
URL = "https://jsonkeeper.com/b/MX0A"

# Función que obtiene la lista de productos desde la URL
def fetch_products() -> List[Dict]:
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data.get("products", [])
    else:
        return []

# Función que simula la visualización de productos
def display_products(products: List[Dict]) -> str:
    if not products:
        return "No hay productos para mostrar."
    display = "\n".join([f"{p['name']} - {p['price']} {p['currency']}" for p in products])
    return display

# Clase de prueba unitaria
class TestDisplayProducts(unittest.TestCase):
    
    def test_display_products_with_data(self):
        products = fetch_products()
        result = display_products(products)
        self.assertIn("iPhone 13 - 999.99 USD", result)
        self.assertIn("Samsung Galaxy S21 - 899.99 USD", result)
        self.assertNotIn("No hay productos para mostrar.", result)

    def test_display_products_empty(self):
        result = display_products([])
        self.assertEqual(result, "No hay productos para mostrar.")

if __name__ == "__main__":
    unittest.main()

class Customer:
  def __init__(self, name: str):
    self.name = name
    self.orders = []

class Order:
  def __init__(self, order_in: int, customer):
    self.order_in = order_in
    self.customer = customer
    customer.orders.append(list)

person = Customer("Moira")

order_1 = Order(101, moira)

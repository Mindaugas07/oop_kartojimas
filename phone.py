from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0) -> None:
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)
        # Run validations to the received arguments
        # assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        # assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        assert (
            broken_phones >= 0
        ), f"Quantity {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        # self.name = name
        # self.price = price
        # self.quantity = quantity
        self.broken_phones = broken_phones
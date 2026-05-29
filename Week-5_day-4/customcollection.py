class ShoppingCart:
    def __init__(self):
        self._items = []  

    #Add item 
    def add_item(self, item):
        self._items.append(item)

    #Remove item
    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
        else:
            raise ValueError(f"{item} not found in cart")

    #Indexing support
    def __getitem__(self, index):
        return self._items[index]

    #Length support
    def __len__(self):
        return len(self._items)

    # Iteration support
    def __iter__(self):
        return iter(self._items)

    #Nice display
    def __repr__(self):
        return f"ShoppingCart({self._items})"

cart = ShoppingCart()

cart.add_item("Apple")
cart.add_item("Banana")
cart.add_item("Milk")

print(cart)  

print(cart[0])  

cart.remove_item("Banana")

for item in cart:
    print(item)

print(len(cart))
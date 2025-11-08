'''
Shopping Cart Class

create class ShoppingCart
that allows adding and removing items (use a list)
methods:
addItem(item)
removeItem(item)
view cart() # iterate list
calculate total amount (based on items)
'''
class ShoppingCart:
    def __init__(self,name):
        self.name=name
        self.cart=[
            # Item    rs/kg  
            ['Apples',100],
            ['Bananas',80],
            ['Berries',500],
            ['Oranges',20],
            ['Grapes',60]
        ]
        print(f'{self.name}, Welcome to our shop')

    def addItem(self,item):
        self.cart.append(item)
        print("Item added successfully")

    def removeItem(self,idx):
        self.cart.pop(idx)
        print(f'item is removed successfully.')

    def viewCart(self):
        for i in self.cart:
            print(f'{i[0]} price is {i[1]}')

    def totalAmount(self):
        sum=0
        for i in self.cart:
            # print(i[1],end=" ")
            sum+=i[1]

        print(f'Your total amount is : {sum}')
        print(f'Thank you for choosing us.')

        
person=ShoppingCart("Parwez Alam")
person.addItem(['Onions',40])
person.removeItem(2)
person.viewCart()
person.totalAmount()

# Lori Vo 1852113

class ItemToPurchase:
    def __init__(self, name='none', price=0, quantity=0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price,
                                         self.item_quantity*self.item_price))


if __name__ == '__main__':
    item1 = ItemToPurchase()
    print('Item 1')
    print('Enter the item name:')
    item1.item_name = input()
    print('Enter the item price:')
    item1.item_price = int(input())
    print('Enter the item quantity:')
    item1.item_quantity = int(input())

    print()

    item2 = ItemToPurchase()
    print('Item 2')
    print('Enter the item name:')
    item2.item_name = input()
    print('Enter the item price:')
    item2.item_price = int(input())
    print('Enter the item quantity:')
    item2.item_quantity = int(input())
    print()

    print('TOTAL COST')
    total = (item1.item_quantity*item1.item_price)+(item2.item_quantity*item2.item_price)

    item1.print_item_cost()
    item2.print_item_cost()
    print()
    print('Total: ${}'.format(total))

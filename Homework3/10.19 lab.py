# Lori Vo 1852113

class ItemToPurchase:
    def __init__(self, given_name='none', price=0, quantity=0, description="none"):
        self.item_name = given_name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price,
                                         self.item_quantity*self.item_price))

    def print_item_description(self):
        print('{}: {}'.format(self.item_name, self.item_description))


class ShoppingCart:
    def __init__(self, cus_name="none", cur_date="January 1, 2016", cart=[]):
        self.customer_name = cus_name
        self.current_date = cur_date
        self.cart_items = cart

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self):
        print('REMOVE ITEM FROM CART')
        remove_name = str(input('Enter name of item to remove:'))
        number = 0
        for n in self.cart_items:
            if n.item_name == remove_name:
                self.cart_items.remove(n)
                print()
                number = 1
                break
        if number == 0:
            print()
            print('Item not found in cart. Nothing removed.')
        print()

    def modify_item(self, item_modifying, item_quantity):
        item_modifying.item_quantity = item_quantity

    def get_num_items_in_cart(self):
        num_in_cart = 0
        for amount in self.cart_items:
            num_in_cart += amount.item_quantity
        return num_in_cart

    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += (item.item_quantity * item.item_price)
        return total

    def print_total(self):
        total = self.get_cost_of_cart()
        print('OUTPUT SHOPPING CART')
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print('Number of Items:', str(self.get_num_items_in_cart()))
        print()
        if total != 0:

            for n in self.cart_items:
                n.print_item_cost()

            print()
            print('Total: ${}'.format(self.get_cost_of_cart()))
            print()
        else:
            print('SHOPPING CART IS EMPTY')
            print()
            print('Total: ${}'.format(self.get_cost_of_cart()))
            print()

    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print()
        print('Item Descriptions')
        for n in self.cart_items:
            n.print_item_description()
        print()


def print_menu(cart):
    user_option = ''

    while user_option != 'q':
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print("i - Output items' descriptions")
        print('o - Output shopping cart')
        print('q - Quit')
        print()
        print('Choose an option:')
        user_option = input()
        while user_option != 'a' and user_option != 'r' and user_option != 'c' and user_option != 'i'\
                and user_option != 'o' and user_option != 'q':
            print('Choose an option:')
            user_option = input()
        if user_option == 'a':
            print('ADD ITEM TO CART')
            print('Enter the item name:')
            item_name = (input())
            print('Enter the item description:')
            item_description = (input())
            print('Enter the item price:')
            item_price = int(input())
            print('Enter the item quantity:')
            item_quantity = int(input())
            print()
            item_purchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item_purchase)
        if user_option == 'r':
            cart.remove_item()
        if user_option == 'c':
            print('CHANGE ITEM QUANTITY')
            k = 0
            print('Enter the item name:')
            i_name = input()

            print('Enter the new quantity:')
            i_quantity = int(input())

            for i in cart.cart_items:
                if i_name == i.item_name:
                    k = 1
                    print('Enter the new quantity:')
                    cart.modify_item(i, i_quantity)

                    print()
                    break
            if k == 0:
                print('Item not found in cart. Nothing modified.')
                print()

        if user_option == 'i':
            cart.print_descriptions()
        if user_option == 'o':
            cart.print_total()
        if user_option == 'q':
            break


if __name__ == "__main__":
    name = input("Enter customer's name:")
    print()
    date = input("Enter today's date:")
    print()
    print()
    print("Customer name:", name)
    print("Today's date:", date)
    new_cart = ShoppingCart(name, date)
    print()
    print_menu(new_cart)

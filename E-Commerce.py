from abc import ABC, abstractmethod

# ------------------ USER CLASSES ------------------

class user(ABC):
    @abstractmethod
    def check_credentials(self, uname, passw):
        pass


class admin(user):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_credentials(self, uname, passw):
        return self.username == uname and self.password == passw


class customer(user):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_credentials(self, uname, passw):
        return self.username == uname and self.password == passw


# ------------------ CATEGORY CLASS ------------------

class category:
    def __init__(self, cat1, cat2, cat3, id1, id2, id3):
        self.cat = cat1 + "," + cat2 + "," + cat3
        self.category_id = id1 + "," + id2 + "," + id3

    def display(self):
        cats = self.cat.split(",")
        ids = self.category_id.split(",")
        for c, i in zip(cats, ids):
            print(f"{i} → {c}")

    def add_category(self, new_cat, new_cat_id):
        self.cat = self.cat + "," + new_cat
        self.category_id = self.category_id + "," + new_cat_id

    def delete_category(self, cat_name, cat_id, items_obj=None):
        self.cat = self.cat.replace(cat_name, "").replace(",,", ",").strip(",")
        self.category_id = self.category_id.replace(cat_id, "").replace(",,", ",").strip(",")
        # New: Also delete all items under that category
        if items_obj:
            items_obj.delete_items_by_category(cat_id)

    def modify_category(self, cat_name, cat_id, new_cat_name, new_cat_id):
        self.cat = self.cat.replace(cat_name, new_cat_name)
        self.category_id = self.category_id.replace(cat_id, new_cat_id)


# ------------------ ITEMS CLASS ------------------

class items:
    def __init__(self,
                 item1_id, item1_name, item1_cat, item1_price,
                 item2_id, item2_name, item2_cat, item2_price,
                 item3_id, item3_name, item3_cat, item3_price,
                 item4_id, item4_name, item4_cat, item4_price,
                 item5_id, item5_name, item5_cat, item5_price,
                 item6_id, item6_name, item6_cat, item6_price,
                 item7_id, item7_name, item7_cat, item7_price,
                 item8_id, item8_name, item8_cat, item8_price,
                 item9_id, item9_name, item9_cat, item9_price):

        self.items = (
            item1_id + "-" + item1_name + "-" + item1_cat + "-" + item1_price + "," +
            item2_id + "-" + item2_name + "-" + item2_cat + "-" + item2_price + "," +
            item3_id + "-" + item3_name + "-" + item3_cat + "-" + item3_price + "," +
            item4_id + "-" + item4_name + "-" + item4_cat + "-" + item4_price + "," +
            item5_id + "-" + item5_name + "-" + item5_cat + "-" + item5_price + "," +
            item6_id + "-" + item6_name + "-" + item6_cat + "-" + item6_price + "," +
            item7_id + "-" + item7_name + "-" + item7_cat + "-" + item7_price + "," +
            item8_id + "-" + item8_name + "-" + item8_cat + "-" + item8_price + "," +
            item9_id + "-" + item9_name + "-" + item9_cat + "-" + item9_price
        )

    def display(self):
        its = self.items.split(",")
        for i in its:
            print(f"{i}")

    def add_item(self, item_id, item_name, item_cat, item_price):
        self.items = self.items + "," + item_id + "-" + item_name + "-" + item_cat + "-" + item_price

    def delete_item(self, item_id, item_name, item_cat, item_price):
        target = item_id + "-" + item_name + "-" + item_cat + "-" + item_price
        self.items = self.items.replace(target, "")
        self.items = self.items.replace(",,", ",").strip(",")

    def modify_item(self, old_id, old_name, old_cat, old_price, new_id, new_name, new_cat, new_price):
        old_item = old_id + "-" + old_name + "-" + old_cat + "-" + old_price
        new_item = new_id + "-" + new_name + "-" + new_cat + "-" + new_price
        self.items = self.items.replace(old_item, new_item)

    def search_items(self, name):
        its = self.items.split(",")
        found = [i for i in its if name.lower() in i.lower()]
        if found:
            print("Search Results:")
            for f in found:
                print(f)
        else:
            print("No items found with that name.")

    # --- New: delete all items belonging to a deleted category ---
    def delete_items_by_category(self, cat_id):
        its = self.items.split(",")
        remaining = [i for i in its if f"-{cat_id}-" not in i]
        self.items = ",".join(remaining)
        print(f"All items under category {cat_id} have been removed.")


# ------------------ CART CLASS ------------------

class cart:
    def __init__(self, items=""):
        self.items = items

    def add_item(self, item_id, item_name, category_id, item_price):
        new_item = item_id + "-" + item_name + "-" + category_id + "-" + item_price
        if self.items == "":
            self.items = new_item
        else:
            self.items = self.items + "," + new_item

    def delete_item(self, item_id, item_name, category_id, item_price):
        target = item_id + "-" + item_name + "-" + category_id + "-" + item_price
        self.items = self.items.replace(target, "")
        self.items = self.items.replace(",,", ",").strip(",")

    def view_cart(self):
        if self.items == "":
            print("Your cart is empty.")
        else:
            print("\nItems in your cart:")
            for i in self.items.split(","):
                print(f" - {i}")

    def total_amount(self):
        if not self.items:
            return 0
        total = 0
        for i in self.items.split(","):
            parts = i.split("-")
            if len(parts) == 4:
                total += int(parts[3])
        return total


# ------------------ PAYMENT CLASS ------------------

class payment:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print("\nSelect Payment Method:")
        print("1. UPI")
        print("2. Debit Card")
        print("3. Net Banking")
        print("4. PayPal")

        choice = int(input("Choice: "))
        if choice == 1:
            print(f"You will be redirected to UPI portal to pay Rs. {self.amount}")
        elif choice == 2:
            print(f"You will be redirected to Debit Card portal to pay Rs. {self.amount}")
        elif choice == 3:
            print(f"You will be redirected to Net Banking portal to pay Rs. {self.amount}")
        elif choice == 4:
            print(f"You will be redirected to PayPal to pay Rs. {self.amount}")
        else:
            print("Invalid payment option.")
            return
        print("✅ Payment successful! Your order has been placed.")


# ------------------ MAIN PROGRAM ------------------

if __name__ == "__main__":
    print("Welcome to the Demo Marketplace")

    admin_user = admin("admin", "admin123")
    customer_user = customer("customer", "cust123")
    categories = category("Clothing", "Footwear", "Electronics", "C1", "C2", "C3")
    it = items(
        "I1", "Shirt", "C1", "2000",
        "I2", "Jacket", "C1", "2500",
        "I3", "Jeans", "C1", "1000",
        "I4", "Sneakers", "C2", "1500",
        "I5", "Slippers", "C2", "3000",
        "I6", "Boots", "C2", "2000",
        "I7", "Phone", "C3", "50000",
        "I8", "Laptop", "C3", "120000",
        "I9", "Headphones", "C3", "5000"
    )

    print("Please login to continue:\n1. Yes\n2. No (View as Guest)")
    choice = int(input("Choice: "))

    # ------------------ LOGIN ------------------

    if choice == 1:
        print("Select Usertype:\n1. Admin\n2. Customer")
        utype = int(input("Usertype: "))

        # ------------------ ADMIN LOGIN ------------------
        if utype == 1:
            while True:
                uname = input("Enter username: ")
                passw = input("Enter password: ")
                if admin_user.check_credentials(uname, passw):
                    print("Login Successful as Admin")

                    while True:
                        print("\n--- Admin Menu ---")
                        print("1. View Categories")
                        print("2. View Items")
                        print("3. Add Category")
                        print("4. Delete Category")
                        print("5. Modify Category")
                        print("6. Add Item")
                        print("7. Delete Item")
                        print("8. Modify Item")
                        print("9. Logout")

                        admin_choice = int(input("Enter your choice: "))

                        if admin_choice == 1:
                            categories.display()
                        elif admin_choice == 2:
                            it.display()
                        elif admin_choice == 3:
                            categories.display()
                            a = input("Enter new category: ")
                            b = input("Enter new category ID: ")
                            categories.add_category(a, b)
                        elif admin_choice == 4:
                            categories.display()
                            a = input("Enter category to delete: ")
                            b = input("Enter ID: ")
                            categories.delete_category(a, b, it)
                        elif admin_choice == 5:
                            categories.display()
                            a = input("Enter category to modify: ")
                            b = input("Enter ID: ")
                            c = input("Enter modified category name: ")
                            d = input("Enter new ID: ")
                            categories.modify_category(a, b, c, d)
                        elif admin_choice == 6:
                            a = input("Enter item ID: ")
                            b = input("Enter item name: ")
                            c = input("Enter category ID: ")
                            d = input("Enter price: ")
                            it.add_item(a, b, c, d)
                        elif admin_choice == 7:
                            a = input("Enter item ID: ")
                            b = input("Enter item name: ")
                            c = input("Enter category ID: ")
                            d = input("Enter price: ")
                            it.delete_item(a, b, c, d)
                        elif admin_choice == 8:
                            a = input("Old item ID: ")
                            b = input("Old item name: ")
                            c = input("Old category ID: ")
                            d = input("Old price: ")
                            e = input("New item ID: ")
                            f = input("New item name: ")
                            g = input("New category ID: ")
                            h = input("New price: ")
                            it.modify_item(a, b, c, d, e, f, g, h)
                        elif admin_choice == 9:
                            print("Logging out as Admin...")
                            break
                        else:
                            print("Invalid choice.")
                    break
                else:
                    print("Invalid admin credentials. Try again.")

        # ------------------ CUSTOMER LOGIN ------------------
        elif utype == 2:
            while True:
                uname = input("Enter username: ")
                passw = input("Enter password: ")

                if customer_user.check_credentials(uname, passw):
                    print("Login Successful as Customer")
                    user_cart = cart()

                    while True:
                        print("\n--- Customer Menu ---")
                        print("1. View Categories")
                        print("2. View Items")
                        print("3. Search Item")
                        print("4. Add to Cart")
                        print("5. Remove from Cart")
                        print("6. View Cart")
                        print("7. Proceed to Payment")
                        print("8. Logout")

                        cust_choice = int(input("Enter your choice: "))

                        if cust_choice == 1:
                            categories.display()
                        elif cust_choice == 2:
                            it.display()
                        elif cust_choice == 3:
                            name = input("Enter item name to search: ")
                            it.search_items(name)
                        elif cust_choice == 4:
                            a = input("Enter item ID: ")
                            b = input("Enter item name: ")
                            c = input("Enter category ID: ")
                            d = input("Enter price: ")
                            user_cart.add_item(a, b, c, d)
                            print("Item added to cart.")
                        elif cust_choice == 5:
                            a = input("Enter item ID: ")
                            b = input("Enter item name: ")
                            c = input("Enter category ID: ")
                            d = input("Enter price: ")
                            user_cart.delete_item(a, b, c, d)
                            print("Item removed from cart.")
                        elif cust_choice == 6:
                            user_cart.view_cart()
                        elif cust_choice == 7:
                            total = user_cart.total_amount()
                            print(f"Your total is Rs. {total}")
                            if total > 0:
                                pay = payment(total)
                                pay.process_payment()
                                user_cart = cart()  # Empty cart after payment
                            else:
                                print("Your cart is empty.")
                        elif cust_choice == 8:
                            print("Logging out as Customer...")
                            break
                        else:
                            print("Invalid choice.")
                    break
                else:
                    print("Invalid customer credentials. Try again.")

    # ------------------ GUEST MODE ------------------
    elif choice == 2:
        print("\nYou are viewing as a Guest.")
        while True:
            print("\n--- Guest Menu ---")
            print("1. View Categories")
            print("2. View Items")
            print("3. Search Item")
            print("4. Try to Shop (Login Required)")
            print("5. Exit")

            guest_choice = int(input("Enter your choice: "))

            if guest_choice == 1:
                categories.display()
            elif guest_choice == 2:
                it.display()
            elif guest_choice == 3:
                name = input("Enter item name to search: ")
                it.search_items(name)
            elif guest_choice == 4:
                print("\n🛒 You must login to shop or checkout. Please restart and log in as Customer.")
            elif guest_choice == 5:
                print("Exiting Guest mode. Goodbye!")
                break
            else:
                print("Invalid choice.")

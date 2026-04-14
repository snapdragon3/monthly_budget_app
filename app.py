# fname=input("What is your first Name: ")
# lname=input("What is your last Name: ")

# print(f"Hello {fname} {lname}, how was your day?")

shopping_list = []

def show_menu():
    print("\n--- Shopping List App ---")
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added!")
    elif choice == "2":
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    elif choice == "3":
        item_num = int(input("Enter item number to remove: "))
        if 0 < item_num <= len(shopping_list):
            removed = shopping_list.pop(item_num - 1)
            print(f"{removed} removed!")
        else:
            print("Invalid number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")


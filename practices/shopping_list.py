# KK 2nd Shopping List Manager Practice

start = '\033[1m'
end = '\033[0m'

shopping_list = []
print(f"Greetings. Type 'exit' to stop.\n{start}'Add' - Add an item to your shopping list\n'Remove' - Remove an item from your shopping list\n'View' - See what items you have in your shopping list\n'Mark' - Mark an item as bought in your shopping list{end}")
while True:
    choice = input(f"\nRespond below to remove something, add, mark, or view your list:\n").lower().strip()
    
    if choice == "add":
        added_item = input("\nWhat would you like to add to your shopping list?:\n").capitalize().strip()
        shopping_list.append(added_item)
        print(f"Added: {added_item}")
        
    elif choice == "view": 
        if shopping_list == []:
            print("There is currently nothing in your shopping list.")
        else:
            print("\nYour Shopping List: ")
            for item in shopping_list:
                print(f"{item}")
    ### doesn't fully work
    elif choice == "mark":
        checker = input("\nWhat would you like to check off of your list?:\n").capitalize().strip()
        if checker in shopping_list:
            for a in shopping_list:
                print(f"{a}: Bought")
        else:
            print("This isn't in your shopping list!")
    elif choice == "remove":
        removed_item = input(f"\nWhat would you like to remove from your list?:\n").capitalize().strip()
        if removed_item in shopping_list:
            shopping_list.remove(removed_item)
            print(f"Removed: {removed_item}")
        else:
            print("Item isn't in your shopping list")
    elif choice == "exit":
        break
    else:
        print("\nNot an option! Try again.") 

    

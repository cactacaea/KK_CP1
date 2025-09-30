# KK 2nd Shopping List Manager Practice

start = '\033[1m'
end = '\033[0m'

shopping_list = []
print("Greetings. Type 'exit' to stop.")
while True:
    choice = input(f"{start}'Add' - Add an item to your shopping list\n'Remove' - Remove an item from your shopping list\n'View' - See what items you have in your shopping list\n'Check' - Mark an item as bought in your shopping list\n{end}Respond below to remove something, add, or see your list:\n")
    
    if choice == "add":
        added_item = input("\nWhat would you like to add to your shopping list?:\n").capitalize().strip()
        shopping_list.append(added_item)
        #print(f"{shopping_list}\n")
        
        for item in shopping_list:
            print(f"\nNoted Shopping List:\n{item}")

    
    if added_item == "exit":
        break



# Have a help command
# Have a show command
# Clean code up in general




# MAKE sure to run this as python3 - input function can cause issues - Read the comments

# make a list to hold onto our items
shopping_list = []


def show_help():
    # print out instruction on how to use the app
    print('What should we get at the store?')
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for list help.
Enter 'SHOW' to show current list.
""")

def show_list():
    # print out the list
    print("Here's your list:")
    for item in shopping_list:
     print(item)



show_help()

while True:
    # ask for new items
    # if using python 2 change this to raw_input()
    new_item = input("Item: ")

    # be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue

    # add new items to our list
    shopping_list.append(new_item)




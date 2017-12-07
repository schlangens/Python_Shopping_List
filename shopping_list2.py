

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

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

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
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)


show_list()


# make a list to hold onto our items
shopping_list = []

# print out instruction on how to use the app
print('What should we get at the store?')
print("Enter 'DONE' to stop adding items.")

while True:
    # ask for new items
    # if using python 2 change this to raw_input()
    new_item = input("Item: ")

    # be able to quit the app
    if new_item == 'DONE':
        break

    # add new items to our list
    shopping_list.append(new_item)


# print out the list
print("Here's your list:")

for item in shopping_list:
    print(item)

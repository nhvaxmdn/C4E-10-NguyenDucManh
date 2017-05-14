cuahang = ["T-Shirt", "Sweater", "Jeans"]

print("===========================================")
print(" Add = A, Update = U, Delete = D")
print("===========================================")

while True:

    print("")
    action = input("Welcome to our shop, what do you want ( A, U, D) ?")
    print(action)
    action = action.upper()

    print("Items is shop:")
    item_no = 1
    for items in cuahang:
        print("{0}.{1}".format(item_no,items))
        item_no +=1


    if action =="A":
        item = input("Add new item: ")
        cuahang.append(item)
    elif action =="U":
        item_no = int(input("Update new item:"))-1
        new_item = input("New item:")
        cuahang.insert(ite_no, item_new)

    elif action =="D":
        delete_item = input("Delete item")
        cuahang.remove(delete_item)

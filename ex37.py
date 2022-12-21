def print_dict(dicty):
    item_list = list(dicty.items())
    for i in item_list:
        print(i, type(i))



my_dict = {'matej': 20, 'siniša': 35, 'danijela': 22}

try:
    print_dict(my_dict)
except NameError:
    print("variable not implemented")
except NotImplementedError:
    print("function not implemented")
else:
    print("nothing else is wrong")
finally:
    print("try except is finished.")

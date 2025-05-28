grocery = {} # create empty dictionary

# create a function that handles duplicate entry
def check_basket(new_item):
    if new_item.upper() in grocery.keys():
        grocery[new_item.upper()] += 1
    else:
        grocery[new_item.upper()] = 1


while True:
    try:
        x = input("add to basket : ")
        check_basket(x)
    except EOFError:
        for item in grocery:
            print(f'{grocery[item]} - {item}')
        break

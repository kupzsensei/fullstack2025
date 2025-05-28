try:
    x = int(input("give a number: ")) # cat
    print(x/0)
except ValueError: # catch defined Error
    print("Please input a number next time")

except ZeroDivisionError as err: # catch defined Error
    print("try again", err )
    x = int(input("give a number: ")) # cat

except: # catch all runtime error
    print("something went wrong")

else: # run this block if no runtime error
    print(x)

finally: # print whatever the result
    print("print")
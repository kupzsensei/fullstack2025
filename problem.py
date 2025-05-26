# In the United States, it’s customary to leave a tip for your server after dining in a restaurant, 
# typically an amount equal to 15% or more of your meal’s cost.
# Not to worry, though, we’ve written a tip calculator for you, below!

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO


def percent_to_float(p):
    # TODO


main()
# Here’s how to test your code manually:

# Run your program with python tip.py. Type $50.00 and press Enter. Then, type 15% and press Enter.
# Your program should output:
# Leave $7.50    
# Run your program with python tip.py. Type $100.00 and press Enter. Then, type 18% and press Enter. 
# Your program should output:
# Leave $18.00
# Run your program with python tip.py. Type $15.00 and press Enter. Then, type 25% and press Enter. 
# Your program should output
# Leave $3.75

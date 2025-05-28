name = "firtName" 

# name =  ["k" , "e" , "n" ]

for c in name:
    if c.isupper():
        print("_", end="")
        print(c.lower(), end="")
    else:
        print(c , end='')

print()
statement = input("how is the day today? ")
if "sunny" in statement :
    print("Dont go outside then")
elif "rainy" in statement:
    print("Take a umbrella then")
else:
    print("Have a Good Day then")

for x in statement:
    print(x)   
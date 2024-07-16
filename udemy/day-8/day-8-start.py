# greet function
def greet(input):
    for i in range(0, input):
    
        print("Starting up again")
    
x = 5
# greet(x)

# func with one input
def greet_with_name(name):
    print(f"Hello {name}")



# greet_with_name(full_name)

# func with multiple inputs
def greetings(name, location):
    print(f"\nHi, {name}!")
    print(f"What's the weather like in {location}?\n")

greetings(location= "Boston", name = "Mr.Turra")
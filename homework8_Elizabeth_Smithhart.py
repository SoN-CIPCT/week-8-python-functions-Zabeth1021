# Defining the function with the * in front of the parameter allows it to collect as many arguments as the calling line provides.
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

# Calling the function  with two different ingredient choices.
make_sandwich("Ham", "Cheese", "Lettuce", "Tomato")
make_sandwich("Turkey", "Bacon", "Avocado")

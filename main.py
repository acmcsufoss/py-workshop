"""
This is a multiline comment
This is a multiline comment
This is a multiline comment
"""


def my_function(name: str, amount: int = 1) -> int:
    """
    my_function prints hello world.
    """
    print(("hello " + name) * amount)
    return amount**2


# This is the main entry point of the program.
if __name__ == "__main__":
    print("hello world")
    x = 1 + 1
    print(x)

    my_string = "hello world"
    multi_line_string = """
    This is a multiline string
    This is a multiline string
    This is a multiline string
    """

    print(my_string[5:])
    print(my_string[:5])
    print(my_string[2:5])

    # Convert integer to a string.
    print(str(1) + str(1))
    print(1 + 1)

    # Integers.
    my_int = 1
    my_float = 1.0
    print(int("5"))
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    print((first_number) + (second_number))
    print(float("5.5"))

    # Control structures.
    is_ready = True
    is_patrick_ready = False
    if is_ready:
        print("I'm ready!")
    elif is_patrick_ready:
        print("Patrick is ready!")
    else:
        print("I'm not ready! 😢")

    count = 0
    while is_ready:
        count += 1
        print(count)
        if count == 10:
            is_ready = False

    # Ternary operator.
    happiness_level = 10 if is_ready else 0

    # Lists.
    my_list: list[int] = []
    my_list.append(1)
    first_item = my_list[0]
    print(first_item)

    # # Remove from list.
    my_list.remove(1)
    print(my_list)

    # # Iterate over list.
    my_list = [1, 2, 3, 4, 5]
    for item in my_list:
        print(item)

    # Dictionaries.
    my_dictionary = {"name": "Patrick"}
    my_dictionary["age"] = "30"
    my_dictionary["is_happy"] = "True"
    del my_dictionary["is_happy"]
    print(my_dictionary["name"])

    # Functions.
    result = my_function("Ethan", 3)
    print(result)

    # Files.
    with open("LICENSE", "r") as file:
        print(str(file.read()))

    # Write to file.
    level = 0
    with open("test.txt", "w") as file:
        file.write(str(level))

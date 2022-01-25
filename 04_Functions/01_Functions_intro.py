# def woof(number_of_woofs):
#     print("Woof!" * number_of_woofs)
#
#
# def greeting(name):
#     print(f"Hello to you, {name}")
#
#
# greeting("David")


def shopping(name, *items, shout=False):  # multiargs
    if shout:
        name = name.upper()
    for item in items:
        print(f"{name}! Don't forget to buy a {item}")


shopping("David", "banana", "apple", "orange")


# Type Hints

def greeting(name: str = "David"):
    print("Hello to you, " + name)


def add_user():
    pass


print("All finished")


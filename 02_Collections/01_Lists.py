# Lists

# shopping_list = ["eggs", "bread", "bananas", "tea"]
# print(shopping_list, type(shopping_list))
#
# print(len(shopping_list))
#
# print(shopping_list[0])
# print(shopping_list[-1])
#
# shopping_list[2] = "milk"
# print(shopping_list)
# # shopping_list[4] = "biscuits"
#
# shopping_list.append("biscuits")
# print(shopping_list)
#
# shopping_list.append("bread")
# shopping_list.append("bread")
# print(shopping_list)
#
# shopping_list.remove("bread")
# print(shopping_list)
#
#
# last_item = shopping_list.pop()
# print(shopping_list)
# print(last_item)

mixed = [1, 2, "three", True, None, ["another", "list"], 6, 7, 8, 8]
# print(mixed)

# mixed[1] = 2.0
# print(mixed)

# LISTS ARE MUTABLE
#
# print(mixed[2:7:2])
# print(mixed[7:2:-1])
# print(mixed[::3])
#
# sublist = mixed[5].copy()
# print(sublist)
# mixed[5][1] = 'b'
# print(mixed)
# print(sublist)

# Tuples

colours = ("red", "blue", "green", "red")
print(colours, type(colours))

print(colours[0])
# colours[0] = "maroon"

# Tuples are IMMUTABLE

print(colours.count("red"))
print(colours.index("green"))


list_in_tuple = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

print(len(list_in_tuple))
list_in_tuple[0].append("SUCCESS")
print(list_in_tuple)
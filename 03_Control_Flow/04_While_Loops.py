# for x in ['a', 'b', 'c', 'd', 'e']:
#     break_for = False
#     i = 100
#     while i < 110:
#         print(x, i)
#         if x == 'b' and i == 105:
#             break_for = True
#             break
#         i += 1
#     if break_for:
#         break
#
# prompt_user = True
# age = None
# while prompt_user:
#     age = input("What is your age?\n")
#     if age.isdigit():
#         if int(age) <= 119:
#             prompt_user = False
#         else:
#             print("You are not that old")
#     else:
#         print("Please provide age in digits")
#
# print(f"Double your age is {int(age) * 2}")

# Max age = 119


i = 1
while True:
    print(i)
    if i == 10:
        break
    print("Adding 1 to i...")
    i += 1
    if i == 3:
        continue
    print("1 has been added to i.")
    print("Back to the start of the loop")
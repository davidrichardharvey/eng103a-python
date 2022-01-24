# Numeric!

# i = 375  # int
# f = 3.75  # float
# c = 3j + 2  # complex
#
# print(c, type(c))
#
# add = 3 + 5
# subtract = 3 - 5
# multiply = 3 * 5
# divide = 3 / 5
# power = 3 ** 5
# modulo = 3 % 5
#
# print(13 % 3)  # 4 * 3 = 12, 13 - 12 = 1
# print(12 % 3)
#
# print(14 // 3, 14 % 3)
# print(12 / 3)
#
# third = 1 / 3
# print(third)
# print(third * 3)


# Strings!

single = 'String in single quotes'
double = "String in double quotes"

single_in_double = "This is David's string"
double_in_single = 'This is a "string"'
both = "This is David's \"string\""
print(both)

# Indexing and slicing

# hi = "Hello World!"
# print(hi[0])  # Python starts counting at zero!
# print(hi[6])
# print(hi[-1])
# print(hi[0:7])
# # print "lo Wo"
# print(hi[3:8])

# Methods

# white_space = "      lots of white space       "
# print(len(white_space))
# print(white_space.strip())
# print(white_space.upper())
# print(white_space.strip().capitalize())
# print(white_space.strip().count(" "))
# print(white_space.replace("o", "ooooo").replace("i", "oooo").replace("a", "ooooo"))
#
# print(white_space)
#
# # F-Strings (formatted strings)
#
# pi = 3.14159265359
# print(pi)
# print(f"Pi to 3dp: {pi:.3f}")
# print(f"Pi to 5dp: {pi:.5f}")
# print(f"Pi to 0dp: {pi:.0f}")
#
# score = 16
# max_score = 26
#
# print(f"You scored {score / max_score}")
# print(f"You scored {score / max_score:.2f}")
# print(f"You scored {score / max_score:%}")
# print(f"You scored {score / max_score:.2%}")
# print(f"You scored {score / max_score:.0%}")

# Boolean

t = True
f = False

# print(t, type(t))
#
# print(3 + 2 == 5)
# print(12 % 3 == 0)
# print(5 != 5)
# print(1 < 100)
# print(100 < 1)
# print(5 < 5)
# print(5 <= 5)
# # print(5 >= 5)
#
# age = 16
# drink = 'alcohol'
#
# print(age > 18 and drink == 'alcohol')
# print(age > 18 or drink == 'alcohol')

# hi = "HELLOWORLD"
# print(hi.isalpha())
# print(hi.islower())
# print(hi.isupper())
# print(hi.endswith("rld"))
# print(hi.startswith("Hell"))

print(bool(1))
print(bool(0))
print(bool(23423))
print(bool(-2342))
print(bool(1.342))

print(bool("Hello"))
empty = ""

print(empty, type(empty), bool(empty))

# None

n = None

print(n, type(n))
print(bool(None))

print(n is None)

print(type(15) is int)

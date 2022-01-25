# age = 17
# film_showing = False
#
# if age >= 18 and film_showing:
#     print("You are allowed to buy a ticket for this film.")
#     print("Enjoy the film!")
#
#     print("Still in the if-block")
# elif age == 17:
#     print("Come back next year")
# else:
#     print("No dice")
#
# print("This will always print")

certificate = '12A'  # U, PG, 12, 12A, 15, 18
# Check the certificate
# Print corresponding info about the film

if certificate.upper() == 'U':
    print('Suitable for all ages')
elif certificate.upper() == 'PG':
    print('Parental guidance recommended')
elif certificate.upper() in ('12', '12A'):
    print('Recommended for ages 12 and above')
elif certificate == '15':
    print('Ages 15 and up')
elif certificate == '18':
    print('Adults only')
else:
    print('Certificate not recognised')
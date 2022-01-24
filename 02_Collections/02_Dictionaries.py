# Dictionaries

# Key-Value Pairs

my_dict = {'key': 'value'}

table = {
    'name': 'The Table',
    'colour': 'light brown',
    'dimensions': {
        'height': 120,
        'length': 200,
        'width': 150
    }
}

# Print the width (use get a [] methods)
print(table.get('dimensions').get('width'))
print(table['dimensions']['width'])

print(table)
print(table.keys())
print(table.values())
print(table.items())

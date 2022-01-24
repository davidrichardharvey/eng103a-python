pokemon = {'Bulbasaur', 'Squirtle', 'Charmander'}

print(pokemon, type(pokemon))

pokemon.add("Pikachu")
print(pokemon)

# Sets are mutable and unordered

pokemon.discard('Bulbasaur')
print(pokemon)

pokemon.add('Bulbasaur')
pokemon.add('Bulbasaur')
print(pokemon)

l = [1, 2, 5, 3,34,6,4,2,2,5,0,3,1,3,4,6,3,1,3]
print(l)
print(set(l))

# Frozen Set

x = frozenset(['let', 'it', 'go'])
print(x)

# Frozen sets are immutable sets

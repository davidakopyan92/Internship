colors = {'red', 'blue', 'orange'}
print("Initial set: {'red', 'blue', 'orange'}  differs from a printed set:", colors)

colors.add('blue')
print('\nUnsuccessful attempt to add '
      'already existing color "blue":\n'
      'duplicates not allowed <=> unindexed \n')

colors1 ={'blue', 'blue', 'red', 'white','red', 'black'}
print("Duplicates are excluded from the initial set, {'blue', 'blue', 'red', 'white','red', 'black'}.\n"
      "This proves set is mutable. "
      "It is the items that are immutable. Final set : ", colors1)




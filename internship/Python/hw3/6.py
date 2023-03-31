country = {}
country.update({'eu_member': 'no'})
print(list(country.keys()))

neighbours = ['neighbor1', 'neighbor2']
neighbours_str = ', '.join(neighbours)
country['neighboring_countries'] = neighbours_str
print(country)

if 'religion' not in country.keys():
    print('No religion is specified')
    country['religion'] = 'Christianity'
    print('Religion is added:', country['religion'])


my_dict = {'Anton': 1996, 'Denis': 1995, 'Anna': 1990}
print(my_dict)
print(my_dict['Anna'])
print(my_dict.get('Olga'))
my_dict.update({'Nasta':1997,'Marina':2000})
print(my_dict)
a=my_dict.pop('Anna')
print(my_dict)
print(a)

# задание на множества

my_set={1,2,2,3,3,4,4,1,6,'str', (1,2,3)}
print(my_set)
print(my_set.discard(2))
print(my_set)



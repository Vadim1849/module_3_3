def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print('первое условие')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])


print()
print('второе условие')
values_list = ['Vadim', 123, True]
print_params(*values_list)
values_dict = {'a': 'Pavel', 'b': False, 'c': 55}
print_params(**values_dict)


print()
print('третье условие')
values_list_2 = [66.6, 'Страница']
print_params(*values_list_2, 42)

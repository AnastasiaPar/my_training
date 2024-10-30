# Задача "Распаковка":
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

# 2.Распаковка параметров:
values_list = [1]
values_dict = {'b': 'строка', 'c': True}
print_params(*values_list, **values_dict)

#3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

# пометки для себя !Не передавай списки задавая по умолчанию пустой список или другой изменяемый тип данных!
# Можно передавать вот так
# (список создаётся локально, мы не влияем на его изменение вне функции)
# def append_to_list(item, list_my=None):
#   if list_my is None:
#    list_my = []
#   list_my.append(item)
# print(list_my)
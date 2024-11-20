nums = [5,6,2,1,3,4]

def bubble_sort(ls):
    # чтобы цикл сработал хотя бы 1 раз, задаем значение перемнной True
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls)-1):
            if ls[i] > ls[i+1]: # если один соседний эелемент больше другого, то
                ls[i], ls[i+1] = ls[i+1], ls[i] # меняем местами
                swapped = True
# bubble_sort(nums)
# print(nums)


def selection_sort(ls):
    # количество отсортированных эл-ов
    for i in range(len(ls)):
        lowest = i # чтобы плучить индекс самого малеького эл-та
        # цикл для перебора неотсортированных эл-ов
        for j in range(i+1, len(ls)): # список который будет запускаться с i+1 (т.е буду браться элементы неотсортированной части и сравниватья с самым маленьким эл-ом
            if ls[j] < ls[lowest]:
                lowest = j
        # самый маленький эл-т меняем местами с первым эл-ом
        ls[i], ls[lowest] = ls[lowest], ls[i]


def insertion_sort(ls):
    # Начинаем сортировать со 2 эл-та, так как 1 эл-т уже считается отсортированным
    for i in range(1, len(ls)):
        item = ls[i]
        # берем эл-т для вставки и сохраняем ссылку на индекс предыдущего эл-та
        j = i - 1
        # отсортированный кусок от списка двигаем вперед, если он больше эл-та для вставки
        while j >= 0 and ls[j] > item:
            ls[j + 1] = ls[j]
            j -= 1
            # вставляем элемент
        ls[j + 1] = item





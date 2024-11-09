#Создайте новую функцию test_function
# Создайте внутри test_function другую функцию - inner_function,
# Эта функция должна печатать значение "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function

def test_function():
    def inner_function():
        print('Я в области видимой функции')
    inner_function()
    return

# inner_function() - ошибка: name 'inner_function' is not defined. Did you mean: 'test_function'?

test_function()
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function() #  здесь ничего не возвращает

 # inner_function() Вызов функци inner_function() вне функции test_function приводит к появлению ошбики -
# NameError: name 'inner_function' is not defined
# вследствие различия пространства имён, т.к.  мы не можем доставать значения внутри функции (извне)

test_function() # Здесь - работает, но это объемлющая функция
def my_shiny_new_decorator(function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate()  # Сама функция
        print("А я - код, срабатывающий после")

    # Вернём эту функцию
    return the_wrapper_around_the_original_function


# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")


stand_alone_function()
# Я простая одинокая функция, ты ведь не посмеешь меня изменять?
# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
# который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
# готовую к использованию функцию:
stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
stand_alone_function_decorated()

# Если бы мы хотели, чтобы каждый раз, во время вызова stand_alone_function,
# вместо неё вызывалась stand_alone_function_decorated.
# Для этого просто перезапишем stand_alone_function:
stand_alone_function = my_shiny_new_decorator(stand_alone_function)
stand_alone_function()


# Размещение конструкции @my_shiny_new_decorator перед определением функции равносильно использованию конструкции вида stand_alone_function = my_shiny_new_decorator(stand_alone_function)
# можно было записать предыдущий пример, используя синтаксис декораторов:
@my_shiny_new_decorator
def another_stand_alone_function():
    print("Оставь меня в покое")


another_stand_alone_function()



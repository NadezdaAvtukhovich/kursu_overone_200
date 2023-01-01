# Можно использовать несколько декораторов для одной функции, например так:
def bread(func):
    def wrapper():
        print()
        func()
        print("<\______/>")

    return wrapper

def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")

    return wrapper

def sandwich(food="--ветчина--"):
    print(food)

sandwich()
# использование нескольких декораторов:
sandwich = bread(ingredients(sandwich))
sandwich()

# Или используя синтаксис декораторов:
@bread
@ingredients
def sandwich(food="--ветчина--"):
    print(food)

sandwich()

# Важен порядок декорирования. Сравните с предыдущим примером:
@ingredients
@bread
def sandwich(food="--ветчина--"):
    print(food)

sandwich()



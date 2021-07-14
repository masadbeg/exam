#Напишите декоративную функцию, которая будет обрамлять функцию divide и будет проверять 
# являются ли оба аргумента числами. И не является ли аргумент b нулём
def wrapper(function_to_decorate):
    def divide(a, b):
        if type(a) == int and type(b)==int and b != 0:
            return f'Ваш результат: {function_to_decorate(a,b)}'
        else:
            print('Ошибка на ноль делить нельзя')
    return divide
@wrapper

 

def divide(a, b):
    return a/b

 

print(divide(5,2))
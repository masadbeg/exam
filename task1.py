#Напишите функцию, которая принимает в себя строку с датой в формате День.Месяц.Год, и возвращает возраст человека
def func(age):
    d_list = age.rsplit('.')
    result = ((2021-int(d_list[2]))*365 + (5-int(d_list[1]))*30 + 7 + int(d_list[0]))/365
    print(f'You are {int(result)} years old')

 

func('15.01.1995')
func('28.11.1195')
func('21.04.2003')



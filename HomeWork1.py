#Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

n = int(input("Введите число обозначающее день недели:"))
if n==1:
    print('понедельник - будни')
elif n==2:
    print('вторник - будни')
elif n==3:
    print('среда - будни')
elif n==4:
    print('четверг - будни')
elif n==5:
    print('пятница - будни')
elif n==6:
    print('суббота - выходной')
elif n==7:
    print('воскресенье - выходной')
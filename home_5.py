# Реализуйте алгоритм перемешивания списка

from random import randint

my_list = [6,-75,4.7,True,"dog",33,20] # произвольный список

for i in range(7):
    unknown = randint(0,6)             # случайный индекс списка
    temp = my_list[i]                  #  | 
    my_list[i] = my_list[unknown]      #  | меняем местами два элемента
    my_list[unknown] = temp            #  |

print(my_list)

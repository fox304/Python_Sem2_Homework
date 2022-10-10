# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

with open("num.txt","r") as pos:
    num_text = pos.read()

num_text = num_text.split()
num_map = list(map(float,num_text))
print(num_text,sum(num_map))

#Известно, что в первой группе суммарное количество решенных на контесте задач равно a, а во второй — b. 
#Всего на контесте было предложено n задач, а также известно, что каждый студент решил не менее одной (и не более n) задач.
#По заданным a, b и n определите, могло ли в первой группе быть строго больше студентов, чем во второй.

a = int(input())
b = int(input())
ma = int(input())

if b % ma == 0:
    if a > b // ma:
        print("YES")
    else:
        print("NO")
else:
    if a > b // ma + 1:
        print("YES")
    else:
        print("NO")

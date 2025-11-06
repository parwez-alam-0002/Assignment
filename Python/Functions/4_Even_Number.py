# Print even numbers from 1-100

def fun_print(st,end):
    for i in range(st,end+1):
        if not i%2:
            print(i,end=" ")

fun_print(end=100,st=1)

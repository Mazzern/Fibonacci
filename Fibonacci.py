#フィボナッチ数
def Fib(n, a=1, b=0):
    if n < 1:
        print(b)
    else:
        print(b)
        Fib(n-1, a+b, a)

#実行
n = int(input('Enter a number: '))
Fib(n,1,0)

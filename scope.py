

x = 0

def func(arg):
    x = arg
    def innerfunc():
        print x
    return innerfunc()



def retLambda(arg):
    x = arg
    action = (lambda n: x + n)
    return action

print 'global x =',x

f = func(2)

f
a = retLambda(1)
print a(4)


print 'global x =',x

def func_loop():
    x = 1
    for i in range(5):
        #x = 2
        def f(i):
            i = i + 1
        f(i)
        print i,x + i

func_loop()

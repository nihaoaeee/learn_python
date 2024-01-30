#coding=utf-8
lst = [1 ,2 ,3, 4, 5]
g = (n for n in lst if n in lst)
lst = [0, 1, 2]
print(list(g))


class C:
    def f(self):
        pass

o = C()

a=id(o.f)
b=id(o.f)
print(a,b)

from objprint import op
op.config(arg_name=True)

op(set([x for x in range(5)]))
op(set([str(x) for x in range(5)]))



def f():
    a = 0
    print(locals())
    exec("print(locals());a=1;print(locals())")
    print(locals())
    print(a)

f()

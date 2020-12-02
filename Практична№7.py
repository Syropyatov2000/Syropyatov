from cmath import exp
from tkinter import Y


def linspace(param, param1, param2):
    pass

>>> importmatplotlib.pyplotasplt
>>> plt.plot([1, 3, 2, 4])
[<matplotlib.lines.Line2D object at 0x01A00430>]
>>> plt.show()
def f(t):
    return t**2*exp(-t**2)
t = linspace(0, 3, 51)
# 51 точкаміж 0 та 3y = f(t) plt.plot(t, y) plt.show()
t = linspace(0, 3, 51)
y1 = t**2*exp(-t**2)
y2 = t**4*exp(-t**2)
Y.plot(t, y1, label='t^2*exp(-t^2)')
Y.plot(t, y2, label='t^4*exp(-t^2)')
# декоративначастинаplt.xlabel('t')
# plt.ylabel('y')
# plt.title('Plotting two curves in the same plot')
# plt.legend()
# plt.show()
t = linspace(0, 3, 51)
y1 = t**2*exp(-t**2)
y2 = t**4*exp(-t**2)
y3 = t**6*exp(-t**2)
Y.plot(t, y1, 'g^',
Y(exp)=x*sin(5*x), x=[-2...5]
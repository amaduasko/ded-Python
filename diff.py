import math
from sympy import *

print('Форма функции : f(t, x(t)) =  ax(t-tau) на интервале [t0, t1]', '\n')

t_0 = int(input('Ведите t0: '))
t_1 = int(input('Ведите t1: '))
tau = int(input('Ведите чаг tau: '))
a = int(input('Ведите a: '))
x_0 = int(input('Ведите начальное условые x0: '))
t = symbols('t')

print('<=============================================================>', '\n')
print(f'Ваша функция : f(t,x(t)) = {a}x(t-{tau})', '\n')
print('<=============================================================>', '\n')


starter_x = x_0*(a * (t - tau) + 1)


def x(periode):
    if(t == 0):
        return x_0
    else:
        dif_x = a*x_0*(a * (periode - tau) + 1)
        integrated_x = integrate(dif_x, t)
        return integrated_x


sum_max = math.ceil((t_1 - t_0) / tau)
arr_tau = []

currentTau = tau
for i in range(sum_max):
    if currentTau < t_1:
        lastTau = currentTau
        currentTau += tau
        arr_tau.append([lastTau, currentTau])

print([0, tau], '\n')
print(f'x(t) = {starter_x} ', '\n')

for index in range(len(arr_tau)):
    interval = arr_tau[index]
    periode = t - interval[0]
    print(interval, '\n')
    print(f'x(t) = {x(periode)} + C_{index+1}', '\n')

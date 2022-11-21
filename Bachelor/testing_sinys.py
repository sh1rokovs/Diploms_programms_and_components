from scipy.integrate import quad # модуль для интегрирования
import matplotlib.pyplot as plt # модуль для графиков
import numpy as np # модуль для операций со списками и массивами
T=np.pi; w=2*np.pi/T# период и круговая частота
def func(t):# анализируемая функция
         if t<np.pi:
                  p=np.cos(t)
         else:
                  p=-np.cos(t)
         return p
def func_1(t,k,w):# функция для расчёта коэффициента a[k]
         if t<np.pi:
                  z=np.cos(t)*np.cos(w*k*t)
         else:
                  z=-np.cos(t)*np.cos(w*k*t)
         return z
def func_2(t,k,w):#функция для расчёта коэффициента b[k]
         if t<np.pi:
                  y=np.cos(t)*np.sin(w*k*t)
         else:
                  y=-np.cos(t)*np.sin(w*k*t)
         return y
a=[];b=[];c=4;g=[];m=np.arange(0,c,1);q=np.arange(0,2*np.pi,0.01)# подготовка списков для численного анализа
a=[round(2*quad(func_1, 0, T, args=(k,w))[0]/T,3) for k in m]# интеграл для a[k], k -номер гармоники
b=[round(2*quad(func_2, 0, T, args=(k,w))[0]/T,3) for k in m]# интеграл для b[k], k -номер гармоники
F1=[a[1]*np.cos(w*1*t)+b[1]*np.sin(w*1*t) for t in q]#функции для гармоник
F2=[a[2]*np.cos(w*2*t)+b[2]*np.sin(w*2*t) for t in q]
F3=[a[3]*np.cos(w*3*t)+b[3]*np.sin(w*3*t) for t in q]
plt.figure()
plt.title("Классический гармонический анализ функции \n при t<pi  f(t)=cos(t)  при t>=pi  f(t)=-cos(t)")
plt.plot(q, F1, label='1 гармоника')
plt.plot(q, F2 , label='2 гармоника')
plt.plot(q, F3, label='3 гармоника')
plt.xlabel("Время t")
plt.ylabel("Амплитуда А")
plt.legend(loc='best')
plt.grid(True)
F=np.array(a[0]/2)+np.array([0*t for t in q-1])# подготовка массива для анализа с a[0]/2
for k in np.arange(1,c,1):
         F=F+np.array([a[k]*np.cos(w*k*t)+b[k]*np.sin(w*k*t) for t in q])# вычисление членов ряда Фурье
plt.figure()
P=[func(t) for t in q]
plt.title("Классический гармонический синтез")
plt.plot(q, P, label='f(t)')
plt.plot(q, F, label='F(t)')
plt.xlabel("Время t")
plt.ylabel("f(t),F(t)")
plt.legend(loc='best')
plt.grid(True)
plt.show()
# Exercise 07 Driven Nonlinear Pendulum
#####邹志远_2014301020056

##目标
---
作业3.13&3.14
##背景
---
对于一个无阻尼没有驱动力作简谐运动的摆，它的运动满足以下方程:
$$\frac{d^2\theta}{dt^2}=-\frac{g}{l}\theta$$
拆分可得
$$\frac{d\omega}{dt}=-\frac{g}{l}\theta$$
$$\frac{d\theta}{dt}=-\omega$$
上章中euler法计算了炮弹轨迹的ODE并求出了轨迹，但对于本问题euler法并不适用，使用euler法会导致无论dt取的多小，对于任何非零的dt，系统的能量总是增多的。因此需要改用euler_cromer方法，具体操作为：
$$\omega_{i+1}=\omega_i-(g/l)\theta_i\Delta t$$
$$\theta_{i+1}=\theta_i+\omega_{i+1}\Delta t$$
将euler法中的$\omega_i$改为$\omega_{i+1}$即可避免能量的无限增多
在此基础上引进阻尼和驱动力可得
$$\frac{d\omega}{dt}=-\frac{g}{l}\theta-q\omega+F_Dsin(\Omega_Dt)$$
$$\frac{d\theta}{dt}=-\omega$$
$$\omega_{i+1}=\omega_i-((g/l)\theta_i-q\omega+F_Dsin(\Omega_Dt))\Delta t$$
$$\theta_{i+1}=\theta_i+\omega_{i+1}\Delta t$$
$$t_{i+1}=t_i+\Delta t$$

##程序
---
3.13
```python
#coding:utf-8
import pylab as pl
import math
class Driven_Nonlinear_Pendulum:

    def __init__(self,inital_angle1=0,inital_angle2=1.0,\
                 string_length=9.8,gravity=9.8,time_step=0.04,\
                 damping=0.5,driving_force=0.5):
        self.a1=[inital_angle1]
        self.t1=[0]
        self.a2=[inital_angle2]
        self.t2=[0]
        self.l=string_length
        self.g=gravity
        self.dt=time_step
        self.q=damping
        self.Fd=driving_force
        self.omg_d=2.0/3
        self.da=[]

    def pendulum1(self):
        t=self.t1[0]
        a=self.a1[0]
        vw=0.0
        while(t<150):
            vw=vw - (self.g/self.l*math.sin(a)+self.q*vw-self.Fd*math.sin(self.omg_d*t))*self.dt
            a=a+vw*self.dt
            while(abs(a)>math.pi):
                if (a > math.pi):
                    a = a - 2 * math.pi
                elif (a < -math.pi):
                    a = a + 2 * math.pi
            t=t+self.dt
            self.a1.append(a)
            self.t1.append(t)


    def pendulum2(self):
        t=self.t2[0]
        a=self.a2[0]
        vw=0.0
        while(t<150):
            vw=vw - (self.g/self.l*math.sin(a)+self.q*vw-self.Fd*math.sin(self.omg_d*t))*self.dt
            a=a+vw*self.dt
            while(abs(a)>math.pi):
                if (a > math.pi):
                    a = a - 2 * math.pi
                elif (a < -math.pi):
                    a = a + 2 * math.pi
            t=t+self.dt
            self.a2.append(a)
            self.t2.append(t)

    def compare(self):
        for i in range(len(self.t1)):
            da=abs(self.a1[i]-self.a2[i])
            self.da.append(da)

    def show_result(self):
        pl.figure(1)
        pl.title('Trajectory of cannon shell')
        pl.plot(self.t1,self.a1)
        pl.xlabel('t ($s$)')
        pl.ylabel('$\theta$ ($radians$)')
        pl.figure(2)
        pl.title('Trajectory of cannon shell')
        pl.title('Trajectory of cannon shell2')
        pl.plot(self.t2,self.a2)
        pl.xlabel('t ($s$)')
        pl.ylabel('$\theta ($radians$)')
        pl.figure(3)
        pl.title('$\Delta \theta$ versus time')
        pl.yscale('log')
        pl.plot(self.t1,self.da)
        pl.xlabel('t ($s$)')
        pl.ylabel('$\Delta\theta$ ($radians$)')
        pl.show()
a=Driven_Nonlinear_Pendulum()
a.pendulum1()
a.pendulum2()
a.compare()
a.show_result()
```
[代码链接](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/exercise07.py)
3.14代码可以通过在第52行后简单插入```self.q=self.q+0.05```来实现

##运行结果
---
![](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/ex7_1.png)
![](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/ex7_2.png)
![](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/ex7_3.png)
##反思
---
![](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/ex7_4.png)

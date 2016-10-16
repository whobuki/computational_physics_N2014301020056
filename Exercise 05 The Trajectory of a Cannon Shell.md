

# Exercise 05 The Trajectory of a Cannon Shell
#####邹志远_2014301020056

##背景
---
炮弹在空气中的运动受到重力空气阻力等多种力的作用并不是做完美的抛物线运动

##正文
---
我们使用欧勒法可以简单又不失精准的解决炮弹运动这类ODE问题。不考虑阻力的情况下炮弹运动遵循以下方程：

<img src="http://latex.codecogs.com/gif.latex?\x_{i+1}=x_i+v_{x,i}\Delta{t}" alt="" title="" />

<img src="http://latex.codecogs.com/gif.latex?\v_{x,i+1}=v_{x,i}" alt="" title="" />

<img src="http://latex.codecogs.com/gif.latex?\y_{i+1}=y_i+v_{y,i}\Delta{t}" alt="" title="" />

<img src="http://latex.codecogs.com/gif.latex?\v_{y,i+1}=v_{y+i}-g\Delta{t}" alt="" title="" />

以下是程序源代码：
```python
#coding:utf-8
import pylab as pl
import math as mt
class cannon_shells:
    def __init__(self,initial_velocity=0.7,g=0.0098,range=0,height=0,time_step=0.01,initial_angle=30.0,da=5.0):
        self.v=[initial_velocity]
        self.a=[initial_angle]
        self.g=g
        self.dt=time_step
        self.da=da
        self.x=[range]
        self.y=[height]

    def run(self):
        _a=self.a[0]
        while(_a<=60):    
            _a+=self.da
            self.a.append(self.a[-1]+self.da)
            t = 2 * mt.sin(_a / 180.0 * mt.pi) * self.v[0]/self.g
            vx=mt.cos(_a / 180.0 * mt.pi) * self.v[0]
            vy=mt.sin(_a / 180.0 * mt.pi) * self.v[0]
            _time=0
            xi = [0]
            yi = [0]
            while(_time<t):
                xi.append(xi[-1]+self.dt*vx)
                yi.append(yi[-1]+self.dt*vy)
                vy=vy - self.g * self.dt
                _time+=self.dt
            self.x = self.x + xi
            self.y = self.y + yi

    def show_results(self):
        # coding:utf-8
        font = {'family': 'yahei',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }
        font2 = {'family': 'yahei',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }
        pl.title('Trajectory of cannon shell')
        pl.text(0.95 * max(self.x), 0.95 * max(self.y),'No drag', fontdict=font)
        pl.text(0.8 * self.tx[1], 1.01 * self.ty[1], '30', fontdict=font2)
        pl.text(0.8 * self.tx[2], 1.01 * self.ty[2], '35', fontdict=font2)
        pl.text(0.8 * self.tx[3], 1.01 * self.ty[3], '40', fontdict=font2)
        pl.text(0.8 * self.tx[4], 1.01 * self.ty[4], '45', fontdict=font2)
        pl.text(0.8 * self.tx[5], 1.01 * self.ty[5], '50', fontdict=font2)
        pl.text(0.8 * self.tx[6], 1.01 * self.ty[6], '55', fontdict=font2)
        pl.text(0.8 * self.tx[7], 1.01 * self.ty[7], '60', fontdict=font2)
        pl.plot(self.x,self.y)
        pl.xlabel('x ($km$)')
        pl.ylabel('y ($km$)')
        pl.show()

a = cannon_shells()
a.run()
a.show_results()
```
---
程序运行的结果截图
![](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/exercise05_figure_1.png)
[附程序链接](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/exercise05.py)
##反思
---
编程过程中遇到了一些小问题如
尝试使用whlie循环来输出
```
        pl.text(0.8 * self.tx[1], 1.01 * self.ty[1], '30', fontdict=font2)
        pl.text(0.8 * self.tx[2], 1.01 * self.ty[2], '35', fontdict=font2)
        pl.text(0.8 * self.tx[3], 1.01 * self.ty[3], '40', fontdict=font2)
        pl.text(0.8 * self.tx[4], 1.01 * self.ty[4], '45', fontdict=font2)
        pl.text(0.8 * self.tx[5], 1.01 * self.ty[5], '50', fontdict=font2)
        pl.text(0.8 * self.tx[6], 1.01 * self.ty[6], '55', fontdict=font2)
        pl.text(0.8 * self.tx[7], 1.01 * self.ty[7], '60', fontdict=font2)
```
这一段不同角度图像的标记，使用了如下代码
```
a=[*计算生成的一串角度*]
        while(i<7):
            a=int(self.a[i])
            b=str(a)+'°'
            pl.text(0.85 * self.tx[i+1], 1.01 * self.ty[i+1], \
                    b, fontdict=font)
            i+=1

```
debug出错，发现pylab的函数不能很好的识别str，且不支持utf-8格式的‘°’符号（主程序中可以在开头加入```#coding:utf-8```来支持这些符号）
####实力有限不能很好的理解后面的空气阻力


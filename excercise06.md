# Exercise 06 The Trajectory of a Cannon Shell2

##目标
---
* 作业L1 2.10题强化版（引入迎面风阻）
* 作业L2 2.10题进一步升级，发展“超级辅助精确打击系统”（考虑炮弹初始发射的时候发射角度误差正负2度，速度有5%的误差，迎面风阻误差10%，计算需要考虑海拔高度的影响，使用绝热模型进行计算，误差描述使用最简单的均匀分布描述）

#####附2.10题目

> 2.10 Generalize the program developed for the previous problem so that it can deal with situations in which the target is at a different altitude than the cannon. Consider cases in which the target is higher and lower than the cannon. Also investigate how the minimum firing velocity required to hit the target varies as the altitude of the target is varied.

##背景
---
> The Euler method we used to treat the bicycle problem can easily be generalized to deal with motion in two spatial dimensions. To be specific, we consider a projectile such as a shell shot by a cannon. We have a very large cannon in mind, and the large size will determine some of the important physics...

不考虑空气阻力时炮弹运动满足以下方程
![](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/ex05_1.jpg)

* 空气阻力满足，其中$\rho_0$为海平面处的空气密度。：
![](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/ex6_3.png)


* 考虑绝热模型下空气密度随海拔高度的变化，其中$y_0\approx10km$：

![](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/ex6_4.png)

即考虑海拔高度和空气阻力时，炮弹运动满足：

![](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/ex6_5.png)

* 再引入迎面风
迎面风的作用等于改变了炮弹相对空气的运动速度，式中$v_w$为风速(迎面相对速度相加)：

![](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/ex6_6.png)

综上所述，炮弹运动满足：

![](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/ex6_7.png)

##程序
---
```python
#coding:utf-8
import pylab as pl
import math
import random
class cannon_shell:
    def __init__(self,initial_velocity=2,g=0.0098,range=0,height=0,target_range=100,target_height=1,time_step=0.005,\
                 da=0.00001*math.pi,\
                 wind_speed=0.01,b_m=0.04,accuracy=0.01):
        self.v=initial_velocity*1.0
        self.Vw=wind_speed*1.0
        self.a=math.atan((target_height-height)/(target_range-range))*1.0
        self.g=g*1.0
        self.dt=time_step*1.0
        self.da=da*1.0
        self.x=[range*1.0]
        self.y=[height*1.0]
        self.xt=target_range*1.0
        self.yt=target_height*1.0
        self.b_m=b_m*1.0 #B2/m
        self.ture_x=[]
        self.ture_y=[]
        self.rand_x=[]
        self.rand_y=[]
        self.dxdy=accuracy*1.0

    def pre_run_test(self): #初步判断减少计算量
        _a= 0.001*math.pi
        da= 0.001*math.pi
        dxdy=1.0
        aa=[]
        t=1
        a_max=0.5 * math.pi
        while(t<10): #减少计算时间用
            can2=0 #辅助跳出循环用
            while (_a < a_max):
                can = 0  # 判断命中用（未命中=0）
                vx = math.cos(_a) * self.v
                vy = math.sin(_a) * self.v
                xi = [0]
                yi = [0]
                while (yi[-1] >= 0):
                    xi.append(xi[-1] + self.dt * vx)
                    yi.append(yi[-1] + self.dt * vy)
                    v = ((vx + self.Vw)**2+vy**2)**0.5
                    vx = vx \
                         - math.exp(-yi[-1] / 10) * self.b_m * v * (vx+self.Vw) * self.dt
                    vy = vy \
                         - self.g * self.dt \
                         - math.exp(-yi[-1] / 10) * self.b_m * v * vy * self.dt
                    if (abs(xi[-1] - self.xt) < dxdy and abs(yi[-1] - self.yt) < dxdy):  # 判断是否命中
                        can = 1 # 判断命中用（命中=1）
                        break
                if can: #找出近似的角度
                    aa.append(_a)
                    can2=1  #判断已经得到下次计算用的角度值
                elif can==0 and can2==1: break #跳出之后的多余循环
                _a = _a + da
            if aa==[]:
                if t==1 :
                    print "无法命中目标" #第一次循环时如果无法命中则判断无法命中目标
                else:
                    print "已达计算精度上限"
                    break #输出当前条件下可以达成的最高精度，使程序不至报错
            _a=min(aa)-da
            a_max=max(aa)+da
            da=da/5
            dxdy=dxdy/4
            _aa =aa #将本次正确计算的结果保存在_aa中
            aa=[]
            print "calculating*"+str(t)  #程序目前进行了几次运算（告诉你没有死机）
            t+=1
        self.a= 0.5*max(_aa)+0.5*min(_aa)
        self.dxdy=dxdy*4

    def accurate(self): #绘制无误差时的基准炮线
        _a = self.a
        vx = math.cos(_a) * self.v
        vy = math.sin(_a) * self.v
        xi = [0]
        yi = [0]
        while (yi[-1] >= 0):
            xi.append(xi[-1] + self.dt * vx)
            yi.append(yi[-1] + self.dt * vy)
            v = ((vx + self.Vw)**2+vy**2)**0.5
            vx = vx \
                 - math.exp(-yi[-1] / 10) * self.b_m * v * (vx+self.Vw) * self.dt
            vy = vy \
                 - self.g * self.dt \
                 - math.exp(-yi[-1] / 10) * self.b_m * v * vy * self.dt
            if (abs(xi[-1] - self.xt) < self.dxdy and abs(yi[-1] - self.yt) < self.dxdy):  # 判断是否命中
                n=((xi[-1] - self.xt)**2+(yi[-1] - self.yt)**2)**0.5
                print "理论炮弹命中坐标为("+str(xi[-1])+","+str(yi[-1])+")"
                print "误差为"+str(n)
        self.ture_x = xi
        self.ture_y = yi

    def run(self):   #绘制有随机误差时的炮线,并计算误差的平方均值
        t=1
        _dxdy=[]
        while t<=200:
            dxdy = []
            xi = [0]
            yi = [0]
            _a = self.a + 1 / 90 * math.pi * random.uniform(-1,1)
            vx = math.cos(_a) * self.v * (1 + 0.05 * random.uniform(-1,1))
            vy = math.sin(_a) * self.v * (1 + 0.05 * random.uniform(-1,1))
            Vw = self.Vw * (1 + random.uniform(-1, 1) * 0.1)
            while (yi[-1] >= 0):
                xi.append(xi[-1] + self.dt * vx)
                yi.append(yi[-1] + self.dt * vy)
                v = ((vx + Vw) ** 2 + vy ** 2) ** 0.5
                vx = vx \
                     - math.exp(-yi[-1] / 10) * self.b_m * v * (vx+Vw) * self.dt
                vy = vy \
                     - self.g * self.dt \
                     - math.exp(-yi[-1] / 10) * self.b_m * v * vy * self.dt
                n=((xi[-1] - self.xt) ** 2 + (yi[-1] - self.yt) ** 2) ** 0.5   #炮弹与目标的距离
                if abs(xi[-1] - self.xt) < self.xt/10 and abs(yi[-1] - self.yt) < self.yt/10:  #取较靠近目标的点
                    dxdy.append(n)
            t+=1
            _dxdy.append(min(dxdy))
            if t<=10:  #取其中几条轨迹画图
                self.rand_x = self.rand_x + xi
                self.rand_y = self.rand_y + yi
        amont=len(_dxdy)
        average1=0
        for i in range(amont):
            average1=average1+_dxdy[i]**2
        rms=(average1/amont)**0.5
        print "误差平方均值为"+str(rms)

    def show_result(self):
        pl.title('Trajectory of cannon shell')
        pl.plot(self.xt,self.yt,'ro',label="target")
        pl.plot(self.rand_x,self.rand_y,'--',label="random",color="green",linewidth=0.5,)
        pl.plot(self.ture_x,self.ture_y,label="accurate",color="blue",linewidth=2)
        pl.ylim(0,)
        pl.xlim(0,)
        pl.legend()
        pl.xlabel('x ($km$)')
        pl.ylabel('y ($km$)')
        pl.show()
a=cannon_shell()
a.pre_run_test()
a.accurate()
a.run()
a.show_result()
```
[代码链接](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/exercise06.py)
##运行结果
---
![](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/ex6_1.png)
![](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/ex6_2.png)
##反思
---
* 计算耗时过长，其中使用da扫描的部分可以拆分成多线程同时计算（然而不会）
* 其实没有弄懂在考虑初始值有误差的条件下怎样算打得准。根据误差分析当模型固定后结果的误差范围与各参数的误差范围应有确定函数关系（如果没记错的话）

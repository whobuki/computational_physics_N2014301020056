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
        self.b_m=b_m*1.0
        self.ture_x=[]
        self.ture_y=[]
        self.rand_x=[]
        self.rand_y=[]
        self.dxdy=accuracy*1.0

    def pre_run_test(self):
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
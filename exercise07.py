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
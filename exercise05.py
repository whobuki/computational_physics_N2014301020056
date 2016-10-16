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
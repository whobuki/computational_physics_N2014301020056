# Exercise_03
#### 邹志远 2014301020056
---
##作业内容
#####让名字在屏幕上动起来
##思路
#####使用for/break循环指令来在print的内容前插入空格，空格数量由range()控制。使用time.sleep来挂起进程来控制名字移动速度，并使用os.system调用cls清屏从而使图像连贯
##代码
---
![代码截图](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/code_image_03.png)
---
[代码](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/exercise_03.py)

    print('Please input the distance and speed for my name moving')
    a=int(input('distance(recommend 60):'))
    v=input('speed(recommend 10):')
    b=float(1)/v
    for i in range(a):
        print (i*' '+'#######    #######    #     #')
        print (i*' '+'     #          #      #   #')
        print (i*' '+'    #          #        # #')
        print (i*' '+'   #          #          #')
        print (i*' '+'  #          #           #')
        print (i*' '+' #          #            #')
        print (i*' '+'#######    #######       #')
        if i==a-1:
            break
        import time
        time.sleep(b)
        import os
        i=os.system('cls')
---
![运行结果截图](https://github.com/whobuki/computational_physics_N2014301020056/blob/master/result_03.gif)

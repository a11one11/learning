#import as方式
import time as x #导入time模块并且为其重新命名x
s =x.ctime() #调用time模块中的ctime函数，得到当前的时间
print(s)  #将时间输出

#from import方式导入
from time import ctime #导入模块time 中的ctime函数
s =ctime()#直接调用函数
print(s)
#注意此方法因为只导入ctime函数，使用其他的就会系统报错


#from import*，将模块中的所有名字导入当前的模块符号表里面
from time import *#导入模块time中的所有名字
s = ctime()#直接调用函数
print(s)
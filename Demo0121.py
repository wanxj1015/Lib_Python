#-*-coding:UTF-8-*-
import math

'''
	一、函数定义
	    1、格式
	    2、返回值
	    3、入参
	    （1）固定参数
	    （2）默认参数
	    （3）可变参数
	    （4）关键字参数
	    （5）命名关键字参数
'''
def Repid_var(Name,Age):
	print("%s" % Name)
	print("%d" % Age)
	
def Varible_var1(ListInput):
	for var in ListInput:
		print("%s" % var)

def Varible_var2(origin,*data):
	Sum = origin
	for var in data:
		Sum = Sum + var
	print("Sum = %d" % Sum)

''' 注意：默认值不能取变量，需要取定值，大坑'''	
def Default_var(name,age,addr="ZTE",ID=12):
	#print("Name=%s,age=%d,addr=%s,ID=%d" % name,age,addr,ID);
	print("Sum = %s" % name)
	print("Sum = %d" % age)
	print("Sum = %s" % addr)
	print("Sum = %d" % ID)

'''
关键词参数与默认参数的区别在于，其可以传入一个dict，也就是XXX=XXX的形式
data是个dict的形式
'''
def KeyWord_var(name,age,**data):
	print('Name:',name,'Age:',age,'Others:',data)

'''
关键词参数与默认参数的区别在于，其可以传入一个dict，也就是XXX=XXX的形式
data是个dict的形式,其有两种表示形式 fun(name,age,*,addr) fun(name,*age,addr,id)
*后面的以及*age
'''	

def NamedKeyWord_var1(sum,*data,addr):
	sum = 0
	for var in data:
		sum = sum + var
	print('sum',sum,'others:',addr)	

def NamedKeyWord_var2(name,age,*,addr):
	print('Name',name,'age:',age,'others:',addr)	


	Repid_var('wanxinjie',28)
Varible_var1(['wanxinjie','xuanjie','lengfang'])
Varible_var2(10,1,2,3,4,5)
Default_var('wanxinjie',12)
Default_var('wanxinjie',12,'huawei')
KeyWord_var('wanxinjie',23,addr='zte',ID=12)
NamedKeyWord_var1('10',1,2,3,3,4,5,6,addr='zte')
NamedKeyWord_var2('wanxinjie',28,addr='zte')

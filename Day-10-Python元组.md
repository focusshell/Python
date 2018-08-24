---
title: Day-10-Python元组
date: 2018-08-23 14:37:12
tags: Python
top: 13
---

# Python 元组 #

&emsp;Python的元组与列表类似，不同之处在于元组的元素不能修改。
&emsp;元组使用小括号，列表使用方括号。
&emsp;元组创建很简单，只需要在括号中添加元素用，并使用逗号隔开即可；

``` python
>>> tup1 = ('Google','Runoob',1997,2000);
>>> tup2 = (1,2,3,4,5);
>>> tup3 = "a","b","c","d";
>>> type(tup3)
<class 'tuple'>
>>>
```

&emsp;创建空元组

``` python
tup1 = ( );
```

&emsp;元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当做运算符使用；

``` python
>>> tup2 = (34);            # 不加逗号，类型为整型
>>> type(tup2)
<class 'int'>


>>> tup4 = (199,);          # 加上逗号，类型为元组
>>> type(tup4)
<class 'tuple'>
>>>
```

&emsp;元组与支付穿类似，下标索引从0开始，可以进行截取，组合等；

# 访问元组 #

&emsp;元组可以使用下标索引来访问元祖中的值，如下示例：

``` python
#!/usr/bin/python3

tup1 = ('Baduy','Rybiiv',1997.2018)
tup2 = (1,2,3,4,5,6)


print("tup1[0]:",tup1[0])
print("tup2[1:5]:",tup2[1:5])
```

&emsp;以上代码执行结果为：

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/元组.py"
tup1[0]: Baduy
tup2[1:5]: (2, 3, 4, 5)
```

# 修改元组 #

&emsp;元祖中的元素值是不允许修改的，但我们可以对元组进行连接组合，例如：

``` python
#!/usr/bin/python3

tup1 = (12,32.45);
tup2 = ('abc','xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组

tup3 = tup1 + tup2
print(tup3)
```

&emsp;以上代码执行结果：

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/修改元组.py"
(12, 32.45, 'abc', 'xyz')
```

# 删除元组 #

&emsp;元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下：

``` python
#! /usr/bin/python3

tup = ('Baudy','Runoob',1997,2018);

print(tup)
del tup;
print("删除后的元组 tup ：")
print(tup)
```

&emsp;以上实例元组被删除后，输出变量会有异常信息，如下：

``` python
删除后的元组 tup ：
  File "D:/Pycharm job/删除元组.py", line 8, in <module>
    print(tup)
NameError: name 'tup' is not defined
```

# 元组运算符 #

&emsp;与字符串一样，元组之间可以使用+号和*号进行运算，这就意味着他们可以组合和复制，运算后会生成一个新的元组：

|       Python表达式         |             结果            |               描述             |
|---------------------------|:--------------------------:|-------------------------------:|
|len(1.2.3)                 |3                           |计算元素个数                     |
|(1.2.3)+(4.5.6)            |(1.2.3.4.5.6)               |连接                             |
|('Hil'.)*4                 |('Hil','Hil','Hil'.'Hil')   |复制                             |
|3 in (1.2.3)               |True                        |元素是否存在                      |
|for x in (1.2.3) print(x.) |1 2 3                       |迭代                             |

# 元组索引，截取 #

&emsp;因为元组也是一个序列，所以我们可以访问元组中的指定为位置的元素，也可以截取索引中的一段元素，如下：

&emsp;元组：

``` python
L = ('Baidu','Runoob',1997,2018);
```

| Python表达式 |               结果           |              描述             |
|-------------|:----------------------------:|------------------------------:|
|L[2]         |'1997'                        |读取第三个元素                  |
|L[-2]        |'1997'                        |反向读取；读取倒数第二个元素      |
|L[1:]        |('Runoob', 1997, 2018)        |截取元素，从第二个开始后的所有元素|

&emsp;实例运行如下：

``` python
>>> L = ('Baidu','Runoob',1997,2018)
>>> print (L[2])
1997
>>> print (L[-2])
1997
>>> print (L[1:])
('Runoob', 1997, 2018)
>>>
```

# 元组内置函数 #

&emsp;Python元组包含了以下内置函数

## len(tuple) ##

&emsp;计算元组元素个数：
&emsp;__实例：__

``` python
>>> tup1 = ('Baidu','Runoob',1997,2018);
>>> len(tup1)
4
>>>
```

## max(tuple) ##

&emsp;返回元组中元素的最大值：
&emsp;__实例：__

``` python
>>> tup2 = ('19','222','3333')
>>> max(tup2)
'3333'
>>>
```

## min(tuple) #

&emsp;返回元组中元素最小值
&emsp;__实例：__

``` python
>>> tup2 = ('19','222','3333')
>>> min(tup2)
'19'
>>>
```

## tuple(seq) ##

&emsp;将列表转换为元组
&emsp;__实例：__

``` python
>>> list1 = ('Baidu','Tudou','Runoob','souhu')
>>> tuple1=tuple(list1)
>>> tuple1
('Baidu', 'Tudou', 'Runoob', 'souhu')
>>>
```

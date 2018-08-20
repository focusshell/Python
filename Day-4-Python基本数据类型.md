---
title: Day-4-Python基本数据类型
date: 2018-08-16 11:11:13
tags: Python
top: 6
---

## Python3的基本数据类型 ##

### 数据类型 ###

&emsp;计算机顾名思义就是可以做数学计算的机器，因此，计算机程序理所当然地可以处理各种数值。但是计算机能处理的远不止数值，还可以处理文本、图形、音频、视频、网页等各种各样的数据，不同的数据，需要定义不同的数据类型。在Python中，能够直接处理的数据类型有以下几种：

__整数:__
&emsp;Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一摸一样，例如：

``` python
1,100,-8080,0.等等
```

&emsp;计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0X前缀和0-9，a-f表示，例如：

``` python
0xff00,0xa5b4c3d2,等等
```

***

__浮点数:__
&emsp;浮点数也就是小数，之所以称为浮点数，是因为按照科学计数法表示时，一个浮点数的小数点位置是可变的，比如：浮点数可以用数学写法，如1.23，3.14,-9.01，等等。但是对很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，就是1.23e9，或者12.3e8,0.000012可以写成1.2e-5，等等；
&emsp;证书和浮点数在计算机内部存储的方式是不同的，整数计算永远是精确的（除法难道也是精确的？是的），而浮点数运算则可能会有四舍五入的误差。
***
__字符串:__
字符串是以单引号'或双引号"括起来的任意文本，比如：'abc',"xyz"等等。请注意，''或""本身只是一种表示方法，不是字符串的一部分，因此，字符串'abc'只有a,b,c这3个字符。如果'本身也是一个字符，那久可以""括起来，比"I`m ok”包含的字符就是I,',m,空格,o,k这6个字符。


&emsp;如果字符串内部既包含'又包含"怎么办？可以用转义符\来标识，比如：
__实例：__

``` python
'I\'m \"ok\"!'
```

&emsp;表示字符串内容是：

``` python
I'm "ok"!
```

&emsp;转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\，可以Python的交互式命令用print()打印字符串看看:

``` python
>>> print('I\'m ok ')
I'm ok
>>> print('I\'m learning\nPython')
I'm learning
Python
>>> print('\\\n\\')
\
\
>>>
```

如果字符串里面有很多字符都要转义，就需要加很多\,为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以试试：

``` python
>>> print('\\\n\\')
\
\
>>>
```

&emsp;如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容，可以试试：

``` python
>>> print('''line1
... line2
... line3
... line4''')    #  注意在line1后面不要加)，不然打印之后会显示出line1）
line1
line2
line3
line4
>>>
```


&emsp;Python中的数据变量不需要声明，每个变量都在使用前都必须赋值，变量赋值以后该变量才会被创建；
&emsp;在Python中，变量就是变量，他没有类型，我们所说的 __“类型”__ 是变量说指的内存中的对象的类型；
&emsp;等号 __(=)__ 用来给变量赋值;
&emsp;等号 __(=)__ 运算符左边是一个变量号，等号(=)运算符右边是存储在变量中的值，例如：

__实例：__

``` python
#!/bin/bash/python3


counter = 100     # 整型变量
miles = 1000.0    # 浮点型变量
name = "runoob"   # 字符串

print(counter)
print(miles)
print(name)
```

&emsp;执行上述代码会输出如下结果：

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/数据类型.py"
100
1000.0
runoob

Process finished with exit code 0
```

***

## 多个变量赋值 ##

&emsp;Python允许你同时为多个变量赋值。例如：

``` python
a = b =c = 1
```

&emsp;以上实例，创建一个整型对象，值为1，从后向前赋值，三个变量都指向同一个内存地址。您也可以为多个对象指定多个变量。例如：
__实例：__

``` python
a,b,c = 1,2,"runoob"
```

&emsp;以上实例，连个整型对象1和2的分配给变量a和b，字符串对象"runoob"分配给对象c。
***

## 标准数据类型 ##

&emsp;Python中有六个标准的数据类型：

>1. Number(数字)
>2. String(字符串)
>3. List(列表)
>4. Tuple(元组)
>5. Set(集合)
>6. Dictionart(字典)

&emsp;Python3中的六个标准数据类型中：

__不可变数据(3个)__：Number（数字）、String(字符串)、Tuple(元组)；
__可变数据(3个)__：List(列表)、Dictionary(字段)、Set（集合）；

### Number(数字) ###

&emsp;Python3支持int、float、bool、complex(复数)。
&emsp;在Python3里，只有一种整数类型int，表示为长整型，没有Python2中的Long；
&emsp;像大多数语言一样，数值类型的复制和计算都是很直观的；
&emsp;内置的type()函数可以用来查询变量所指的对象类型。

``` python
>>> a,b,c,d = 20,5.5,True,4+3j
>>> print(type(a),type(b),type(c),type(d))
<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
>>>
```

&emsp;此处还可以用isinstance来判断：
__实例：__

``` python
>>> a,b,c,d = 20,5.5,True,4+3j
>>> print(type(a),type(b),type(c),type(d))
<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
>>>
```

&emsp;isinstance和type的区别在于：

``` python
class A:
    pass

class B(A):
    pass

isinstance(A( ), A)    # returns True
type(A( )) == A        # returns True
isinstance(B( ), A)    # returns True
type(B( )) == A        # returns False
```

***

__区别就是：__

>1. type()不会认为子类是一种父类类型。
>2. isintance()会认为子类是一种父类类型。

``` shell
注意：在Python2中是没用布尔型的，他用数字0表示False，用1表示True。到Python3中，吧True和False定义成关键字了，但他们的值还是1和0，他们可以和数字相加
```

``` python
var1 = 1
var2 = 10
```

&emsp;也可以使用del语句删除一些对象引用；
del语句的语法是：

``` python
del var1[,var2[,var3[.....,varN]]]
```

&emsp;也可用通过使用del语句删除单个或多个对象 例如：

``` python
del var
del var_a,var_b
```

***

### 数值运算 ###

&emsp;数值运算在Python中的使用及其方便；
__实例：__

``` python
>>> 5+4                         # 加法
9
>>> 4.3-2                       # 减法
2.3
>>> 3*47                        # 乘法
141
>>> 2/45                        # 除法，得到一个浮点数
0.044444444444444446
>>> 2//4                        # 除法，得到一个整数
0
>>> 2//4                        # 除法，得到一个整数
0
>>> 2//6                        # 除法，得到一个整数
0
>>> 17 % 3                      # 取余
2
>>> 2 ** 5                      # 乘方
32
>>>
```

__注意：__

>1. Python可以同时为多个变量赋值，如a,b = 1,2.
>2. 一个变量可以通过赋值指向不同类型的对象。
>3. 数值的除法包含两个运算符：/返回一个浮点数，//返回一个整数；
>4. 在混合计算时，Python会吧整型转换成为浮点数，

***

### 数值类型实例 ###

|int      |float     |cpmplex   |
|---------|:--------:|---------:|
|10       |0.0       |3.14j     |
|100      |15.20     |45.j      | 
|-756     |-21.9     |9.322e-36j|
|080      |32.3e+18  |.876j     |
|-0490    |-90       |-.6545+0J |
|-0x260   |-32.54e100|3e+36J    |
|0x69     |70.2E-12  |4.53e-7j  |
&emsp;Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj，或者complex(a,b)表示，复数的实部a和虚部b都是浮点型；
***

### String(字符串) ###

&emsp;Python中的字符串用单引号'或双引号"括起来，同时使用反斜杠\转义特殊字符
&emsp;字符串的截取的语法格式如下：

``` python
变量[头下标:尾下标]
```

&emsp;索引值以0开始的值，-1为从末尾的开始位置

``` python
从后面索引：          -6 -5 -4 -3 -2 -1
从前面缩影：           0  1  2  3  4  5
                     +---+---+---+---+---+---+
                     | a | b | c | d | e | f |
从前面截取：          :   1   2   3   4   5   :
从后面截取：          :  -5  -4  -3  -2  -1   :
```

&emsp;加号+是字符串的连接符，型号*表示复制当前字符串，紧跟的数字为复制的次数。实例如下：
__实例：__

``` python
#!/bin/bash/python3

str = 'Runoob'

print(str)           # 输出字符串
print(str[0:-1])     # 输出第一个到倒数第二个的所有字符
print(str[0])        # 输出字符串第一个字符
print(str[2:5])      # 输出第三个开始到第五个的字符
print(str[2:])       # 输出第三个开始的后的所有字符
print(str * 2)       # 输出字符串两次
print(str + "Test")  # 连接字符串

input("\n\n按下 enter 键后退出。")
```

&emsp;执行上述代码会输出如下结果：

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/等待用户输入.py"
Runoob
Runoo
R
noo
noob
RunoobRunoob
RunoobTest


按下 enter 键后退出。
```

&emsp;Python是用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以子字符串前面添加一个r，表示原始字符串:

``` python
>>> print('Ru\nnoob')
Ru
noob
>>> print(r'Ru\nnoob')
Ru\nnoob
>>>
```

&emsp;另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续，也可以使用 """..."""或者'''...'''跨越多行。
&emsp;注意，Python没有单独的字符类型，一个字符就是长度为1的字符串，
__实例：__

``` python
>>> word = 'Python'
>>> print(word[0],word[4])
P o
>>> print(word[-1],word[-6])
n P
>>>
```

&emsp;与C字符串不同的是，Python字符串不能被改变，向一个索引位置赋值，比如 __worid[0] = 'm'__ 会导致错误。
__注意：__

>1. 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
>2. 字符串可以用+运算符连接在一起，用*运算符表示重复。
>3. Python中的字符串有两宗索引方式，从左往右以0开始，从右往左以-1开始。
>4. Python中的字符串不能改变。
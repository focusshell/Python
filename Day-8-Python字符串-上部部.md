---
title: Day-8-Python字符串(上部部)
date: 2018-08-21 15:05:32
tags: Python
top: 12
---

# Python3 字符串 #

&emsp;字符串是Python中最常用的数据类型，我们可以使用引号('或")来创建字符串，
&emsp;创建字符串很简单，只要为变量分配一个值即可。
&emsp;__实例：__

``` python
>>> var1 = 'Hello blackchain'
>>> var2 = 'Blcakchain'
>>> var1
'Hello blackchain'
>>> var2
'Blcakchain'
>>>
```

# Python 访问字符串中的值 #

&emsp;Python不支持单字符类型，单字符在Python中也是作为一个字符串使用。
&emsp;Python访问字符串，可以使用方括号来截取字符串，如下：

``` python
#!/usr/bin/python3

var1 = 'Hello blackchain'
var2 = 'Blcakchain'

print("var1[0]:",var1[0])
print("var2[2:5]:",var2[1:5])
```

&emsp;以上代码执行的结果：

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/字符串的值.py"
var1[0]: H
var2[2:5]: lcak
```

# Python字符串更新 # 

&emsp;你可以截取字符串的一部分并与其它字段拼接，如下：
&emsp;__实例：__

``` python
#!/usr/bin/python3

var1 = 'Hello python word'

print("已更新字符串：", var1[:6] + 'Runoob!')
```

&emsp;以上实例执行结果：

``` python 
已更新字符串：Hello Runoob！
```

# Python转义字符 #

&emsp;在需要的字符中使用特殊字符，python用反斜杠(\)转义字符，如下表：
![转义](/img/python/zhuan.jpg)

# Python字符串运算符 #

&emsp;下面实例变量a值为字符串“Hello”，b变量值为“Python”
![字符串](/img/python/zifu.jpg)

&emsp;__实例：__

``` python
#!/usr/bin/python3

a = "Hello"
b = "Python"

print("a + b 输出的结果为：",a + b)
print("a * 2 输出的结果为：",a * 2)
print("a[1] 输出结果为：",a[1])
print("a[1:4] 输出结果为：",a[1:4])

if ("H" in a ):
    print("H 在变量a中")
else:
    print("H 不再变量a中")

if ("M" not in a ):
    print("M 不再变量a中")
else:
    print("M 在变量a中")

print(r'\n')
print(R'\n')
```

&emsp;以上代码输出结果为：

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/字符串运算符.py"
a + b 输出的结果为： HelloPython
a * 2 输出的结果为： HelloHello
a[1] 输出结果为： e
a[1:4] 输出结果为： ell
H 在变量a中
M 不再变量a中
\n
\n
```

# Python字符串格式化 #

&emsp;Python支持格式化字符串的输出，尽管这样可能会用到非常复杂的表达式，但最基本的用法试讲一个值插入到一个有字符串%s的字符串中；
&emsp;在Pytthon中，字符串格式化使用C中sprintf函数一样的语法；
&emsp;__举个栗子：__

```python
#!/usr/bin/python3

print("我叫%s 今年 %d 岁!" % ( '小铭',10))
```

&emsp;以上实例输出结果：

``` shell
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/字符串格式化.py"
我叫小铭 今年 10 岁!
```

&emsp;Python字符串格式化符号：
![字符串格式化](/img/python/)
&emsp;格式化操作符辅助命令：
![辅助](/img/python)


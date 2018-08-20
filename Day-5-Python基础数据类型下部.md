---
title: Day-5-Python基础数据类型下部
date: 2018-08-17 15:28:32
tags: Python
top: 7
---

# Python基础数据类型下部 #

&emsp;前面我们主要了解了，Python六个标准数据类型中的 __不可变数据__ Number、String、Tuple;接下来我们学习后面三个标准数据类型，__可变数据__ List、Dictionary、Set;

## List (列表) ##

&emsp;List（列表）是Python中使用最频繁的数据类型。
&emsp;列表可以完成大多数集合类的数据结构实现，列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
&emsp;列表是写在方括号[]之间、用逗号分隔开的元素列表；
&emsp;和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的心列表。
&emsp;列表截取的语法格式如下:

``` python
变量[头下标:尾下标]
```

&emsp;索引值以0为开始值，-1位从末尾的开始位置
![列表截取]{/img/python/liebiao.jpg}
&emsp;加号+是列表连接运算符，星号*是重复操作。如下实例：

``` python
#!/bin/bash/python3

list = [ 'abcd', 786 , 2.23 , 'runoob' , 70.2 ]
tinylist = [123, 'runoob']

print(list)                # 输出完整列表
print(list[0])             # 输出完整列表第一个元素
print(list[1:3])           # 从第二个开始输出到第三个元素
print(list[2:])            # 输出从第三个元素开始的所有元素
print(tinylist * 2)        # 输出两次列表
print(list + tinylist)     # 连接列表
```

&emsp;以上代码输出结果：

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/列表截取.py"
['abcd', 786, 2.23, 'runoob', 70.2]
abcd
[786, 2.23]
[2.23, 'runoob', 70.2]
[123, 'runoob', 123, 'runoob']
['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob']
```

&emsp;与Python字符串不一样的是，列表中的元素是可以改变的：
&emsp;__实例：__

``` python
>>> a = [1,2,3,4,5,6]
>>> a[0] = 9
>>> a[2:5] = [13,14,15]
>>> a
[9, 2, 13, 14, 15, 6]
>>> a[2:5] = []   # 将对应的元素值设置为[]
>>> a
[9, 2, 6]
>>>
```

&emsp;List内置有很多方法，例如append()、pop()等等，这在后面会有讲述。
&emsp;__注意：__

>1. List卸载方括号之间，元素用逗号隔开；
>2. 和字符串一样，list可以被索引和切片。
>3. List可以使用+操作符进行拼接。
>4. List中的元素是可以改变的。

***

## Set（集合） ##

&emsp;集合（set）是一个无序不重复的元素的序列。
&emsp;基本功能是进行成员关系测试和删除重复元素。
&emsp;可以使用大括号｛｝或者set（）函数创建集合，注意：创建一个空集合必须用set（）而不是｛｝，因为｛｝是用来创建一个空字典的。
&emsp;__创建格式：__

``` python
#!/bin/bash/python3

parname = {value01,value02,....}
# 或者
set(value)
```

&emsp;__实例：__

``` python
#!/bin/bash/ppython3

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试

if 'Rose' in student :
    print('Rose在集合中')
else :
    print('Rose 不在集合中')

# set 可以进行集合运算

a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)    # a和b的差集

print(a | b)    # a和b的并集

print(a & b)    # a和b的交集

print(a ^ b)    # a和b中不同的时序存在的元素
```

&emsp;上述代码输出结果：

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/set集合.py"
{'Tom', 'Jim', 'Mary', 'Jack', 'Rose'}
Rose在集合中
{'d', 'b', 'a', 'c', 'r'}
{'d', 'b', 'r'}
{'d', 'c', 'z', 'l', 'b', 'a', 'm', 'r'}
{'c', 'a'}
{'d', 'z', 'l', 'm', 'b', 'r'}
```

***

## Dictionary (字典) ##

&emsp;字典（Dictionary）是Python中另一个非常有用的内置数据类型。
&emsp;列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：__字典当中的元素是通过键来存取的，而不是通过偏移存取。
&emsp;字典是一种映射类型，字典"{}"标识，他是一个无序的键(key)：值(value)对组合。
&emsp;键（Key）必须使用不可变类型，
&emsp;在同一字典中，键（key）必须是唯一的。
&emsp;__实例：__

``` python
#!/bin/bash/python3

dict = { }
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = { 'name': 'runoob','code':1, 'site': 'www.focusshell.com' }

print(dict[ 'one' ])       # 输出键为‘one’的值
print(dict[2])             # 输出键为2的值
print(tinydict)            # 输出完整的字典
print(tinydict.keys())     # 输出所有键
print(tinydict.values())   # 输出所有值
```

&emsp;以上代码输出结果：

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/字典.py"
1 - 菜鸟教程
2 - 菜鸟工具
{'site': 'www.focusshell.com', 'code': 1, 'name': 'runoob'}
dict_keys(['site', 'code', 'name'])
dict_values(['www.focusshell.com', 1, 'runoob'])
```

&emsp;构造函数dict()可以直接键值对序列中构建字典如下：
&emsp;__实例：__

``` python
>>>dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
{'Taobao': 3, 'Runoob': 1, 'Google': 2}
 
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
 
>>> dict(Runoob=1, Google=2, Taobao=3)
{'Taobao': 3, 'Runoob': 1, 'Google': 2}
```

&emsp;另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。
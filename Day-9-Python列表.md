---
title: Day-9-Python列表
date: 2018-08-22 11:52:21
tags: Python
top: 13
---

# Python列表 #

&emsp;序列是Python中最基本的数据结构，序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，以此类推。
&emsp;Python有6哥序列的内置类型，但最常见的是列表和元组。
&emsp;序列都可以进行的操作包括索引，切片，加，乘，检查成员；
&emsp;此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
&emsp;列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
&emsp;列表的数据项不需要具有相同的类型；
&emsp;创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下：

``` python
list1 = ['Google','Runoob',1997,2000];
list2 = [1,2,3,4,5 ];
list3 = ["a","b","c","d"];
```

&emsp;与字符的索引一样，列表索引聪0开始，列表可以进行截取、组合等；

## 访问列表中的值 ##

&emsp;使用下标索引来访问列表中的值，统一你也可以使用方括号的形态截取字符，如下：

``` python
#!/usr/bin/python

list1 = ['Google','Runoob',1997,2000];
list2 = [1,2,3,4,5 ];
list3 = ["a","b","c","d"];

print(list1)
print(list2)
print(list3)
```

&emsp;以上代码输出结果：

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/Python列表.py"
['Google', 'Runoob', 1997, 2000]
[1, 2, 3, 4, 5]
['a', 'b', 'c', 'd']
```

## 更新列表 ## 

&emsp;你可以对列表的数据项进行修改或更新，你也可以是使用append（）方法来添加列表项，如下：

``` python
#!/usr/bin/python

list = ['Google','Runoob',1997,2000]

print ("第三个元素为 : ", list[2])
list[2] = 2018
print("更新后的第三个元素为:",list[2])
```

&emsp;__注意：__ 我们会在接下来额的章节中讨论append()方法的使用，
&emsp;以上代码的执行结果

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/更新列表.py"
第三个元素为 :  1997
更新后的第三个元素为: 2018
第三个元素为 :  1997
更新后的第三个元素为 :  2001
```

## 删除列表元素 ##

&emsp;可以使用del语句来删除列表的元素；如下：

``` python
#!/usr/bin/python

list = ['Google','Runoob',1991,2018]

print("原始列表：",list)
del list[2]
print("删除第三个元素：",list)
```

&emsp;以上代码执行结果

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/删除元素.py"
原始列表： ['Google', 'Runoob', 1991, 2018]
删除第三个元素： ['Google', 'Runoob', 2018]
```

&emsp;__注意：__ 我们在接下来的章节中讨论remover()方法的使用：

# Python列表脚本操作符 #

&emsp;列表+和*的操作符与字符串相似，+号用于组合列表，*号用于重复列表
&emsp;如下所示：

|           Python表达式           |          结果            |            描述            |
|---------------------------------|:-----------------------:|----------------------------:|
|len{[1,2,3]}                     |3                        |长度                         |
|[1,2,3]+[4.5.6]                  |[1,2,3,4,5,6]            |组合                         |  
|['Hi!']*4                        |['Hi!','Hi!','Hi!','Hi!']|重复                         |
|3 in [1,2,3]                     |True                     |元素是否存在于列表中           |
|for x in [1,2,3]:print(x,end="") |1 2 3                    |迭代                         |

# Python列表截取于拼接 #

&emsp;Python的列表截取于字符串操作类型，如下：

``` python
L = ['Google','Runoob','Taobao']
```

&emsp;操作：

|Python表达式|      结 果          |                    描述                      |
|-----------|:-------------------:|---------------------------------------------:|
|L[2]       |'Taobao'             |读取第三个元素                                  |
|L[-2]      |'Runoob'             |从右侧开始读取倒数第二个元素:countfron the right |
|L[1:]      |['Runoob','Tbaobao'] |输出从第二个元素开始后的所有元素                  |

``` python
>>> L = ['Google','Runoob','Taobao']
>>> L[2]
'Taobao'
>>> L[-2]
'Runoob'
>>> L[1:]
['Runoob', 'Taobao']
>>>
```

&emsp;列表还支持拼接操作：

``` python
>>> squares = [1,4,9,16,25]
>>> squares += [36,49,64,81,100]
>>> squares
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>>
```

# 嵌套列表 #

&emsp;使用嵌套列表即在列表里创建其他列表，例如：

``` python
>>> a = ['a','b','c']
>>> n = [1,2,3]
>>> x = [a,n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
>>>
```

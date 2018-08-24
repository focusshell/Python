---
title: Day-10-Python字典
date: 2018-08-24 16:46:38
tags: Python
top: 14
---

# Python字典 #

&emsp;字典是另一种可变容器模型，且可存储任意类型对象。
&emsp;字典的每个键值（Key=>value）对用冒号(:)分解，每个队之间用逗号(,)分割，整个字典包括在花括号({})中，格式如下：

``` python
d = {key1 : value1.key2 : value2 }
```

&emsp;键必须是唯一的，但值则不必；
&emsp;值可以取任何数据类型，但键必须是不可变得，如字符串，数字或元组；
&emsp;一个简单的字典例子：

``` python
dict = {'Alice': '2341', 'Bath': '9102','Cecil': '3258'}
```

&emsp;也可以如此创建字典：

``` python
dict1 = {'abc': 456 };
dict2 = {'abc': 123,98.5: 32 };
```

# 访问字典里的值 #

&emsp;把响应的键放入到方括号中，如下：

``` python
#!/usr/bin/python3

dict = {'Name': 'Runoob', 'Age':5, 'class':'First'}

print("dict{'Name'}:",dict['Name'] )
print("dict[''Age]:",dict['Age'])
```

&emsp;上述代码执行的结果

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/访问字典里的值.py"
dict{'Name'}: Runoob
dict[''Age]: 5
```

&emsp;如果用字典里没有键的访问数据，会输出错误如下：

``` python
# 错误示范

dict = {'Name':'Runoob','Age':6,'ckass': 'first'}

print("dict[Alice]:",dict['Alice'])

```

&emsp;以上代码输出结果：

``` python
Traceback (most recent call last):
dict[''Age]: 5
  File "D:/Pycharm job/访问字典里的值.py", line 13, in <module>
    print("dict[Alice]:",dict['Alice'])
KeyError: 'Alice'
```

# 修改字典 #


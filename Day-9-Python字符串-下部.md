---
title: Day-9-Python字符串-下部
date: 2018-08-22 10:24:32
tags: Python
top: 12
---

# Python三引号 #

&emsp;Python三引号允许一个字符串跨多行，字符串中也可以包含换行符、制表符以及其他特殊字符。
&emsp;__实例：__

``` python
#!/usr/bin/python3

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB(\t)
也可以使用换行符[ \n ]
"""
print(para_str)
```

&emsp;以上代码执行结果为：

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/三引号.py"
这是一个多行字符串的实例
多行字符串可以使用制表符
TAB(	)
也可以使用换行符[ 
 ]
```

&emsp;三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG(所见即所谓)格式的。
&emsp;一个典型的用例是，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐

``` HTML
errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
cursor.execute('''
CREATE TABLE users (  
login VARCHAR(8), 
uid INTEGER,
prid INTEGER)
''')
```

# Unicode 字符串 #

&emsp;在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀u。
&emsp;在Python3中，所有的字符串都是Unicode字符串；
***


---
title: Day-3-Python基础语法.md
date: 2018-08-15 11:42:53
tags: Python
---

## 编码 ##

&emsp;默认情况下，Python3源码文件有以UTF-8编码，所有字符串都是unicode字符串。当然你也可以为源码文件指定不同的编码：

``` python
# -*- coding: cp-1252 -*-
```

&emsp;上述定义允许在原文件中使用Windows-1252字符集中的支付编码，对应适合语言为保加利亚语、白俄罗斯语、马其顿语、俄语、塞尔威亚语。
***

***

## 标识符 ##

``` python
第一个支付必须是字母表中字母或下划线_
标识符的其他的部分由字母、数字和下划线组成。
标识符对大小写敏感
```
&emsp;在Python3 中，非ASCII标识符也是允许的了。
***

## Python保留字 ##

&emsp;保留字即关键字，我们不能把它们用做任何标识符名称。Python的标准库提供了一个Keyword模块，可是输出当前的所有关键字：

``` python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>>
```
***

***

## 注释 ##

&emsp;Python中单行注释以 __#__ 开头，
&emsp;__实例:__

``` python
#!/bin/bin/python3

# 第一个注释
print("Hello Python") # 第二个注释
```

&emsp;执行上述代码，输出结果为：

``` python
Hello Python
```

多行实例可以用多个 __#__,还有 __'''__ 和 __"""__ ;
&emsp;__实例:__

``` python
#!/bin/bash/python3

# 第一个注释
# 第二个注释

'''
第三个注释
第四个注释
'''

"""
第五个注释
第六个注释
"""
print("Hello python")
```

&emsp;执行上述代码，输出结果为：

``` python
Hello word
```

***

## 行与缩进 ##

&emsp;Python最具有特色的就是使用缩进来表示代码块，不需要使用大括号{};
&emsp;缩进的空格数是可变的，但是同一个代码快的语句必须包含相同的缩进空格数。实例如下：
&emsp;__实例：__

``` python
if True:
    print("True")
else
    print("False")
```

&emsp;以下代码最后一行语句说金属的空格数不一致，会导致运行错误：

``` python
if True:
    print("True")
else
    print("False")
   print("Anser") # 缩进不一致，空格数不一样；会导致运行错误；
```

&emsp;以上程序由于缩进不一致，执行后会出现类似以下错误：

``` python
File "test.py",line 6
    print("False") # 缩进不一致，会导致运行错误；
                                  ^
IndentationError: unindent does not match any outer indentation level
```

***

## 多行语句 ##

&emsp;Python通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 __(\)__ 来实现多行语句。例如：

``` python
total = item_one + \
        item_two + \
        item_three
```

&emsp;在[]、{}、或()中的多行语句，不需要使用反斜杠(\),例如：

``` python
total = ['item_one','item_two', 'item_three',
        'item_four','item_five']
```

***

## 数字（Nember）类型 ##

&emsp;Python中数字有四种类型：整数、布尔型、浮点数和复数。

``` python
int (整数)，如：1，只有一种整数类型int，表示为长整型，没有Python2中的Long；
bool(布尔)，如：True；
float(浮点数)，如：1.23、3E-2；
complex(复数)，如：1+2j、1.1+2.2j；
```

***

## 字符串 ##

>Python中单引号和双引号使用完全相同；
>三引号（""或""");可以指定一个多行字符串
>转义符'\'
>反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。如：r"this is al line with \n"则'\n' 会显示，并不是换行。
>按字面意义级联字符串，如"this""is""string"会被自动转换this is string。
>字符串可以用 + 运算符连接在一起，用 * 运算符重复；
>Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1 开始。
>Python中的字符串不能改变。
>Python没有单独的字符类型，一个字符的长度为1的字符串。
>字符串的截取的语法格式如下:变量[头下标:尾下标]

``` python
word = '字符串'
sentence = '这是一个句子'
paragraph = """这是一个段落
可以由多行组成"""
```

``` python
#!/bin/bash/python3

str='Runoob'
print(str)                  # 输出字符串
print(str[0:-1])            # 输出第一个到倒数第二个的所有字符
print(str[0])               # 输出字符串第一个字符
print(str[2:5])             # 输出从第三个开始到第五个的字符
print(str[2:])              # 输出从第三个开始的后的所有字符
print(str * 2)              # 输出字符串两次
print(str + '你好')         # 连接字符串

print('-----------------------------------')
print('hello\nrunoob')     # 使用反斜杠(\)+n 特殊字符
print(r'hello\nrunoob')    # 再字符串前面添加一个r，表示远视字符串，不会发生转义
```

&emsp;输出结果为：

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/学习.py"
Runoob
Runoo
R
noo
noob
RunoobRunoob
Runoob你好
-----------------------------------
hello
runoob
hello\nrunoob

Process finished with exit code 0
```
***

## 空行 ##

&emsp;函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
&emsp;空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同的功能或含义的代码，便于日后代码的维护或重构；
&emsp;__记住：__ 空行也是程序代码的一部分；
***

## 等待用户输入 ##

&emsp;执行下面的程序在按回车键后就会等待用户输入：

&emsp;__实例：__

``` python
#!/bin/bash/python3
input("\n\n按下 enter 键后退出。")
```

以上代码中，"\n\n"在结果输出前会输出两个新的空行。一旦用户按下enter键，程序将退出；
***

## 同一行显示多条语句 ##

&emsp;Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
&emsp;__实例：__

``` python
#!/bin/bash/python3
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
```

&emsp;使用脚本执行以上代码，输出结果为：

``` python
runoob
```

&emsp;使用交互式命令行执行，输出结果为：

``` python
>>> import sys; x = 'runoob'; sys.stdout.write(x + '\n')
runoob
7
>>>
```

***

## 多个语句构成代码组 ##

&emsp;缩进相同的一组语句构成一个代码块，我们称之代码组；
&emsp;像if、while、def和class这样的符合语句，首行以关键字开始，以冒号(:)结束，该行之后的一行或多行代码构成代码组。
&emsp;我们将首航及后面的代码组称之为一个子句(clause)。
&emsp;__如下实例：__

``` python
#!/bin/bash/python3
if expression :
    suite
elif expression :
    suite
else :
    suite
```

***

## Print 输出 ##

&emsp;print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 __end=""__
&emsp;__实例：__

``` python
#!/bin/bash/python3

x="a"
y="b"
# 换行输出
print(x)
print(y)

print('--------')
# 不换行输出
print( x,end="" )
print( y,end="" )
```

&emsp;以上实例执行结果为：

``` python
C:\Users\User\Anaconda3\python.exe "D:/Pycharm job/print输出.py"
a
b
--------
ab
```

***

## impot与from...import ##

&emsp;在Python用 __import__ 或者 __from...import__ 来到如响应的模块，
&emsp;将整个模块(somemodule)导入，格式为：__import somemodule__
&emsp;从某个模块中导入某个函数，格式为：__from somemodule import somefunction__
&emsp;从某个模块中导入多个函数，格式为：__from somemodule import firsfunc,secondfunc,thirdfunc__
&emsp;将某个模块中的全部函数导入，格式为：__from somemodule import *__

&emsp;__实例：__

&emsp;__导入sys模块__

``` python
mport sys
print('============python import mode============');
print('命令行参数为：')
for i in sys.argv:
    print(i)
print('\n python 路径为',sys.path)
```

&emsp;__导入sys模块的argv,path成员__

``` python
from sys import argv,path  # 导入特定的成员

print('============python from import ===========')
print('path:',path ) # 因为已经导入path成员，所以此处应用时不需要加sys，path
```

***

## 命令行参数 ##

&emsp;很多程序可以自行一些操作来查看一些基本信息，Python可以使用 __-h__ 参数查看各参数帮助信息：

&emsp;__实例：__

``` python
C:\Users\User>python -h
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):
-b     : issue warnings about str(bytes_instance), str(bytearray_instance)
         and comparing bytes/bytearray with str. (-bb: issue errors)
-B     : don't write .py[co] files on import; also PYTHONDONTWRITEBYTECODE=x
-c cmd : program passed in as string (terminates option list)
-d     : debug output from parser; also PYTHONDEBUG=x
-E     : ignore PYTHON* environment variables (such as PYTHONPATH)
-h     : print this help message and exit (also --help)
-i     : inspect interactively after running script; forces a prompt even
         if stdin does not appear to be a terminal; also PYTHONINSPECT=x
-I     : isolate Python from the user's environment (implies -E and -s)
-m mod : run library module as a script (terminates option list)
-O     : optimize generated bytecode slightly; also PYTHONOPTIMIZE=x
-OO    : remove doc-strings in addition to the -O optimizations
-q     : don't print version and copyright messages on interactive startup
-s     : don't add user site directory to sys.path; also PYTHONNOUSERSITE
-S     : don't imply 'import site' on initialization
-u     : unbuffered binary stdout and stderr, stdin always buffered;
         also PYTHONUNBUFFERED=x
         see man page for details on internal buffering relating to '-u'
-v     : verbose (trace import statements); also PYTHONVERBOSE=x
         can be supplied multiple times to increase verbosity
-V     : print the Python version number and exit (also --version)
-W arg : warning control; arg is action:message:category:module:lineno
         also PYTHONWARNINGS=arg
-x     : skip first line of source, allowing use of non-Unix forms of #!cmd
-X opt : set implementation-specific option
file   : program read from script file
-      : program read from stdin (default; interactive mode if a tty)
arg ...: arguments passed to program in sys.argv[1:]

Other environment variables:
PYTHONSTARTUP: file executed on interactive startup (no default)
PYTHONPATH   : ';'-separated list of directories prefixed to the
               default module search path.  The result is sys.path.
PYTHONHOME   : alternate <prefix> directory (or <prefix>;<exec_prefix>).
               The default module search path uses <prefix>\lib.
PYTHONCASEOK : ignore case in 'import' statements (Windows).
PYTHONIOENCODING: Encoding[:errors] used for stdin/stdout/stderr.
PYTHONFAULTHANDLER: dump the Python traceback on fatal errors.
PYTHONHASHSEED: if this variable is set to 'random', a random value is used
   to seed the hashes of str, bytes and datetime objects.  It can also be
   set to an integer in the range [0,4294967295] to get hash values with a
   predictable seed.
```

&emsp;我们在使用脚本形式执行python时，可以接受命令行输入的参数，具体使用可以参照<a href="https://www.python.org/">Python官网</a>;

---
title: Day-5-Sed应用实例
date: 2018-09-04 10:05:40
tags: Linux 三剑客
top: 18
---
# sed用法实例 #

&emsp;sed对于linux三剑客来讲，在处理大量文本数据的时候，其功能的强大不言而喻。但是理解了简单的基础项，其实还是不行的，我们还要深入了解下他的应用以及用法，各类用法都是公式的套用，要尽量研究、变通其用法，让其能发挥更大的作用；

## 替换操作：s命令 ##

&emsp;替换文本中的字符串：

``` shell
[root@docker-Reg ~]# sed 's/my/i/' test.txt 
i am fine thanks
i dream in SHIJIAZHUANG
i life in you life
Do you like there?
yes  fine is ok
ok nimabi
giao giao giao 
```

&emsp;__-n选项和p命令一起使用表示只打印那些发生替换的行；__
&emsp;__sed -n 's/my/i/p' test.txt (file)__

``` shell
[root@docker-Reg ~]# sed -n 's/my/i/p' test.txt 
> i dream in SHIJIAZHUANG
> i life in you life
```

&emsp;__直接编辑文件选项-i，会匹配file文件中每一行的第一个my替换为i；__

``` shell
[root@docker-Reg ~]# cat test.txt 
> i am fine thanks
> i dream in SHIJIAZHUANG
> i life in you life
> Do you like there?
> yes  fine is ok
> ok nimabi
> giao giao giao 
> EOF
```

## 全面替换标记g ##

&emsp;使用后缀/g标记会替换每一行中的所有匹配；

``` shell
[root@docker-Reg ~]# sed 's/i/my/g' test.txt
> my am fmyne thanks
> my dream myn SHIJIAZHUANG
> my lmyfe myn you lmyfe
> Do you lmyke there?
> yes  fmyne mys ok
> ok nmymabmy
> gmyao gmyao gmyao 
> EOF
```

&emsp;当需要从第N处匹配开始替换时，可以使用/Ng；

``` shell
[root@docker-Reg ~]# sed 's/skr/giao/5g' test2.txt   # 从第五行开始替换
skr
skrskrskrskrgiaogiaogiaogiaogiaogiaogiao
[root@docker-Reg ~]# sed 's/skr/giao/3g' test2.txt   # 从第三行开始替换
skr
skrskrgiaogiaogiaogiaogiaogiaogiaogiaogiao
[root@docker-Reg ~]# sed 's/skr/giao/2g' test2.txt   # 从第二行开始替换
skr
skrgiaogiaogiaogiaogiaogiaogiaogiaogiaogiao
```

## 定界符 ##

&emsp;以上命令中字符 / 在sed中作为定界符使用，也可以使用任意的定界符；

``` shell
sed 's:test:TEXT:g'
sed 's|test|TEXT|g'
```

&emsp;__定界符出现样式内部时，需要进行转义：__

``` shell
sed 's/\/bin/\/usr\/local\/bin/g'
```

## 删除操作：d命令 ##

&emsp;__删除空白行__

``` shell
sed '/^$/d' test2.txt 
```

&emsp;__删除文件的第2行__

``` shell
sed '2d' test2.txt 
```

&emsp;__删除文件第二行到末尾的所有行：__

``` shell
[root@docker-Reg ~]# sed '2,$d' test2.txt 
skr
```

&emsp;__删除文件最后一行：__

``` shell
sed '$d' test2.txt 
```

&emsp;__删除文件中所有开头是skr的行：__

``` shell
sed '/^skr/d' test2.txt 
```

## 已匹配字符串标记& ##

&emsp;正则表达式\w\+ 匹配每一个单词，使用[&]替换它，&对应于之前所匹配到的单词

``` shell
[root@docker-Reg ~]# sed 's/\w\+/[&]/g' test.txt 
[my] [am] [fmyne] [thanks]
[my] [dream] [myn] [SHIJIAZHUANG]
[my] [lmyfe] [myn] [you] [lmyfe]
[Do] [you] [lmyke] [there]?
[yes]  [fmyne] [mys] [ok]
[ok] [nmymabmy]
[gmyao] [gmyao] [gmyao] 
[EOF]
[192].[168].[1].[2]
```

&emsp;所有以192.168.1.2开头行都会被替换成它自己加localhost

``` shell
[root@docker-Reg ~]# sed 's/^192.168.1.2/&localhost/' test.txt 
my am fmyne thanks
my dream myn SHIJIAZHUANG
my lmyfe myn you lmyfe
Do you lmyke there?
yes  fmyne mys ok
ok nmymabmy
gmyao gmyao gmyao 
EOF
192.168.1.2localhost
```

## 子串匹配标记\1 ##

&emsp;匹配给定样式的其中一部分；

``` shell
[root@docker-Reg ~]# echo this is digit 6 in a number | sed 's/6 \([a-z]\)/\1/'
this is digit in a number
```

&emsp;命令中digit 6，被替换成了 in。样式匹配到子串是7，\(..\) 用于匹配子串，对于匹配到的第一个子串被标记为\1，以此类推匹配到的第二个结果就是\2,例如：

``` shell
[root@docker-Reg ~]# echo aaa BBB | sed 's/\([a-z]\+\) \([A-Z]\+\)/\2 \1/'
BBB aaa
```

&emsp;love被标记为1，所有loveable会被替换成lovers，并打印出来：

``` shell
[root@docker-Reg ~]# sed -n 's/\(love\)able/\1rs/p' test.txt 
lovers
```

## 组合多个表达式 ##

``` shell
sed '表达式' | sed '表达式'
等价于：
sed '表达式'; 表达式'
```

## 引用 ##

&emsp;sed表达式可以使用单引号来引用，但是如果表达式内部包含变量字符串，就需要使用双引号。

``` shell
test=hello
echo hello word | sed "s/$test/HELLO"
HELLO word
```

## 选定行的范围：，（逗号） ##

&emsp;所有在模板test和check所确定的范围内的行都被打印：

``` shell
sed -n '/test/,/check/p' file

[root@docker-Reg ~]# sed -n '/Do/,/1/p' test.txt 
Do you lmyke there?
yes  fmyne mys ok
ok nmymabmy
gmyao gmyao gmyao 
EOF
```

&emsp;打印从第4行开始到第一个包含以1开头的行之间的所有行：

``` shell
[root@docker-Reg ~]# sed -n '6,/^1/p' test.txt 
ok nmymabmy
gmyao gmyao gmyao 
EOF
192.168.1.2
```

&emsp;对于模板am和Do之间的行，每行的末尾用字符串aaa bbb替换：

``` shell
[root@docker-Reg ~]# sed -n '/am/,/D/s/$/aaa bbb/p' test.txt 
my am fmyne thanksaaa bbb
my dream myn SHIJIAZHUANGaaa bbb
my lmyfe myn you lmyfeaaa bbb
Do you lmyke there?aaa bbb
[root@docker-Reg ~]# 
```

## 多点编辑：(e命令) ##

&emsp;-e选项允许在同一行里执行多条命令：

``` shell
[root@docker-Reg ~]# sed -e '1,5d' -e 's/love/yes/' test.txt 
ok nmymabmy
gmyao gmyao gmyao 
EOF
192.168.1.2

yes
yesable
```

&emsp;上述sed命令第一条命令表示删除1至5行，第二条命令用yes替换love，命令的执行顺序对结果有影响。如果两个命令都是替换命令，那么第一个替换命令将影响第二个替换命令的结果；
&emsp;和 -e 等价的命令是 --expression：

``` shell
[root@docker-Reg ~]# sed --expression 's/am/test/' --expression '/love/d' test.txt 
my test fmyne thanks
my dretest myn SHIJIAZHUANG
my lmyfe myn you lmyfe
Do you lmyke there?
yes  fmyne mys ok
ok nmymabmy
gmyao gmyao gmyao 
EOF
192.168.1.2
```

## 从文件读入：r命令 ##


&emsp;file里的内容被读进来，显示在于am匹配的行后面，如果匹配多行，则file的内容将显示在所有匹配行下面:

``` shell
[root@docker-Reg ~]# sed '/^my/r test2.txt' test.txt 
my am fmyne thanks
skr
skrskrskrskrskrskrskrskrskrskrskr
skrskrskrskrskrskrskrskrskrskrskr
skrskrskrskrsrksrksrkskrskrskrskr
skrskrksrksrksrskr
```

## 写入文件：w命令 ##

&emsp;在test2.txt中华所有包含skr的行都写入test.txt中:

``` shell
[root@docker-Reg ~]# cat test.txt 
skr
skrskrskrskrskrskrskrskrskrskrskr
skrskrskrskrskrskrskrskrskrskrskr
skrskrskrskrsrksrksrkskrs
```

## 追加（行下）：a\命令 ##

&emsp;将this is a test line 主驾到以skr开头的行后面

``` shell
[root@docker-Reg ~]# sed '/^skr/a\this is a test line' test.txt 
skr
this is a test line
skrskrskrskrskrskrskrskrskrskrskr
this is a test line
skrskrskrskrskrskrskrskrskrskrskr
this is a test line
skrskrskrskrsrksrksrkskrskrskrskr
this is a test line
skrskrksrksrksrskr
this is a test line
```

&emsp;在test.txt文件第5行之前插入this is a test line

``` shell
[root@docker-Reg ~]# sed -i '5i\this is a test line' test.txt 
[root@docker-Reg ~]# cat test.txt 
skr
skrskrskrskrskrskrskrskrskrskrskr
skrskrskrskrskrskrskrskrskrskrskr
skrskrskrskrsrksrksrkskrskrskrskr
this is a test line
```

## 下一个：n命令 ##

&emsp;如果skr 被匹配，则移动到匹配行的下一行，替换着一块的skr，变为bb，并打印该行，然后继续；

``` shell
[root@docker-Reg ~]# sed '/skr/{n;s/skr/bb/;}' test.txt 
skr
bbskrskrskrskrskrskrskrskrskrskr
skrskrskrskrskrskrskrskrskrskrskr
bbskrskrskrsrksrksrkskrskrskrskr
```

## 变形：y命令 ##

&emsp;把1~10行内所有的skr转变为大写，注意正则表达式元字符不能使用这个命令；

``` shell
[root@docker-Reg ~]# sed '1,10y/skr/SKR/' test.txt 
SKR
SKRSKRSKRSKRSKRSKRSKRSKRSKRSKRSKR
SKRSKRSKRSKRSKRSKRSKRSKRSKRSKRSKR
SKRSKRSKRSKRSRKSRKSRKSKRSKRSKRSKR
thiS iS a teSt line
SKRSKRKSRKSRKSRSKR
 SKRSKRSKRSKRSRKSRKSRKSKRSKRSKRSKR
 SKRSKRSKRSKRSRKSRKSRKSKRSKRSKRSKR
 SKRSKRSKRSKRSRKSRKSRKSKRSKRSKRSKR
```

## 退出：q命令 ##

&emsp;打印完第十行，退出sed

``` shell
[root@docker-Reg ~]# sed '10q' test.txt 
skr
skrskrskrskrskrskrskrskrskrskrskr
skrskrskrskrskrskrskrskrskrskrskr
skrskrskrskrsrksrksrkskrskrskrskr
this is a test line
skrskrksrksrksrskr
 skrskrskrskrsrksrksrkskrskrskrskr
 skrskrskrskrsrksrksrkskrskrskrskr
 skrskrskrskrsrksrksrkskrskrskrskr
 skrskrskrskrsrksrksrkskrskrskrskr
```

## 保持和获取：h命令和G命令 ## 

&emsp;在sed处理文件的时候，每一行都被保存在一个叫模式空间的临时缓冲区中，除非行被删除或者输出被取消，否则所有被处理的行都将打印在屏幕上，接着模式空间被清空，并存入新的一行等待处理；

``` shell
sed -e '/skr/h' -e '$G' test.txt
```

&emsp;在这个例子里，匹配skr的行被找到后，将存入模式空间，h命令将其估值并存入一个保存缓冲区的铁树缓冲区内。第二条语句的意思是，当达到最后一行后，G命令取出保持缓冲区的行，然后把它放回到模式空间中，且追加到现在已经存在于模式空间中的行的末尾。在这个例子中就是追加到最后一行。简单来说，任何包含skr的行都被复制并追加到该文件的末尾。

## 保持和互换：h命令和x命令

&emsp;互换模式空间和保持缓冲区的内容。也就是把包含skr与 skr的行互换：

``` shell
sed -e '/skr/h' -e '/ skr/x' test.txt 
```

## 脚本scriptfile ##

&emsp;sed脚本是一个sed的命令氢弹，启动Sed时以-f选项阴道脚本文件名。Sed对于脚本中输入的命令非常挑剔，在命令的末尾不能有任何空白或文本，如果在一行中有多哥命令，要用分号分隔，以#开头的行为注释行，且不能跨行；

``` shell
sed [options] -f scriptfile file(s)
```

## 打印奇数行或偶数行 ##

&emsp;方法1：

``` shell
sed -n 'p;n' test.txt 
sed -n 'n;p' test.txt
```

&emsp;方法2：

``` shell
sed -n '1~2p' test.txt
sed -n '2~2p' test.txt
```

## 打印匹配字符串的下一行 ##

``` shell
grep -A 1 SCC URFILE
sed -n '/SCC/{n;p}' URFILE
awk '/SCC/{getline; print}' URFILE
```

---
title: Day-1-Awk命令
date: 2018-08-27 10:17:11
tags: Liunx三剑客
top: 16
---

# Linux三剑客之Awk #

&emsp;Awk是一种处理文本文件的语言，是一个强大的文本分析工具。
&emsp;之所以叫Awk是因为其取了三位创始人Alfred Aho,Peter Weinberger.和Brain kernginghan的Family Name的字符。

## 语法 ##

``` shell
awk [选项参数] 'script' var=value file(s)
或
awk [选项参数] -f scriptfile var=value file(s)
```

&emsp;__awk的处理过程:__ 依次对每一行进行处理，然后输出：
&emsp;__awk的命令形式:__

``` shell
awk [-F][-f][-V] `BEGIN{} //{command1; command2} END{}`file
[-F][-f][-v]：大参数，-F指定分隔符，-f调用脚本，-v定义变量var=value
` `:引用代码块
BEGIN：初始化代码块，在对每个航进行处理之前，初始化代码，主要是引用全局变量，设置FS分隔符；
// ： 匹配代码块，可以使字符串或者正则表达式；
{} ： 命令代码块包含一条或多条命令
； ： 多挑明了使用分号分隔
END ： 结尾代码块，在对每一行进行处理之后再执行的代码块，主要是进行最终计算或输出结尾摘要信息；
```

&emsp;__特殊要点：__

``` shell
$0            表示整个当前行；
$1            每行第一个字段；
NF            字段数量变量；
NR            每行的记录号，多文件记录递增；
FNR           与NR类似，不过多文件记录不递增，每个文件都从1开始；
\t            制表符；
\n            换行符；
FS            BEGIN时定义分隔符
RS            输入的记录分隔符，默认为换行符（即文本是按一行一行输入）
~             匹配，与==相比不是精确比较
!~            不匹配，不精确比较
==            等于，必须全部相等，精确比较
!=            不等于，精确比较
&&            逻辑与
||            逻辑或
+             匹配时表示1个或1个以上
/[0-9][0-9]+/ 两个或两个以上数字
/[0-9][0-9]+/ 一个或一个以上数字
FILENAME      文件名
OFS           输出字段分隔符，默认也是空格，可以改为制表符等
ORS           输出的记录分隔符，默认为换行符，即处理结果也是一行一行输出到屏幕
-F'[:#/]'     定义三个分隔符
```

&emsp;__print & $0:__
&emsp;print是awk打印指定内容的主要命令

``` shell
awk '{print}' /etc/passwd  == awk '{print $0}' /etc/passwd
awk '{print ""}' /etc/passwd   # //不输出passwd 的内容。而是输出相同个数的空行，进一步解释awk是一行一行处理文本
awk '{print "a"}' /etc/passwd  # //输出相同个数的a行，一行只有一个a字母
awk -F":" '{print $1}' /etc/passwd  # //以":"为分隔符打印第一个字母
awk -F":" '{print $1;print $2}' /etc/passwd # //将每一行的前两个字字段，分行输出，进一步理解一行一行处理文本；
awk -F":" '{print $1,$3,$6}' OSF="\t" /etc/passwd # //输出字段1，3，6，以制表符作为分隔符
```

&emsp;__-f指定脚本文件__
&emsp;awk -f script.awk file

``` shell
BEGIN{
FS=":"
}
[root@docker-Reg ~]# awk 'BEGIN{X=0} /^$/{X+=1} END{print "I find",X,"blank lines."}' anaconda-ks.cfg 
I find 6 blank lines.
[root@docker-Reg ~]# ls -l|awk 'BEGIN{sum=0} !/^d/{sum+=$5} END{print "total size is",sum}'    # 计算文件大小
total size is 1031
```

&emsp;__-F指定分隔符__
&emsp;$1 指定分隔符后，第一个字段，$3第三个字段，\t是制表符；
&emsp;一个或多个连续的空格或制表符看作一个定界符，即多个空格看作一个空格

``` shell
awk -F":" '{print $1}' /etc/passwd    # 以“:”为分隔符，打印passwd文件的第一个字段；
awk -F":" '{print $1 $3}' /etc/passwd # $1和$3相连输出，不分隔；
输出结果：root0
awk -F":" '{print $1,$3}' /etcpasswd  # $1和$3以空格隔开 输出
输出结果：root 0
awk -F":" '{print $1 " " $3}' /etc/passwd  # $1和$3 之间手动添加空格分开；
输出结果：root 0
awk -F":" '{print "Username:" $1 "\t\t Uid:" $3}' /etc/passwd # 自定义输出
awk -F:'{print NF}' /etc/passwd         # 显示每行有多少字段
awk -F: '{print $NF}' /etc/passwd        # 将每行第NF个字段的值打印出来
awk -F: 'NF==4{print}' /etc/passwd       # 显示只有4个字段的行
awk -F: 'NF>2{print $0}' /etc/passwd     # 显示每行字段淑凉大于2的行
awk '{print NR,$0}' /etc/passwd          # 输出每行的行号
awk -F: 'NF==5{print}' /etc/passwd       # 显示第五行
awk -F: '{print NR,NF,$NF,"\t",$0}' /etc/passwd #依次打印行号，字段数，最后字段值，制表符，每行内容；
awk -F: 'NR==5||NR==6{print}' /etc/passwd # 显示第五行和第六行
route -n |awk 'NR!=1{print}'
```

&emsp;__匹配代码块__
&emsp;__纯字符匹配 ！纯字符不匹配 ~ 字段值匹配 !~ 字段值不匹配 ~ /a1|a2/字段值匹配a1或a2__

``` shell
awk '/docker/' /etc/passwd
awk '/docker/{print}' /etc/passwd
awk '/docker/{print $0}' /etc/passwd  # 三条指令输出的结果是一样的
awk '!/docker/{print $0}' /etc/passwd  # 输出不匹配docker的行 （！反义字符）
awk '/docker|mail/{print}' /etc/passwd
awk -F: '/mail/,/docker/{print}' /etc/passwd # 区间匹配
awk '/[2][7][7]*/{print $0}' /etc/passwd # 匹配包含27为数字开头的行，如27、277、27777....
awk -F: '$1~/mail/{print $1}' /etc/passwd # $1匹配指标内容显示
awk -F: '{if($1~/mail) print $1}' /etc/passwd # 与上面相同
awk -F: '$1!~/mail/{print $!}' /etc/passwd # 不匹配
awk -F: '$1!~/mail|mysql/{print $1}' /etc/pawsswd
```

&emsp;__IF语句__
&emsp;__必须用在{}中，且比较内容用（）扩起来__

``` shell
[root@docker-Reg ~]# awk -F: '{if($1~/mail/) print $1}' /etc/passwd # 简写
mail
[root@docker-Reg ~]# awk -F: '{if($1~/mail/){print $1}}' /etc/passwd # 全写
mail
awk -F: '{if($1~/mail/) {print $1} else {print $2}}' /etc/passwd # if判断句如果什么不然什么  if...else....
```
---
title: Day-3-AWk应用
date: 2018-08-29 17:49:51
tags: Linux三剑客命令
top: 17
---

# AWK应用实例 #

&emsp;这几天有点事比较忙，更新较慢；
&emsp;awk的数组，以及正则表达式的引用，相对来讲只能多练；练的多了慢慢就理解了，今天打算磨合awk的应用，以便让自己迅速的理解awk各类语法的应用，能熟练套用、应用语法；


## 应用① ##

``` shell
awk -F" " '{print NF}' hei.sh   # 输出文件每行有多少个字段
awk -F" " '{print $1,$2,$3,$4,$5}' hei.sh   # 以空格为分隔符输出前五个字段
awk -F" " '{print $1,$2,$3,$4,$5}' OFS='\t' hei.sh  # 输出前五个字段并使用制表符分隔输出
awk -F" " '{print NR,$1,$2,$3,$4,$5}' OFS='\t' hei.sh  # 制表符分隔输出前五个字段，并打印行号
```

## 应用② ##

``` shell
awk -F'[:#]' '{print NF}' hei.sh  #  指定多个分隔符"[:#]" 输出每行多少字段
awk -F'[:#]' '{print NR,$1,$2,$3}' OFS='\t' hei.sh  # 制表符分隔输出前三个字段，并打印行号
```

## 应用③ ##

``` shell
awk -F'[:#/]' '{print NF}' /etc/passwd  # 指定三个分隔符，并输出每行字段数
awk -F'[:#/]' '{print NR,$1,$2,$3,$4}' OFS='\t' /etc/passwd # 制表符分隔 并输出多个字段
```

## 应用④ ##

&emsp;__计算/home目录下，普通文件的大小，使用KB作为单位__

``` shell
ls -l|awk 'BEGIN{sum=0} !/^d/{sum +=$5}END{print "total size is:",sum/1024,"KB"}' 
ls -l|awk 'BEGIN{sum=0} !/^d/{sum+=$5} END{print "total size is:",int(sum/1024),"KB"}' # int的意思是取整的意思
```

&emsp;通常，对于每个输入行， awk 都会执行每个脚本代码块一次。然而，在许多编程情况中，可能需要在 awk 开始处理输入文件中的文本之前执行初始化代码。对于这种情况， awk 允许您定义一个 BEGIN 块。
&emsp;因为 awk 在开始处理输入文件之前会执行 BEGIN 块，因此它是初始化 FS（字段分隔符）变量、打印页眉或初始化其它在程序中以后会引用的全局变量的极佳位置。
awk 还提供了另一个特殊块，叫作 END 块。 awk 在处理了输入文件中的所有行之后执行这个块。通常， END 块用于执行最终计算或打印应该出现在输出流结尾的摘要信息。

## 应用⑤ ##

&emsp;__统计netstat -anp状态为LISTEN和CONNECT的连接数量分别是多少__

``` shell
netstat -anp|awk '$6~/LISTEN|CONNECTED/{sum[$6]++} END{for (i in sum) printf "%-10s %-6s %-3s \n",i,"",sum[i]}'
```

## 应用⑥ ##

&emsp;统计/home目录下不同用户的普通文件的总数是多少？

``` shell
[root@docker-Reg ~]# ls -l|awk 'NR!=1 && !/^d/{sum[$3]++} END{for (i in sum)printf "%-6s %-5s %-3s \n",i,"",sum[i]}'
root         2   
```

&emsp;统计/home目录下不同用户的普通文件的大小的总size是多少？

``` shell
[root@docker-Reg ~]# ls -l|awk 'NR!=1 && !/^d/{sum[$3]++} END{for (i in sum)printf "%-6s %-5s %-3s %-2s \n",i," ",sum[i]/1024/1024,"MB"}'
root         1.90735e-06 MB 
```

## 应用⑦ ##

&emsp;输出成绩表

``` shell
[root@docker-Reg ~]# cat >test0 <<EOF
> Marry   2143 78 84 77
> Jack    2321 66 78 45
> Tom     2122 48 77 71
> Mike    2537 87 97 95
> Bob     2415 40 57 62
> EOF
[root@docker-Reg ~]# awk 'BEGIN{math=0;eng=0;com=0;printf "Lineno.   Name    No.    Math   English   Computer    Total\n";printf "------------------------------------------------------------\n"}{math+=$3; eng+=$4; com+=$5;printf "%-8s %-7s %-7s %-7s %-9s %-10s %-7s \n",NR,$1,$2,$3,$4,$5,$3+$4+$5} END{printf "------------------------------------------------------------\n";printf "%-24s %-7s %-9s %-20s \n","Total:",math,eng,com;printf "%-24s %-7s %-9s %-20s \n","Avg:",math/NR,eng/NR,com/NR}' test0
Lineno.   Name    No.    Math   English   Computer    Total
------------------------------------------------------------
1        Marry   2143    78      84        77         239     
2        Jack    2321    66      78        45         189     
3        Tom     2122    48      77        71         196     
4        Mike    2537    87      97        95         279     
5        Bob     2415    40      57        62         159     
------------------------------------------------------------
Total:                   319     393       350                  
Avg:                     63.8    78.6      70                   
[root@docker-Reg ~]# 
```

## 应用⑧ ##

&emsp;利用awk取IP及子网掩码；

``` shell
[root@docker-Reg ~]# ip addr show eth0|awk -F'[: ]+' 'NR==3 {print $3,$5}'
192.168.56.18/24 192.168.56.255

[root@docker-Reg ~]# ip addr show eth0|awk -F'[: ]+' 'NR==3 {print}'
    inet 192.168.56.18/24 brd 192.168.56.255 scope global eth0 
# 整行打印
```
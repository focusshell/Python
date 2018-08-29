---
title: Day-2-Awk命令下部
date: 2018-08-28 09:56:51
tags: Linux三剑客命令
top: 16
---

# Awk命令下部分 #

&emsp;__条件表达式:__
&emsp;__== != > >=__

``` shell
awk -F":" "$1=="mysql"{print $3}" /etc/passwd
awk -F":" '{if($1=="docker") print $3}' /etc/passwd  # 与上面相同
awk -F":" '$1!="mysql" {print $3}' /etc/passwd       # 不等于
awk -F":" '$3>1000{print $3}' /etc/passwd            # 大于
awk -F":" '$3>=100{print $3}' /etc/passwd            # 大于等于
awk -F":" '$3<1{print $3}' /etc/passwd               # 小于
awk -F":" '$3<=1{print $3}' /etc/passwd              # 小于等于
```

&emsp;__逻辑运算符__
&emsp;__&& ||__

``` shell
awk -F: '$1~/daocker/ && $3>8{print }' /etc/passwd  # 逻辑与，$1匹配docker，并且$3>8
awk -F: '{if($1~/docker/ && $3>8)print }' /etc/passwd  
awk -F: '$1~/docker/ || $3>1000 {print }' /etc/passwd  # 逻辑或
awk -F: '{if($1~/docker/ || $3>1000) print }' /etc/passwd 
```

&emsp;__数值运算__

``` shell
awk -F: '$3 > 100' /etc/passwd 
awk -F: '$3 > 100 || $3 < 5' /etc/passwd
awk -F: '$3+$4 > 200' /etc/passwd
awk -F: '/docker|mail/{print $3+10}' /etc/passwd     #  第三个字段加10打印
awk -F: '/docker/{print $3-$4}' /etc/passwd     # 减法
awk -F: '/docker/{print $3*$4}' /etc/passwd     # 求乘积
awk '/MemFree/{print $2/1024}' /proc/meminfo    # 除法
awk '/MemFree/{print int($2/1024)}' /proc/meminfo  # 取整
```

&emsp;__输出分隔符OFS__

``` shell
awk '$6 ~ /FIN/ || NR==1 {print NR,$4,$5,$6}' OFS="\t" netstat.txt
awk '$6 ~ /WAIT/ || NR==1 {print NR,$4,$5,$6}' OFS="\t" netstat.txt
# 输出字段6匹配WAIT的行，期中输出没行行号，字段4，5，6，并使用制表符分割字段
```

&emsp;__输出处理结果到文件__

>1. 在命令代码块中直接输出 

``` shell
route -n|awk 'NR!=1{print > "./fs"}
```

>2. 使用重定向进行输出

```shell
route -n|awk 'NR!=1{print}' > ./fs
```

&emsp;__格式化输出__

``` shell
netstat -anp|awk '{print "%-8s %-9s %=10s\n",$1,$2,$3}'
```

&emsp;printf表示格式输出
&emsp;%格式化输出分隔符
&emsp;-8长度为8个字符
&emsp;s表示字符穿类型
&emsp;打印每行前三个字段，指定每个字段输出字符串类型（长度为8），第二个字段输出字符串类型（长度为8）
&emsp;第三个字段输出字符串类型（长度为10）

``` shell
netstat -anp|awk '$6=="LISTEN" || NR==1 {printf "%-10s %-10s %-10s \n",$1,$2,$3}'
netstat -anp|awk '$6=="LISTEN" || NR==1 {print "%-3s %-19s %-10s \n",NR,$1,$2,$3'
```

&emsp;__IF语句__

``` shell
awk -F: '{if($3>100)print "large";else print "smail"}' /etc/passwd
smail
smail
smail
large
smail
smail
smail
awk -F: 'BEGIN{A=0;B=0} {if($3>100) {A++;print "large"} else {B++;print "samil"}} END {print A，"\t" B}' /etc/passwd   # ID大于100，A加1，否则B加1
awk -F: '{if($3<100) next;else print}' /etc/passwd
awk -F: 'BEGIN{i=1} {if(i<NF) print NR,NF,i++ }'  /etc/passwd
awk -F: 'BEGIN{i=1} {if(i<NF) {print NR,NF}i++ }' /etc/passwd
```

&emsp;另一种形式：

``` shell
awk -F: '{print ($3>100 ? "yes":"NO")}' /etc/passwd
awk -F: '{print ($3>100 ? $3":\tyes":$3":\tno")}' /etc/passwd
```

&emsp;__while语句__

``` shell
[root@docker-Reg ~]# awk -F: 'BEGIN{i=1} {while(i<NF) print NF,$i,i++}' /etc/passwd
7 root 1
7 x 2
7 0 3
7 0 4
7 root 5
7 /root 6
```

&emsp;__数组__

``` shell
netstat -anp|awk 'NR!=1{a[$6]++} END{for (i in a)print i,"\t",ap[i]}'
betstat -anp|awk 'NR!=1{a[$6]++} END{for (i in a)printf "%-20s %-10s %-5s\n",i,"\t",a[i]}'
```
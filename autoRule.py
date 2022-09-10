import sys
import random

args=sys.argv

def ret_rule_ans(rule_bin_str_reversed,l,m,r):
    rule_ans=0
    for i in range(len(rule_bin_str_reversed)):
        one_rule_ans=0
        if rule_bin_str_reversed[i]=="1":
            one_rule_ans=1
            now_bin=format(i,"b")
            now_bin=now_bin.zfill(3)

            one_rule_ans &= l if now_bin[0]=="1" else (not l)
            one_rule_ans &= m if now_bin[1]=="1" else (not m)
            one_rule_ans &= r if now_bin[2]=="1" else (not r) 
        rule_ans|=one_rule_ans
    return rule_ans


def gen_rule(rule_num):
    rule_bin=format(rule_num,"b")
    print(rule_bin)
    rule_bin=rule_bin[::-1]
    print(rule_bin)
    rule_eval=""
    for i in range(len(rule_bin)):
        if rule_bin[i]=="1":
            now_bin=format(i,"b")
            now_bin=now_bin.zfill(3)
            for j in range(len(now_bin)):
                if j==0:
                    rule_eval+=" (l " if now_bin[j]=="1" else " (not l "
                elif j==1:
                    rule_eval+=" m " if now_bin[j]=="1" else "not m"
                elif j==2:
                    rule_eval+=" r " if now_bin[j]=="1" else " not r "
                rule_eval+=" and "
            rule_eval+=" 1) "

            rule_eval+=" or "
    rule_eval+="0"
    print(rule_eval)
    return rule_eval


c=0
while True:
    h=800
    length=h*2
    mid=length//2
    
    rule_num=int(random.random()*255)
    c+=1
    rule_bin_str=format(rule_num,"b")
    rule_bin_str=rule_bin_str[::-1]
    rule_formula=gen_rule(rule_num)
    cell=[]
    pre_cell=[]
    
    
    #shokika
    for i in range(length):
        r=1 if 0.9<random.random() else 0
        r=0
        cell.append(r)
        pre_cell.append(r)
    cell[mid]=1
    pre_cell[mid]=1
    
    #main
    for i in range(h):
        for e in cell:
            a=""
            if e==1:
                a="#"
            else:
                a=" "
            print(a,end="")
        print("")
        for j in range(1,len(cell)-1):
            l=pre_cell[j-1]
            m=pre_cell[j]
            r=pre_cell[j+1]
            if ret_rule_ans(rule_bin_str,l,m,r):
                cell[j]=1
            else:
                cell[j]=0
        for k in range(len(cell)):
            pre_cell[k]=cell[k]


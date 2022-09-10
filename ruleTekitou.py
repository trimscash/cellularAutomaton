
#000
# 0
#001
# 1
#010
# 1
#011
# 1
#100
# 1
#101
# 0
#110
# 0
#111
# 0

h=800
length=h*2
mid=length//2

cell=[]
pre_cell=[]

for i in range(length):
    cell.append(0)
    pre_cell.append(0)
cell[mid]=1
pre_cell[mid]=1

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
        if (l or not m)and r:
            
            cell[j]=1
        else:
            cell[j]=0
    for k in range(len(cell)):
        pre_cell[k]=cell[k]





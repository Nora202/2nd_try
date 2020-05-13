def CreateNums():
    f=open('g:\\myProject\\test.txt','w')
    Num=int(input())
    x=0
    for x in range(1,Num+1):
        len_str=''
        for y in range(1,x+1):
            sig_str='{0}*{1}={2}\t'.format(y,x,x*y)
            len_str+=sig_str
        f.write(len_str+'\n')
    f.close()
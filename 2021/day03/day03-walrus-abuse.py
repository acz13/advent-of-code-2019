print((f:=lambda d,j:int([(j:=[k for k in j if(k[b]==d)==(sum(int(i[b])for i in j)*2>=len(j))])for b in range(len(j[0]))if len(j)>1][-1][0],2))("1",(l:=__import__("sys").stdin.readlines()))*f("0",l))

print((f:=lambda d,j: int([(j:=[k for k in j if (k[b]==d)==([i[b] for i in j].count("1")*2>=len(j))]) for b in __import__("itertools").takewhile(lambda __:'j' not in vars() or len(j)>1,__import__("itertools").count(0))][-1][0],2))("1",(l:=__import__("sys").stdin.readlines()))*f("0",l))

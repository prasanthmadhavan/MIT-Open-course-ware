from string import *
def search2(target,key):
	count,a = 0,0
	tlen,klen = len (target),len (key)
	for i in range(0,tlen):
		if target[a:klen+a]==key:
			count = count+1
			a = a+1
		else:	a = a+1

	print target
	print key
	print count	


count = 0
def search1(target,key):
         global count
         i = 0
         klen = len (key)
         if find(target,key)==-1: return count
         else:
                count +=1;
                target = target[find(target,key)+klen:]
                count = search1(target,key)
         print count
	 print target
	 print key
         return count

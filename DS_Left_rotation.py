N, D = map(int, input().split())
#array = list(map(int, input().split()))
array = input().split()
for _ in range(D):
    array.append(array[0])
    array.pop(0)

print(' '.join(array[i] for i in range(len(array))))
#print(' '.join(str(i) for i in array))
#for i in array: print(i,end=" ")

###############
n, d = map(int, input().strip().split())
arr = [int(arr_t) for arr_t in input().strip().split()]
for _ in range(d):
    arr.append(arr.pop(0))
print (*arr) # * indicates that there may be more than one arr

###############
n,d = map(int, input().strip().split())
arr = map(int, input().strip().split())
print (' '.join(str(s) for s in (arr[d:] + arr[0:d])))

###############
N, d = map(int, input().split())
#array = list(map(int, input().split()))
arr = input().split()
for value in (arr[d:] + arr[0:d]):
	print (value)

###############
n,r=input().split()
v=input().split()
tmp=0
out=[]
j=int(r)
for i in range(0,len(v)):
    out.append(v[j])
    if(j!=len(v)-1):
        j=j+1
    else:
        j=0

print(" ".join(map(str,out)))

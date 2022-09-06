def parent(i):
    return i//2
def left(i):
    return i*2
def right(i):
   return 2*1+1

#def my_heep(mylist,i):
 #   len=len(mylist)
  #  for i in range()
def max_heapify(A,n,i):
    largest = i
    left_child= i*2#left(i)
    right_child= i*2+1 #right(i)
    #comparing it with the left child
    if(left_child < n and A[largest]<A[left_child]):
        largest = left_child
    #comparing it with the right child
    if(right_child<n and A[right_child]>A[largest]):
        largest =right_child
    #swaping parents
    if largest != i:
        A[i],A[largest] =A[largest],A[i]
        #call max heapify
        max_heapify(A,n,largest)

# LENGTH Of ARR A a
A=[45,34,1,4,8,90,10]
n=len(A)
#(bild max-heap) FOR LOOP WHERE RANGE IS N FLORE DIVISION BY 2 TO -1 AND DECRIMEN BY -1
#define heapSortArray
def heapSort(A):
    for i in range(n-1,0,-1):#n is length of the array 
        #swap last element with the first position
        A[i],A[0]=A[0],A[i]
        max_heapify(A,i,0)

#def build_max_heap(A):
for i in range(n//2-1,-1,-1): 
    #print(i)
    max_heapify(A, n, i) 
heapSort(A)
print("The sorted array: ")
for i in range (n):
    print(A[i])

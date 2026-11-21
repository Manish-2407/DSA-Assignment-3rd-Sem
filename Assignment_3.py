#Assignments-3
def check_n(n):
    if type(n) is not int or n<0:
        raise ValueError("n must be a non-negative integer")

def factorial(n):
    check_n(n)
    if n==0:
        return 1
    return n*factorial(n-1)

def natural_sum(n):
    check_n(n)
    if n==0:
        return 0
    return n+natural_sum(n-1)

def power(x,n):
    check_n(n)
    if n==0:
        return 1
    return x*power(x,n-1)

def is_sorted(d,i=0):
    if i>=len(d)-1:
        return True
    if d[i]>d[i+1]:
        return False
    return is_sorted(d,i+1)

class Stack:
    def __init__(self):
        self.d=[]

    def __len__(self):
        return len(self.d)

    def is_empty(self):
        return len(self.d)==0

    def push(self,e):
        self.d.append(e)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.d.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.d[-1]

class CircularQueue:
    def __init__(self,cp=5):
        if type(cp) is not int or cp<1:
            raise ValueError("capacity must be a positive integer")
        self.d=[None]*cp
        self.sz=0
        self.fr=0

    def __len__(self):
        return self.sz

    def is_empty(self):
        return self.sz==0

    def enqueue(self,e):
        if self.sz==len(self.d):
            raise OverflowError("queue is full")
        i=(self.fr+self.sz)%len(self.d)
        self.d[i]=e
        self.sz+=1

    def first(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.d[self.fr]

    def dequeue(self):
        e=self.first()
        self.d[self.fr]=None
        self.fr=(self.fr+1)%len(self.d)
        self.sz-=1
        return e

    def display(self):
        r=[]
        for i in range(self.sz):
            r.append(self.d[(self.fr+i)%len(self.d)])
        return r

class CircularDeque(CircularQueue):
    def add_first(self,e):
        if self.sz==len(self.d):
            raise OverflowError("deque is full")
        self.fr=(self.fr-1)%len(self.d)
        self.d[self.fr]=e
        self.sz+=1

    def add_last(self,e):
        self.enqueue(e)

    def delete_first(self):
        return self.dequeue()

    def delete_last(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        i=(self.fr+self.sz-1)%len(self.d)
        e=self.d[i]
        self.d[i]=None
        self.sz-=1
        return e

def main():
    print("PART A, Q2: RECURSIVE FUNCTIONS")
    print("factorial(5) =",factorial(5))
    print("natural_sum(10) =",natural_sum(10))
    print("power(2, 10) =",power(2,10))

    print("\nPART A, Q4: NON-DECREASING ORDER")
    for d in ([],[5],[1,1,3],[1,3,2]):
        print(d,"->",is_sorted(d))

    print("\nPART C, Q2: STACK")
    s=Stack()
    s.push(10)
    s.push(20)
    print("top =",s.top(),"length =",len(s))
    print("Pop:",s.pop(),"then",s.pop(),"empty:",s.is_empty())

    print("\nPART C, Q8: CIRCULAR QUEUE")
    q=CircularQueue(3)
    for e in (10,20,30):
        q.enqueue(e)
    print("Full queue:",q.display(),"storage:",q.d)
    print("Dequeue:",q.dequeue())
    q.enqueue(40)
    print("Wrapped queue:",q.display(),"storage:",q.d,"front:",q.fr,"size:",q.sz)

    print("\nPART C, Q10: CIRCULAR DEQUE")
    dq=CircularDeque(4)
    dq.add_last(20)
    dq.add_first(10)
    dq.add_last(30)
    print("After additions:",dq.display())
    print("delete_first:",dq.delete_first())
    print("delete_last:",dq.delete_last())
    print("Remaining:",dq.display())

if __name__=="__main__":
    main()
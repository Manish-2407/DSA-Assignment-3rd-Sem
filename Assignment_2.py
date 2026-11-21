"""Assignment-2: Lab Work 1 and Lab Work 2."""
from time import perf_counter
from math import log2
import random
import matplotlib.pyplot as plt

TR=7
SD=2026

def list_indexing(v):
    return v[len(v)//2]

def binary_search(v,x):
    l,h=0,len(v)-1
    while l<=h:
        m=(l+h)//2
        if v[m]==x:
            return m
        if v[m]<x:
            l=m+1
        else:
            h=m-1
    return -1

def linear_search(v,x):
    for i,j in enumerate(v):
        if j==x:
            return i
    return -1

def merge_sort(v):
    if len(v)<=1:
        return list(v)
    m=len(v)//2
    l=merge_sort(v[:m])
    r=merge_sort(v[m:])
    a=[]
    i=j=0
    while i<len(l) and j<len(r):
        if l[i]<=r[j]:
            a.append(l[i])
            i+=1
        else:
            a.append(r[j])
            j+=1
    a.extend(l[i:])
    a.extend(r[j:])
    return a

def pair_counter(n):
    c=0
    for _ in range(n):
        for _ in range(n):
            c+=1
    return c

def subset_masks(n):
    for i in range(1<<n):
        yield i

def enumerate_subsets(n):
    c=0
    for _ in subset_masks(n):
        c+=1
    return c

def prefix_average1(v):
    a=[]
    for j in range(len(v)):
        s=0
        for i in range(j+1):
            s+=v[i]
        a.append(s/(j+1))
    return a

def prefix_average2(v):
    a=[]
    s=0
    for j,x in enumerate(v):
        s+=x
        a.append(s/(j+1))
    return a

def validate():
    cs=[
        ([],[]),
        ([7],[7.0]),
        ([2,4,6],[2.0,3.0,4.0]),
        ([-2,-4,-6],[-2.0,-3.0,-4.0]),
        ([3,-3,9,-1],[3.0,0.0,3.0,2.0]),
        ([0.5,1.5,-2.0],[0.5,1.0,0.0]),
    ]
    for i,j in cs:
        assert prefix_average1(i)==j
        assert prefix_average2(i)==j
    for i in ([],[1],[4,-1,4,0],[5,4,3,2,1]):
        assert merge_sort(i)==sorted(i)
        o=sorted(i)
        for z in (-10,-1,0,1,4,10):
            for k in (binary_search,linear_search):
                t=k(o,z)
                assert (t==-1)==(z not in o)
                if t!=-1:
                    assert o[t]==z
    assert list_indexing([10,20,30])==20
    for n in range(8):
        assert pair_counter(n)==n*n
        assert list(subset_masks(n))==list(range(2**n))
        assert enumerate_subsets(n)==2**n
    return "Passed: empty, singleton, positive, negative, mixed and float prefix cases; searches, sorting, indexing, pairs and subsets."

def measure(f,a,b=1):
    f(*a)
    s=[]
    for _ in range(TR):
        t0=perf_counter()
        for _ in range(b):
            f(*a)
        s.append((perf_counter()-t0)/b)
    return sorted(s)[TR//2],s

def growth_value(s,n):
    if s=="list_indexing":
        return 1
    if s=="binary_search":
        return n.bit_length()-1
    if s=="linear_search":
        return n
    if s=="merge_sort":
        return n*(n.bit_length()-1)
    if s=="pair_counter":
        return n*n
    return 2**n

def lab_work1():
    print("\nLAB WORK 1: BENCHMARKING ALGORITHMIC GROWTH RATES")
    xp=[
        (list_indexing,"Theta(1)",[128,512,2048,8192,32768],10000),
        (binary_search,"Theta(log n) for misses",[128,512,2048,8192,32768],500),
        (linear_search,"Theta(n) for misses",[128,512,2048,8192,32768],20),
        (merge_sort,"Theta(n log n)",[128,256,512,1024,2048,4096],1),
        (pair_counter,"Theta(n^2)",[50,100,200,400,800],1),
        (enumerate_subsets,"Theta(2^n), small masks",[8,10,12,14,16,18],1),
    ]
    rg=random.Random(SD)
    rs=[]
    for f,bd,sz,bt in xp:
        ts=[]
        print(f"\n{f.__name__} (batch={bt})")
        print("n median seconds    seven trial times (seconds per call)")
        for n in sz:
            if f in (list_indexing,binary_search,linear_search):
                d=list(range(n))
                ar=(d,) if f is list_indexing else (d,-1)
                e=n//2 if f is list_indexing else -1
            elif f is merge_sort:
                d=[rg.randint(-10*n,10*n) for _ in range(n)]
                ar,e=(d,),sorted(d)
            else:
                ar=(n,)
                e=n*n if f is pair_counter else 2**n
            assert f(*ar)==e
            md,sm=measure(f,ar,bt)
            ts.append(md)
            tt=", ".join(f"{t:.8g}" for t in sm)
            print(f"{n:<7} {md:<17.8g} {tt}")
        rs.append((f.__name__,bd,sz,ts))

    fg,axs=plt.subplots(2,3,figsize=(15,8),constrained_layout=True)
    fn,axn=plt.subplots(6,3,figsize=(15,22),constrained_layout=True)
    for ix,(nm,bd,sz,ts) in enumerate(rs):
        ax=axs.flat[ix]
        mo=[ts[0]*growth_value(nm,n)/growth_value(nm,sz[0]) for n in sz]
        ax.plot(sz,ts,"o-",label="Measured median")
        ax.plot(sz,mo,"--",label="Scaled growth model")
        ax.set(title=nm,xlabel="Input size n",ylabel="Seconds per call")
        ax.grid(True,alpha=0.3)
        ax.legend(fontsize=8)
        p1=[t/n for n,t in zip(sz,ts)]
        p2=[t/(n*n) for n,t in zip(sz,ts)]
        p3=[t/(n*log2(n)) for n,t in zip(sz,ts)]
        print(f"\n{nm}: normalized timing table")
        print("n       T(n)/n          T(n)/n^2        T(n)/(n log2 n)")
        for n,a,b,c in zip(sz,p1,p2,p3):
            print(f"{n:<7} {a:<15.6g} {b:<15.6g} {c:.6g}")
        for cl,(lb,vs) in enumerate([
            ("T(n)/n",p1),
            ("T(n)/n^2",p2),
            ("T(n)/(n log2 n)",p3),
        ]):
            ax=axn[ix,cl]
            ax.plot(sz,vs,"o-")
            ax.set(title=f"{nm}: {lb}",xlabel="Input size n",ylabel="Normalized seconds")
            ax.grid(True,alpha=0.3)
    fg.suptitle("Lab 1 Task 4: execution time versus input size")
    fn.suptitle("Lab 1 Task 4: T(n)/n, T(n)/n^2 and T(n)/(n log2 n)")
    fg.savefig("lab1_execution_times.png",dpi=160)
    fn.savefig("lab1_normalized_times.png",dpi=160)
    plt.close(fg)
    plt.close(fn)
    print("\nSaved lab1_execution_times.png and lab1_normalized_times.png.")

def lab_work2():
    print("\nLAB WORK 2: PREFIX AVERAGES")
    rg=random.Random(SD+1)
    sz=[1,10,100,200,400,800,1600,3200]
    q,ln,cf=[],[],[]
    print("n       nested seconds    running seconds   speedup   T1/n^2       T2/n")
    for ix,n in enumerate(sz):
        d=[rg.randint(-100,100) for _ in range(n)]
        assert prefix_average1(d)==prefix_average2(d)
        fs=[prefix_average1,prefix_average2]
        if ix%2:
            fs.reverse()
        tm={}
        sm={}
        for f in fs:
            bt=100 if n<=10 else (10 if f is prefix_average2 else 1)
            tm[f],sm[f]=measure(f,(d,),bt)
        t1,t2=tm[prefix_average1],tm[prefix_average2]
        q.append(t1)
        ln.append(t2)
        if max(sm[prefix_average2])<min(sm[prefix_average1]):
            cf.append(n)
        print(f"{n:<7} {t1:<17.8g} {t2:<17.8g} {t1/t2:<9.2f} {t1/n**2:<12.5g} {t2/n:.5g}")
        for f in (prefix_average1,prefix_average2):
            print(f"  {f.__name__} trials: {sm[f]}")

    fg,axs=plt.subplots(1,3,figsize=(16,5),constrained_layout=True)
    axs[0].plot(sz,q,"o-",label="prefix_average1")
    axs[0].plot(sz,ln,"o-",label="prefix_average2")
    axs[0].set_title("Both implementations")
    for ax,ts,pw,ti in [(axs[1],q,2,"Quadratic: O(n^2)"),
                        (axs[2],ln,1,"Linear: O(n)")]:
        ax.plot(sz,ts,"o-",label="Measured median")
        ax.plot(sz,[ts[-1]*(n/sz[-1])**pw for n in sz],"--",label="Scaled model")
        ax.set_title(ti)
    for ax in axs:
        ax.set_xlabel("Sequence length n")
        ax.set_ylabel("Seconds per call")
        ax.grid(True,alpha=0.3)
        ax.legend()
    fg.suptitle("Lab 2 Task 5: quadratic versus linear prefix averages")
    fg.savefig("lab2_prefix_averages.png",dpi=160)
    plt.close(fg)
    print("\nSaved lab2_prefix_averages.png.")

def main():
    lab_work1()
    lab_work2()

if __name__=="__main__":
    main()
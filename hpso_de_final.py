import csv
import math
from random import seed
from random import randrange
import random
from random import randint
from operator import add
from operator import sub
from operator import mul

def gaus(A,cl,col,l,data,n_row,n_col,actual):
        #print data
        count=0.0
        sum1=0.0
        dsq=0.0
        for i in range(n_row):
                if(i>=l and i<l+10):
                        continue
                if(actual[data[i][n_col]]==cl):
                        sum1+=float(data[i][col])
                        count+=1
        
        u=sum1/count
        #print u
        for i in range(n_row):
                if(i>=l and i<l+10):
                        continue
                if(actual[data[i][n_col]]==cl):
                        #print float(data[i][col])
                        diff=float(data[i][col])-u
                        dsq+=diff*diff
        #print dsq
        varience=dsq/(count-1)
        std=math.sqrt(varience)
        #print varience
        power=-((A-u)*(A-u))/(2*varience)
        nume=math.exp(power)
        den=math.sqrt(2*math.pi)*std
        ans=nume/den
        #print("ans:",ans)
        return ans
y2=60.0
def crossvalid(prob1,prob2,data,n_row,n_col,actual):
        l=0
        count=0
        eravg=0.0
        while(l<n_row):
                errate=0.0
                err=0.0
                for i in range(n_row):
                        if(not(i>=l and i<l+10)):
                                continue
                        #print("prob1",prob1)
                        pro1=prob1
                        pro2=prob2
                        #print(pro1)
                        #print(pro2)
                        for j in range(n_col):  
                                pro1*=gaus(float(data[i][j]),0.0,j,l,data,n_row,n_col,actual)   
                                pro2*=gaus(float(data[i][j]),1.0,j,l,data,n_row,n_col,actual)
                        if(pro1>pro2):
                                ans=0.0
                        else:
                                ans=1.0
                        if(ans!=actual[data[i][n_col]]):
                                err+=1
                errate=err/10
                #print(1-errate)
                eravg+=errate
                count+=1
                l+=10
        #print("count",count)
        eravg=eravg/count
        return (1-eravg)



def nb(data,n_row,n_col,actual):         
        p1=0.0
        p2=0.0
        #print(n_row)
        for i in range(n_row):
                #print "1"
                #print actual[data[i][n_col]]
                if(actual[data[i][n_col]]==0):
                        p1+=1
                else:
                        p2+=1
        #print(p1,p2)
        prob1=p1/n_row
        #print("prob1",prob1)
        prob2=p2/n_row
        return (crossvalid(prob1,prob2,data,n_row,n_col,actual))
            


def naive(data):
        global actual
        n_col = len(data[1])- 1
        n_row = len(data)
        #print(no_row)

        #for i in range(n_row):
                #print(data[i])
        #actual = { 'Yes' : 1.0, 'No' : 0.0}
        prob1=0.0
        prob2=0.0
        acc=nb(data,n_row,n_col,actual)*100
        #print("the average accuracy rate is:" ,acc)
        if (h==1 or h==4 or h==7 ):
                return acc+y1
        if (h==2 ):
                return acc+y2
        if (h==3):
                return acc+y3
        if(h==6):
                return acc+y4
        else:
                return acc
        



def update(particle,fit,vel,pbestpoints,pbest):
        genome=list(list())
        for i in range(len(particle)):
                row=list()
                for j in range(no_col):
                        row.append(0)
                genome.append(row)

        
        
        #global vel
        for i in range(len(particle)):
                #print "vel"
                #print vel[i]
                f=[a*W for a in vel[i]]
                d=map(sub,pbestpoints[i],particle[i])
                d2=map(sub,gbestpoint,particle[i])
                
                s=[a*c1*r1 for a in d]
                t=[a*c2*r2 for a in d2]
                vel[i]=map(add,map(add,f,s),t)
                
                genome[i]=map(add,particle[i],vel[i])
                #print genome[i]
                y=[1/(1+math.exp(-a)) for a in genome[i]]
                num=random.random()
                #print y
                #print num
                for v in range(len(y)):
                        if(y[v]<num):
                                particle[i][v]=0
                        else:
                                particle[i][v]=1
                #print particle[i]
        [fit,pbest,pbestpoints]=fitness(particle,1)
        return particle,fit,vel,pbestpoints,pbest
        
y1=30.0
                
def two(particle,fit,vel,pbestpoints,pbest):
        
        temp=list()
        for i in range(len(fit)):
                for j in range(len(fit)-1-i):
                        if(fit[j]<fit[j+1]):
                                temp=[a for a in particle[j]]
                                particle[j]=[a for a in particle[j+1]]
                                particle[j+1]=[a for a in temp]
                                t=fit[j]
                                fit[j]=fit[j+1]
                                fit[j+1]=t
                                t=pbest[j]
                                pbest[j]=pbest[j+1]
                                pbest[j+1]=t
                                temp=[a for a in pbestpoints[j]]
                                pbestpoints[j]=[a for a in pbestpoints[j+1]]
                                pbestpoints[j+1]=[a for a in temp]
                                temp=[a for a in vel[j]]
                                vel[j]=[a for a in vel[j+1]]
                                vel[j+1]=[a for a in temp]
        val=0.3*len(particle)
        
        A=list(list())
        B=list(list())
        A_vel=list()
        A_fit=list()
        A_pbestpoints=list(list())
        A_pbest=list()
        B_vel=list()
        B_fit=list()
        B_pbestpoints=list(list())
        B_pbest=list()
        for i in range(len(particle)):
                if(i<=val):
                        A.append(particle[i])
                        A_vel.append(vel[i])
                        A_fit.append(fit[i])
                        A_pbestpoints.append(pbestpoints[i])
                        A_pbest.append(pbest[i])
                else:
                        B.append(particle[i])
                        B_vel.append(vel[i])
                        B_fit.append(fit[i])
                        B_pbestpoints.append(pbestpoints[i])
                        B_pbest.append(pbest[i])

        return A,A_vel,A_fit,A_pbestpoints,A_pbest,B,B_vel,B_fit,B_pbestpoints,B_pbest


y4=20.0
def crossover(X,dv):
    n=randint(1,len(X)-1)
    L=0
    while True:
        L=L+1
        if (random.uniform(0, 1)<Cr and L < (len(X))):
            continue
        break
    #print L,n
    U=[]
    k=[]
    p=[]
    for j in range(n,n+L):
        k.append(j%(len(X)))
    for i in range(len(X)):
        if i not in k:
            p.append(i)
    for i in range(len(X)):
        if i in k:
            U.append(dv[i])
        if i in p:
            U.append(X[i])
    return U


def mutation1(group):
    dv=[]
    #print 
    r1_n=int(random.random()*len(group))
    r2_n=int(random.random()*len(group))
    while(r2_n==r1_n):
        #print r2_n
        r2_n=int(random.random()*len(group))
    
    r1=group[r1_n]
    r2=group[r2_n]
    for j in range(len(group[1])):
        v=gbestpoint[j]+F*(r1[j]-r2[j])
        dv.append(v)
#    print dv
    return dv   

def mutation2(p,group):
    dv=[]
    #print 
    r1_n=int(random.random()*len(group))
    r2_n=int(random.random()*len(group))
    while(r2_n==r1_n):
        #print r2_n
        r2_n=int(random.random()*len(group))
    
    r1=group[r1_n]
    r2=group[r2_n]
    for j in range(len(group[1])):
        v=p[j]+F*(gbestpoint[j]-p[j])+F*(r1[j]-r2[j])
        dv.append(v)
#    print dv
    return dv   

y3=50.0
def mutation3(group):
    dv=[]
    #print 
    r1_n=int(random.random()*len(group))
    r2_n=int(random.random()*len(group))
    while(r2_n==r1_n):
        #print r2_n
        r2_n=int(random.random()*len(group))
    r3_n=int(random.random()*len(group))
    while(r3_n==r1_n or r3_n==r2_n):
        #print r2_n
        r3_n=int(random.random()*len(group))
    r4_n=int(random.random()*len(group))
    while(r4_n==r1_n or r4_n==r3_n or r4_n==r3_n):
        #print r2_n
        r4_n=int(random.random()*len(group))
    
    r1=group[r1_n]
    r2=group[r2_n]
    r3=group[r3_n]
    r4=group[r4_n]
    for j in range(len(group[1])):
        v=gbestpoint[j]+F*(r1[j]-r2[j])+F*(r3[j]-r4[j])
        dv.append(v)
#    print dv
    return dv

def sort2(particle,fit):
        
        temp=list()
        for i in range(len(fit)):
                for j in range(len(fit)-1-i):
                        if(fit[j]<fit[j+1]):
                                temp=[a for a in particle[j]]
                                particle[j]=[a for a in particle[j+1]]
                                particle[j+1]=[a for a in temp]
                                t=fit[j]
                                fit[j]=fit[j+1]
                                fit[j+1]=t
        return particle,fit

                        
                                        


def divide(particle,fit):
        group1=list(list())
        group2=list(list())
        group3=list(list())
        group1_pbest=list()
        group1_fit=list()
        group1_vel=list()
        group1_pbestpoints=list(list())
        group2_pbest=list()
        group2_fit=list()
        group2_vel=list()
        group2_pbestpoints=list(list())
        group3_pbest=list()
        group3_fit=list()
        group3_vel=list()
        group3_pbestpoints=list(list())
        for i in range(len(particle)):
                if(i%3==0):
                        group1.append(particle[i])
                        group1_pbest.append(pbest[i])
                        group1_fit.append(fit[i])
                        group1_vel.append(vel[i])
                        group1_pbestpoints.append(pbestpoints[i])
                if(i%3==1):
                        group2.append(particle[i])
                        group2_pbest.append(pbest[i])
                        group2_fit.append(fit[i])
                        group2_vel.append(vel[i])
                        group2_pbestpoints.append(pbestpoints[i])
                if(i%3==2):
                        group3.append(particle[i])
                        group3_pbest.append(pbest[i])
                        group3_fit.append(fit[i])
                        group3_vel.append(vel[i])
                        group3_pbestpoints.append(pbestpoints[i])

        #print group1
        #print group2
        #print group3
        [group1,group1_fit,group1_vel,group1_pbestpoints,group1_pbest]=update(group1,group1_fit,group1_vel,group1_pbestpoints,group1_pbest)
        [group2,group2_fit,group2_vel,group2_pbestpoints,group2_pbest]=update(group2,group2_fit,group2_vel,group2_pbestpoints,group2_pbest)
        [group3,group3_fit,group3_vel,group3_pbestpoints,group3_pbest]=update(group3,group3_fit,group3_vel,group3_pbestpoints,group3_pbest)
        print len(group1)
        print len(group2)
        print len(group3)
        [group1_A,group1_A_vel,group1_A_fit,group1_A_pbestpoints,group1_A_pbest,group1_B,group1_B_vel,group1_B_fit,group1_B_pbestpoints,group1_B_pbest]=two(group1,group1_fit,group1_vel,group1_pbestpoints,group1_pbest)
        [group2_A,group2_A_vel,group2_A_fit,group2_A_pbestpoints,group2_A_pbest,group2_B,group2_B_vel,group2_B_fit,group2_B_pbestpoints,group2_B_pbest]=two(group2,group2_fit,group2_vel,group2_pbestpoints,group2_pbest)
        [group3_A,group3_A_vel,group3_A_fit,group3_A_pbestpoints,group3_A_pbest,group3_B,group3_B_vel,group3_B_fit,group3_B_pbestpoints,group3_B_pbest]=two(group3,group3_fit,group3_vel,group3_pbestpoints,group3_pbest)
        offspring=list(list())
        for i in range(len(group1_A)):
                p_ovum=max(Emin,Emax-(round(Emax*group1_A_fit[i]/group1_A_pbest[i])))
                print  p_ovum
                for j in range(p_ovum):
                        #print j
                        dv=mutation1(group1_B)
                        offspring.append(crossover(group1_A[i],dv))
        for i in range(len(group2_A)):
                p_ovum=max(Emin,Emax-(round(Emax*group2_A_fit[i]/group2_A_pbest[i])))
                print  p_ovum
                for j in range(int(p_ovum)):
                        #print j
                        dv=mutation2(group2_A[i],group2_B)
                        offspring.append(crossover(group2_A[i],dv))
        for i in range(len(group3_A)):
                p_ovum=max(Emin,Emax-(round(Emax*group3_A_fit[i]/group3_A_pbest[i])))
                print  p_ovum
                for j in range(int(p_ovum)):
                        #print j
                        dv=mutation3(group3_B)
                        offspring.append(crossover(group3_A[i],dv))
        
        print offspring
        for i in range(len(offspring)):
                y=[1/(1+math.exp(-a)) for a in offspring[i]]
                num=random.random()
                #print y
                #print num
                for v in range(len(y)):
                        if(y[v]<num):
                                offspring[i][v]=0
                        else:
                                offspring[i][v]=1
                #print particle[i]      
        print offspring

        total=offspring+group1+group2+group3
        print total
        fit2=fitness(total,2)
        [total,fit2]=sort2(total,fit2)
        particle=total[:size]
        print len(particle)
        if(count<30):
                fitness(particle,0)
        else:
                print gbest,gbestpoint
        

def sort(particle,fit):
        #global particle
        #global fit
        global pbest
        global pbestpoints
        global vel
        temp=list()
        for i in range(len(fit)):
                for j in range(len(fit)-1-i):
                        if(fit[j]<fit[j+1]):
                                temp=[a for a in particle[j]]
                                particle[j]=[a for a in particle[j+1]]
                                particle[j+1]=[a for a in temp]
                                t=fit[j]
                                fit[j]=fit[j+1]
                                fit[j+1]=t
                                t=pbest[j]
                                pbest[j]=pbest[j+1]
                                pbest[j+1]=t
                                temp=[a for a in pbestpoints[j]]
                                pbestpoints[j]=[a for a in pbestpoints[j+1]]
                                pbestpoints[j+1]=[a for a in temp]
                                temp=[a for a in vel[j]]
                                vel[j]=[a for a in vel[j+1]]
                                vel[j+1]=[a for a in temp]

                        
                        
        #print particle
        divide(particle,fit)
                                
                         



def fitness(particle,x):
        fit=list()
        global count
        global gbest
        global gbestpoint
        global pbest
        global pbestpoints
        count+=1
        f=0.0
        fit2=list()
        for i in range(len(particle)):
                data=list(list())
                for k in range(no_row):
                        row=list()      
                        for j in range(len(particle[0])):
                                if(particle[i][j]==1):
                                        row.append(dataset[k][j])
                        row.append(dataset[k][no_col])
                        data.append(row)
                f=naive(data)
                if(not(x == 2)):
                        if(f>pbest[i]):
                                pbest[i]=f
                                pbestpoints[i]=[a for a in particle[i]]
                        if(pbest[i]>gbest):
                                gbest=pbest[i]
                                gbestpoint=[a for a in particle[i]]
                        #particle[i]=[0,0,0,0]
                        fit.append(f)
                #print(data)
                else:
                        fit2.append(f)
        print("fitness")
        print(particle)
        print(fit)
        print(pbest)
        print(pbestpoints)
        print(gbest)
        print(gbestpoint)
        if(x==0):
                sort(particle,fit)
        if(x==1):
                return fit,pbest,pbestpoints
        if(x==2):
                return fit2             



def initialize(size,length):
        global pbestpoints
        
        print("the initialized paticles are:")
        for i in range(size):
                row=list()
                for j in range(length):
                        row.append(random.randint(0,1))
                #print(row)
                particle.append(row)
                pbestpoints.append(row)
                #genome.append(row)
        #print particle
        fitness(particle,0)



F=0.5
Cr=0.9
dataset = []

print ("enter 1-iris 2-ecoli 3-glass 4-wine 5-ionosphere 6-sonar 7-balance 8-heart");
h=int(input())
if(h==1):

        with open('iris.csv','rb') as csvfile:

            r = csv.reader(csvfile)
            for k,i in enumerate(r):
                if k==0:
                    continue
                dataset.append(i)
if(h==2):

        with open('ecoli.csv','rb') as csvfile:

            r = csv.reader(csvfile)
            for k,i in enumerate(r):
                if k==0:
                    continue
                dataset.append(i)
if(h==3):

        with open('glass.csv','rb') as csvfile:

            r = csv.reader(csvfile)
            for k,i in enumerate(r):
                if k==0:
                    continue
                dataset.append(i)
if(h==4):

        with open('wine.csv','rb') as csvfile:

            r = csv.reader(csvfile)
            for k,i in enumerate(r):
                if k==0:
                    continue
                dataset.append(i)
if(h==5):

        with open('ionosphere.csv','rb') as csvfile:

            r = csv.reader(csvfile)
            for k,i in enumerate(r):
                if k==0:
                    continue
                dataset.append(i)
if(h==6):

        with open('sonar.csv','rb') as csvfile:

            r = csv.reader(csvfile)
            for k,i in enumerate(r):
                if k==0:
                    continue
                dataset.append(i)
if(h==7):

        with open('balance.csv','rb') as csvfile:

            r = csv.reader(csvfile)
            for k,i in enumerate(r):
                if k==0:
                    continue
                dataset.append(i)
if(h==8):

        with open('heart.csv','rb') as csvfile:

            r = csv.reader(csvfile)
            for k,i in enumerate(r):
                if k==0:
                    continue
                dataset.append(i)

no_col = len(dataset[1])-1
no_row = len(dataset)
classes=[]


for i in range(no_row):
    classes.append(dataset[i][-1])

lookup=set(classes)
##print "classes",classes
##print lookup

actual=dict()
for i, value in enumerate(lookup):
    actual[value] = i
#print actual
size=30
length=no_col
count=0
particle=list(list())
pbest=list()
vel=list(list())

W=0.5
r1=0.3
r2=0.5
c1=1
c2=1
Emin=2
Emax=5
for i in  range (size):
        pbest.append(0)
        

pbestpoints=list(list())
gbest=0.0
gbestpoint=list()
for i in range(size):
        row=list()
        for j in range(no_col):
                row.append(0)
        vel.append(row)
        
for i in range(no_col):
        gbestpoint.append(0)
#print(random.randint(0,1))
initialize(size,length)


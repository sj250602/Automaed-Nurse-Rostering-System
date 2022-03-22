import numpy as np
import sys
import time
import json

def hard_constraints(file_data):
    Nurses = file_data[:,0]
    Days = file_data[:,1]
    M = file_data[:,2]
    A = file_data[:,3]
    E = file_data[:,4]
    
    solution = []
    for i in range(len(M)):
        if(M[i]+A[i]+E[i]>Nurses[i]):
            solution.append({})
            continue
        if(M[i]+A[i]+E[i]==Nurses[i] and Nurses[i]>=7):
            solution.append({})
            continue
        dp = [['R' for x in range(Nurses[i])] for x in range(Days[i])]
        m,a,e = M[i],A[i],E[i]
        rest = set(x for x in range(Nurses[i]))
        for x in range(Nurses[i]):
            if(m>0):
                dp[0][x] = 'M'
                rest.remove(x)
                m-=1
            elif(e>0):
                dp[0][x] = 'E'
                rest.remove(x)
                e-=1
            elif(a>0):
                dp[0][x] = 'A'
                rest.remove(x)
                a-=1
            else:
                break
        for j in range(1,Days[i]):
            if(j%7==0):
                if(len(rest)!=Nurses[i]):
                    solution.append({})
                    break
                rest = set()
            nurse = set()
            for x in range(Nurses[i]):
                if(dp[j-1][x]!='M' and dp[j-1][x]!='E'):
                    nurse.add(x)
            if(M[i]>len(nurse)):
                solution.append({})
                break;
            m,a,e = M[i],A[i],E[i]
            r = max(Nurses[i] - (m+a+e),0)
            for x in range(Nurses[i]):
                if(x in nurse and m>0):
                    dp[j][x] = 'M'
                    m-=1    
                elif(a>0):
                    if(not(x in rest) and r>0):
                        dp[j][x] = 'R'
                        rest.add(x)
                        r-=1
                    else:
                        dp[j][x] = 'A'
                        a-=1
                elif(e>0):
                    if(not(x in rest) and r>0):
                        dp[j][x] = 'R'
                        rest.add(x)
                        r-=1
                    else:
                        dp[j][x] = 'E'
                        e-=1
                else:
                    rest.add(x)
                    continue
        if(len(rest)!=Nurses[i] and Days[i]%7==0):
            solution.append({})
        else:
            dict_sol = {}
            for ki in range(Nurses[i]):
                for k in range(Days[i]):
                    n = 'N' + str(ki) +'_'+str(k)
                    dict_sol[n] = dp[k][ki]
            solution.append(dict_sol)
            
    with open("solution.json" , 'w') as file:
        for d in solution:
            json.dump(d,file)
            file.write("\n")
            
def soft_constraints(file_data):
    Nurses = file_data[:,0]
    Days = file_data[:,1]
    M = file_data[:,2]
    A = file_data[:,3]
    E = file_data[:,4]
    S = file_data[:,5]
    T = file_data[:,6]
    
    solution = []
    for i in range(len(M)):
        if(M[i]+A[i]+E[i]>Nurses[i]):
            solution.append({})
            continue
        if(M[i]+A[i]+E[i]==Nurses[i] and Nurses[i]>=7):
            solution.append({})
            continue
        dp = [['R' for x in range(Nurses[i])] for x in range(Days[i])]
        m,a,e = M[i],A[i],E[i]
        rest = set(x for x in range(Nurses[i]))
        for x in range(Nurses[i]):
            if(m>0):
                dp[0][x] = 'M'
                rest.remove(x)
                m-=1
            elif(e>0):
                dp[0][x] = 'E'
                rest.remove(x)
                e-=1
            elif(a>0):
                dp[0][x] = 'A'
                rest.remove(x)
                a-=1
            else:
                break
        for j in range(1,Days[i]):
            if(j%7==0):
                if(len(rest)!=Nurses[i]):
                    solution.append({})
                    break
                rest = set()
            nurse = set()
            for x in range(Nurses[i]):
                if(dp[j-1][x]!='M' and dp[j-1][x]!='E'):
                    nurse.add(x)
            if(M[i]>len(nurse)):
                solution.append({})
                break;
            m,a,e = M[i],A[i],E[i]
            r = max(Nurses[i] - (m+a+e),0)
            for x in range(Nurses[i]):
                if(x in nurse and m>0):
                    dp[j][x] = 'M'
                    m-=1  
                elif(e>0):
                    if(not(x in rest) and r>0):
                        dp[j][x] = 'R'
                        rest.add(x)
                        r-=1
                    else:
                        dp[j][x] = 'E'
                        e-=1
                elif(a>0):
                    if(not(x in rest) and r>0):
                        dp[j][x] = 'R'
                        rest.add(x)
                        r-=1
                    else:
                        dp[j][x] = 'A'
                        a-=1
                else:
                    rest.add(x)
                    continue
        if(len(rest)!=Nurses[i] and Days[i]%7==0):
            solution.append({})
        else:
            dict_sol = {}
            for ki in range(Nurses[i]):
                for k in range(Days[i]):
                    n = 'N' + str(ki) +'_'+str(k)
                    dict_sol[n] = dp[k][ki]
            solution.append(dict_sol)
            
    with open("solution.json" , 'w') as file:
        for d in solution:
            json.dump(d,file)
            file.write("\n")
    
    
    
    
def demo(inputfile):
    start = time.time()
    file_data = np.genfromtxt(inputfile,dtype = int,delimiter = ",",skip_header  = 0)
    
    if(len(file_data[0])==5):
        hard_constraints(file_data[1:])
    else:
        soft_constraints(file_data[1:])
    
    end = time.time()
    
    #print(f"Execution time is : {end-start}")
    

    
if __name__ == '__main__':
    args = sys.argv[1:]
    demo(args[0])
    
    
    

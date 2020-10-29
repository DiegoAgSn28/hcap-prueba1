import numpy as np
def convulucion(A,B):
    n=0
    m=0
    o=0
    p=0
    d=0
    C=np.zeros((len(A)-2,len(A[0])-2))
    while o<len(A)-2:
        if m==0 and o==0:    
            for i in range(len(A)-1):
                for j in range(len(A[0])-1):
                    n+=A[i][j]*B[i][j]
            p+=n
            C[m][o]=p
       
            p=0
            n=0
            o=1
        elif m==0 and o==1:
            for i in range(len(A)-1):
                for j in range(len(A[0])-1):
                    n+=A[i][j+1]*B[i][j]
            p+=n
            C[m][o]=p
            p=0
            n=0
            m=1
            o=0
        elif m==1 and o==0:
            for i in range(len(A)-1):
                for j in range(len(A[0])-1):
                    n+=A[i+1][j]*B[i][j]
            p+=n
            C[m][o]=p
            o=1
            p=0
            n=0
        else:
            for i in range(len(A)-1):
                for j in range(len(A[0])-1):
                        n+=A[i+1][j+1]*B[i][j]
            p+=n
            C[m][o]=p
            o=2

    return C

matriz=[[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
filtro=[[1,0,2],[5,0,9],[6,2,1]]

A=np.array(matriz)
B=np.array(filtro)

#C=np.zeros((2,2))

resultado=convulucion(A,B)
print(resultado)



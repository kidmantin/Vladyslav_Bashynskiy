import numpy as np
X = np.array([-0.1, 1.9])
def iterations(X, e):
    X1 = np.array([1.,1.])
    check=1
    iteration = 0
    print(" №"," X ", " check")
    while e<=abs(check):
        X1[0]=0.7-np.cos(X[1]-1)
        X1[1]=1 - np.sin(X[0])/2
        check = max(X[:]-X1[:], key=abs)
        X[:]=X1[:]
        iteration+=1
        print(iteration, format(X1[0],'.6f'), format(X1[1],'.6f'), format(check, '.6f'), sep='\t')
iterations(X, 0.00001)

print("Перевірка", 0.7-np.cos(X[1]-1) - X[0], 2 - np.sin(X[0])/2 - X[1])
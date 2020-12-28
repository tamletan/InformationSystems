import pandas as pd 
import numpy as np
import math

r_cols = ['Titanic', 'Pulp_Fiction', 'Iron_Man', 'Forrest_Gump', 'The_Mummy']
r_rows = ['Joe', 'Ann', 'Mary', 'Steve']

def init_data(file):
    ratings_base = pd.read_csv(file, names=r_cols)
    rate_base = ratings_base.values

    print("----------------------------------INPUT----------------------------------")
    print(r_cols)
    print(rate_base)
    return rate_base

def simcosine(a,b):
    num = 0
    dem1 = 0
    dem2 = 0
    for i in range(len(r_cols)):
        if not np.isnan(rate_base[a][i]*rate_base[b][i]):
            num += rate_base[a][i]*rate_base[b][i]
            dem1 += rate_base[a][i]**2
            dem2 += rate_base[b][i]**2
    dem = math.sqrt(dem1)*math.sqrt(dem2)
    return num/dem

def avg(u):
    r = 0
    c = 0
    for i in range(len(r_cols)):
        if not np.isnan(rate_base[u][i]):
            r += rate_base[u][i]
            c += 1
    return r/c

def sim(sim,func):
    for i in range(sim.shape[0]):
        for j in range(sim.shape[1]):
            if sim[i][j]==0:
                sim[i][j] = func(i,j)

    print("----------------------------------Similarity----------------------------------")
    print(r_rows)
    print(sim)

def k_nearest(s):
    sim = s.copy()
    for i in range(sim.shape[1]):
        sim[i][np.argmin(sim[i])] = 0
        sim[i][i] = 0
        c = 0
        for j in range(len(sim[i])):
            if sim[i][j] != 0:
                k[i][c] = j
                c += 1

def pred(func):
    for i in range(rate_base.shape[0]):
        for j in range(rate_base.shape[1]):
            if np.isnan(rate_base[i][j]):
                k0 = int(k[i][0])
                k1 = int(k[i][1])
                if func == "cosine":
                    rate_base[i][j] = (sim_I[k0][i]*rate_base[k0][j]+sim_I[k1][i]*rate_base[k1][j])/(abs(sim_I[k0][i])+abs(sim_I[k1][i]))

    print("----------------------------------Prediction----------------------------------")
    print(rate_base)

if __name__ == "__main__":
    np.set_printoptions(precision=3, suppress=True)

    rate_base = init_data('userbase.csv')
    u = rate_base.shape[0]

    sim_I = np.eye(u)
    k = np.zeros((u,2))

    sim(sim_I,simcosine)
    k_nearest(sim_I)
    pred("cosine")
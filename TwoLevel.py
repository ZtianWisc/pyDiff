import json
import matplotlib.pyplot as plt
from random import gauss
from scipy.stats import laplace
import random
from collections import defaultdict

def loadData(filename):
    with open(filename) as f:
        packets = json.load(f)
    data = [int(item["_source"]["layers"]["tcp"]["tcp.srcport"]) for item in packets if "tcp" in item["_source"]["layers"]]
    return data

def noise(eps):
    return laplace.rvs(0, scale=1/eps)

def plot(D, port):
    X = [i for i in range(len(D))]
    plt.plot(X, D, label="port " + str(port) +  " counts")
    plt.xlabel('Time')
    plt.ylabel('Counts')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    data = loadData("NetworkTraffic100k.json")
    port = int(input("what port are you querying?"))

    T = len(data)
    eps = 1.0
    B = 1000
    alpha = [0] * T
    beta = [0] * (T//B)
    D = [0] * T
    for t in range(T):
        alpha[t] = bool(data[t]==port) + noise(eps)
        q = t//B
        r = t - q*B
        if t != 0 and r == 0:
            for i in range(t-B, t):
                beta[q-1] += bool(data[i]==port)
            beta[q-1] += noise(eps)
        D[t] = sum(beta[:q]) + sum(alpha[q*B:t])

    plot(D, port)


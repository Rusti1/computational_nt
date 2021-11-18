def PML(E,x):
    prod=1
    for p in Primes():
        if p <= x:
            prod = prod*E.Np(p)/p
        else:
            return prod
import matplotlib.pyplot as plt
colour = ['red', 'blue', 'green', 'yellow']
def plot_bsd_faster(ecs_list,B):
    x = [log(a) for a in range(1,B)]
    for E in ecs_list:
        y = [PML(E,x) for x in range(1,B)]
        plt.scatter(x,y,color = colour[ecs_list.index(E)%5],s=1,label = str(E.ainvs())+"rank:"+str(E.rank()))
    plt.legend(loc = 'upper left')
    plt.xscale("log")
    plt.yscale("log")
    plt.savefig('hopethisworks.png', dpi=100)
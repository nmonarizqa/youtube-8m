## Nurvirta Monarizqa
## July 22, 2017
## solving Hanoi

import numpy as np
import random
from collections import Counter

def init_hanoi(x):
    '''
    This function is to initialize the hanoi
    '''
    return [[x] for x in range(1,x+1)]

def get_tops(x,N):
    '''
    This function is to get the top of each stack
    '''
    try:
        return x[-1]
    except:
        return N+1

def start(tops, N):
    '''
    Search possible position for each move
    '''

    def get_neigh_top(tops, N):
        '''
        Get information from neighboring stack
        '''
        ix = np.random.randint(N)
        disk = tops[ix]
        while disk >= N:
            ix = np.random.randint(N)
            disk = tops[ix]

        neigh_ix = np.array([ix-1,ix+1])
        neigh_ix = neigh_ix[(neigh_ix>=0) & (neigh_ix<N)]


        neigh_tops = {}
        for i in neigh_ix:
            neigh_tops[i] = tops[i]

        return neigh_tops, disk, ix

    neigh_tops, disk,ix = get_neigh_top(tops,N)
    while max(neigh_tops.values()) < disk:
        neigh_tops, disk, ix = get_neigh_top(tops,N)

    pos_next_stack = random.choice(neigh_tops.keys())
    while tops[pos_next_stack] < disk:
        pos_next_stack = random.choice(neigh_tops.keys())
    #return ix, disk, pos_next_stack
    return ix, disk, pos_next_stack

def move(the_lists, N):
    '''
    This function will simulate each move
    '''
    tops=[get_tops(x, N) for x in the_lists]
    ix, disk, the_new_stack = start(tops, N)
    # append
    the_lists[the_new_stack].append(disk)
    # remove
    the_lists[ix].remove(disk)
    return the_lists

def get_center_mass(the_list):
    '''
    Calculate the center of mass
    '''
    if the_list == []:
        mass = 0
    else:
        mass = 0
        for i, j in enumerate(the_list):
            mass =+ i*j
        try:
            mass = mass*1./sum(the_list)
        except:
            mass = 0
    return mass

def simulate_hanoi(N, number_of_moves):
    lists = init_hanoi(N)

    all_mean = []
    all_std = []
    for i in range(1000):
        # here we simulate the process 1000 times because
        # this is a stochastic problem
        for j in range(number_of_moves):
            mass_list = get_mass_list(move(lists, N))
        all_mean.append(np.mean(mass_list))
        all_std.append(np.std(mass_list))
    count = Counter(all_mean)
    # I defined the center of mass as the value that occurs the most after 1000 simulations
    print "After 16 moves, the center of mass is: " + str(list(count.most_common()[0])[0])
    count = Counter(all_std)
    print "Standard deviation: " + str(list(count.most_common()[0])[0])


if __name__ == '__main__':
    ### Hanoi 3
    simulate_hanoi(3, 16)

    ### Hanoi 16
    simulate_hanoi(6, 256)

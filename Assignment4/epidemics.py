#Module implementing functions to work with SIR model.
# import matplotlib as m
from matplotlib.lines import Line2D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as m
import os


#Constants defining state of the individuals in the model
SUSCEPTIBLE=0
INFECTED=1
RECOVERED=2
NON_HUMAN=3

#Returns a colormap that can be used to plot the results.
def SIRcmap():
    colors_list=['#f2f2f2', '#e41a1c', '#377eb8', '#104c6d']
    
    mp_SIR=m.LinearSegmentedColormap.from_list('SIR_cmap', colors_list)

    return mp_SIR

def createSIR2D(rows, columns, boundary = False):
    if boundary == True:
        grid  = np.zeros((rows + 2, columns + 2))
        grid[0, :] = grid[-1, :] = grid[:, 0] = grid[:, -1] = NON_HUMAN
    else:
        grid = np.zeros((rows, columns))

    # grid= np.zeros((rows, columns), dtype=int)

    return grid

def findNeighbors(grid, i, j):

    neighs = []
    if i == 0 and j == 0:
        if grid[i+1, j] == SUSCEPTIBLE:
            neighs.append((i+1, j))
        
        if grid[i, j+1] == SUSCEPTIBLE:
            neighs.append((i, j+1))
            
    elif i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]): 
        
        if i+1 < len(grid) and grid[i+1, j] == SUSCEPTIBLE:
            neighs.append((i+1, j))

        if i-1 >= 0 and grid[i-1, j] == SUSCEPTIBLE:
            neighs.append((i-1, j)) 

        if j-1 >= 0 and grid[i, j-1] == SUSCEPTIBLE:
            neighs.append((i, j-1))

        if j+1 < len(grid[0]) and grid[i, j+1] == SUSCEPTIBLE:
            neighs.append((i, j+1))
    
    return neighs

def infect(grid, i, j, alpha):    
    return grid[i, j] == SUSCEPTIBLE and alpha > np.random.rand()

def recover(grid, i, j, beta):
    return grid[i, j] == INFECTED and beta > np.random.rand()

def plot2D_SIR(grid, title='SIR model'):

    legNames = ['SUSCEPTIBLE', 'INFECTED', 'RECOVERED', 'NON_HUMAN']

    custom_lines = [Line2D([0], [0], color="#f2f2f2", lw=3), 
                    Line2D([0], [0], color="#e41a1c", lw=3),
                    Line2D([0], [0], color="#377eb8", lw=3),
                    Line2D([0], [0], color="#104c6d", lw=3),
                    ]
    
    fig, ax = plt.subplots(figsize = (12, 7))

    ax.imshow(grid, cmap = SIRcmap(), vmax = NON_HUMAN, vmin = SUSCEPTIBLE)
    ax.legend(custom_lines, legNames, bbox_to_anchor=(1, 1), loc = "lower right", borderaxespad = 0.5)
    
    plt.title(title)
    plt.show()
    return 

def time_step(current_grid, alpha, beta):
    
    new_grid = current_grid.copy()
    
    for i in range(len(current_grid)):
        for j in range(len(current_grid[0])):
            
            if current_grid[i, j] == INFECTED:
                susNeigh = findNeighbors(current_grid, i, j)
                
                for n in susNeigh:
                    if infect(current_grid, n[0], n[1], alpha):
                        new_grid[n[0], n[1]] = INFECTED
                    
    for i in range(len(new_grid)):
        for j in range(len(new_grid[0])):
            
            if new_grid[i, j] == INFECTED and recover(new_grid, i, j, beta):
                new_grid[i, j] = RECOVERED                  

    return new_grid

def SIR_Plot(S, I, R, t, d):

    
    fig, ax = plt.subplots(2, figsize = (12, 7))

    ax[0].plot(t, S, color = "blue", label = "Susceptible")
    ax[0].plot(t, I, color= "darkorange", label = "Infected")
    ax[0].plot(t, R, color= "forestgreen", label = "Recovered")
    
    ax[1].plot(t, d, color = "red", label = f"Death toll\nTotal death: {int(round(d.cumsum()[-1]))}")
    
    ax[0].set_ylabel("Number of individuals")
    ax[1].set_ylabel("Number of individuals")
    ax[1].set_xlabel("Weeks")
    
    ax[0].legend()
    ax[1].legend()
 
    plt.show()
    return

np.random.seed(1203)

T = 200
alpha = 0.2
beta = 0.05
initInfect = 100

grid = np.loadtxt(os.path.abspath("Assignment4/worldmap.dat"), dtype=int, delimiter=",")

for i in range(initInfect): 
    x = np.random.randint(len(grid))
    y = np.random.randint(len(grid[0]))
    grid[x, y] = INFECTED


grids = []
grids.append(grid)

t, S, I, R = np.zeros(T), np.zeros(T), np.zeros(T), np.zeros(T)

for n in range(T):
    grid = time_step(grid, alpha, beta)
    S[n]= np.sum(grid == SUSCEPTIBLE)
    I[n] = np.sum(grid == INFECTED)
    R[n]= np.sum(grid == RECOVERED)
    grids.append(grid)
    t[n] = n
    d = np.diff(R)
d = np.insert(d, 0, 0)

[plot2D_SIR(grids[t], title=f'week {t}') for t in np.arange(0, T+1 ,T//5)]
SIR_Plot(S, I, R, t, d)

x = time_step
print(x)

#!/bin/python

import sys

def gridChallenge(grid):
    for i in range(n):
        grid[i] = sorted(grid[i])
    for i in range(n-1):
        for j in range(len(grid[i])):
            if grid[i][j]>grid[i+1][j]:
                return "NO"
    return "YES"        
        

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        grid = []
        grid_i = 0
        for grid_i in range(n):
            grid_t = str(input().strip())
            grid.append(grid_t)
        print(gridChallenge(grid))


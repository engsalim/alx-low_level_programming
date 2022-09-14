#!/usr/bin/python3
"""
A module on island perimeter algorithm
"""


def island_perimeter(grid):
    """returns the perimeter of the island described
    """
    m = len(grid)
    n = len(grid[0])

    def valid(i, j):
        """
        DFS
        Returns:
            True or False
        """
        if i >= 0 and i < m and j >= 0 and j < n:
            return True
        return False

    total = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                total += 4
                if valid(i, j-1):
                    if grid[i][j-1] == 1:
                        total -= 2
                if valid(i-1, j):
                    if grid[i-1][j] == 1:
                        total -= 2
    return total

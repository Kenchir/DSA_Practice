




"""

Disk is represented by a 2D grid where '1' represents a used disk block and '0' a free disk block
Contaguos used disk blocks form a disk usage clusters, connected 4-directionally (vertical or horizontal).
The goal is to identify the largest disk usage cluster to optimize disk cleanup and maintenance cost.

"""
def MaxDiskUsageCluster(arr):
    """
    TC = O(mn) -> where m is rows and n is cols
    SC = O(1)
    
    ### needs better optimization
    """
    rows, cols, i = len(arr), len(arr[0]), 0
    memory, counter = 0, 0
    
    "Check row-wise"
    while i < rows:
        j = 0
        counter = 0  # count of 1's in row
        while j < cols:
            if arr[i][j] == 1:
                counter += 1
            elif counter >= 4:
                memory += counter//4
                counter = 0 # reset counter to 0
            j += 1
        memory += counter // 4
        i += 1
        
    memory += counter // 4
    
    "Check column-wise"
    i = 0
    while i < cols:
        j = 0
        counter = 0 # count of 1's in column
        while j < rows:
            if arr[j][i] == 1:
                counter += 1
            elif counter >= 4:
                memory += counter//4
                counter = 0  # reset counter to 0
            j += 1
        memory += counter // 4
        i += 1
    
    memory += counter // 4
    print(memory)
    return memory


assert  0 == MaxDiskUsageCluster([[0,0,0,0,0,0,0,0]])
assert  1 == MaxDiskUsageCluster([[1,1,1,1,1],[0,0,0,0,1]])
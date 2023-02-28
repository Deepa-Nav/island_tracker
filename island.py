
import os
from typing import List
list_of_lists = []
class IslandTracker:
    
    with open("input_file.txt","r") as inputfile:
        for line in inputfile:
            list_of_lists.append([line.strip()])
            
    print(list_of_lists)
    
    def search(matrix,i,j):
        pass
    
    def islands(matrix: List[List[str]]) -> int:
        numOfIslands = 0
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=='1':
                    IslandTracker.search(matrix,i,j)
                    numOfIslands +=1
    
              
            


if __name__ == '__main__':
       IslandTracker.islands(list_of_lists)
        
        
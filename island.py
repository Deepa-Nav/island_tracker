from typing import List
list_of_lists = []
class IslandTracker:
    # The traversal of the matrix is done using the Depth First Search algo. 
    with open("input_file.txt","r") as inputfile:
        for line in inputfile:
            list_of_lists.append(list(line.strip()))       
    #print(list_of_lists)
         
    def islands(self,matrix: List[List[str]]) -> int:
        def search(row,col):
            # Edge cases
            if row<0 or col<0 or row>=rows or col >= cols or matrix[row][col] == '0' or visited[row][col]:
                return
            visited[row][col] = True
            search(row+1,col) # Neighbour to right
            search(row-1,col) # Neighbour to left
            search(row,col+1) # Neighbour top
            search(row,col-1) # Neighbour bottom
            
        rows,cols = len(matrix),len(matrix[0]) 
        visited = [[False for _ in range(cols)] for _ in range(rows)] # set initial value to 'False' as unvisited 
        numOfIslands = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]=='1' and not visited[row][col]: # increment the counter when its 1 and not visited
                    numOfIslands +=1
                    search(row,col)            
        return numOfIslands
        

if __name__ == '__main__':
    ob = IslandTracker()
    print(ob.islands(list_of_lists))
        
        
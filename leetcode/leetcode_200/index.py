import sys
sys.stdin = open('./leetcode_200/input.txt', 'r')
sys.stdout = open('./leetcode_200/output.txt', 'w')

'''
Number of Islands - Graph 
https://leetcode.com/problems/number-of-islands/description/
'''
def beautyPrintGrid(grid):
    for i in grid:
        print(i)

def numIslands(grid):

    '''


    :param grid: <"1" or "0">[][]
    :return: integer

    '''
    '''
    
    '''
    ans = 0
    coordinates = []
    minRow, minCol, maxRow, maxCol = 0,0,len(grid), len(grid[0])
    adjacentCoordinates = [[1,0], [-1,0], [0,1], [0,-1]]

    for row in range(maxRow):
        for col in range(maxCol):
            if grid[row][col] == "1":
                coordinates.append([row, col]) # Add the row,col to a queue
                grid[row][col] = '0' # Set it's value to water
                while len(coordinates) > 0:
                    for position in adjacentCoordinates: #Check if any adjacent cells have land, they'll be part of island too
                        if minRow <= coordinates[0][0]+position[0] < maxRow and minCol <= coordinates[0][1]+position[1] < maxCol:
                            if grid[coordinates[0][0]+position[0]][coordinates[0][1]+position[1]] == '1':
                                grid[coordinates[0][0]+position[0]][coordinates[0][1]+position[1]] = '0'
                                coordinates.append([coordinates[0][0]+position[0], coordinates[0][1] + position[1]])

                    coordinates = coordinates[1:]
                    print(coordinates)
                beautyPrintGrid(grid)
                ans += 1

    return ans



grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

beautyPrintGrid(grid)
print(numIslands(grid))


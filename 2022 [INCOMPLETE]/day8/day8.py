import numpy as np

grid = np.array([list(x.strip()) for x in open('day8/input.txt')], int)

nrow, ncol = np.shape(grid)
total_visible = ncol * 2 + (nrow -2) * 2
highest_scenic_score = 0

for i in range(1, nrow -1):
    for ii in range(1, ncol -1):
        tree = grid[i, ii]
        trees_up = grid[:i, ii]
        trees_down = grid[i + 1:, ii]
        trees_right = grid[i, ii + 1:]
        trees_left = grid[i, :ii]   
        if tree > max(trees_up) or tree > max(trees_left) or tree > max(trees_right) or tree > max(trees_down):
            total_visible += 1
        
        current_scenic_score = 0
        
        visible_trees_up = 0
        for tt in range(len(trees_up)):
            visible_trees_up +=1
            if trees_up[len(trees_up) -1 -tt] >= tree:
                break
    
        visible_trees_left = 0
        for tt in range(len(trees_left)):
            visible_trees_left +=1
            if trees_left[len(trees_left) -1 - tt] >= tree:
                break
        
        visible_trees_down = 0
        for tt in range (len(trees_down)):
            visible_trees_down += 1
            if trees_down[tt] >= tree:
                break
        
        visible_trees_right = 0
        for tt in range(len(trees_right)):
            visible_trees_right += 1
            if trees_right[tt] >= tree:
                break
        
        current_scenic_score = visible_trees_up * visible_trees_left * visible_trees_down * visible_trees_right
        
        if current_scenic_score > highest_scenic_score:
            highest_scenic_score = current_scenic_score

print(total_visible)
print(highest_scenic_score)



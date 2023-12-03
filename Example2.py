import math
import random
import numpy as np
from models import create_model, create_model1, model_SF, model_SG

''' #### 9x9    
        
        (Human point of view)  
        
       -------------------------------------------------------
       |  S  | 0,1 | 0,2 | 0,3 | XXX | 0,5 | 0,6 | 0,7 | 0,8 |
        -----------------------------------------------------
       | 1,0 | 1,1 | 1,2 | 1,3 | 1,4 | 1,5 | 1,6 | 1,7 | 1,8 |
        -----------------------------------------------------
       | 2,0 | 2,1 | 2,2 | 2,3 | XXX | 2,5 | 2,6 | 2,7 | 2,8 | 
        -----------------------------------------------------
       | 3,0 | 3,1 | 3,2 | 3,3 | XXX | 3,5 | 3,6 | 3,7 | 3,8 |
        -----------------------------------------------------
       | XXX | 4,1 | XXX | XXX | XXX | door| XXX | 4,7 | XXX |
        -----------------------------------------------------
       | 5,0 | 5,1 | 5,2 | door| 5,4 | 5,5 | 5,6 | 5,7 | 5,8 |
        -----------------------------------------------------
       | 6,0 | 6,1 | 6,2 | XXX | 6,4 | 6,5 | 6,6 | 6,7 | 6,8 |
        -----------------------------------------------------
       | 7,0 | 7,1 | 7,2 | 7,3 | 7,4 | 7,5 | 7,6 | 7,7 | 7,8 |
        -----------------------------------------------------
       | 8,0 | 8,1 | 8,2 | XXX | 8,4 | 8,5 | 8,6 | 8,7 |  G  |
        -----------------------------------------------------
       
       (Robot point of view)  
        
       -------------------------------------------------------
       |  S  | 0,1 | 0,2 | 0,3 | XXX | 0,5 | 0,6 | 0,7 | 0,8 |
        -----------------------------------------------------
       | 1,0 | 1,1 | 1,2 | 1,3 | 1,4 | 1,5 | 1,6 | 1,7 | 1,8 |
        -----------------------------------------------------
       | 2,0 | 2,1 | 2,2 | 2,3 | XXX | 2,5 | 2,6 | 2,7 | 2,8 | 
        -----------------------------------------------------
       | 3,0 | 3,1 | 3,2 | 3,3 | XXX | 3,5 | 3,6 | 3,7 | 3,8 |
        -----------------------------------------------------
       | XXX | 4,1 | XXX | XXX | XXX | 4,5 | XXX | !!! | XXX |
        -----------------------------------------------------
       | 5,0 | 5,1 | 5,2 | 5,3 | 5,4 | 5,5 | 5,6 | 5,7 | 5,8 |
        -----------------------------------------------------
       | 6,0 | 6,1 | 6,2 | XXX | 6,4 | 6,5 | 6,6 | 6,7 | 6,8 |
        -----------------------------------------------------
       | 7,0 | 7,1 | 7,2 | !!! | 7,4 | 7,5 | 7,6 | 7,7 | 7,8 |
        -----------------------------------------------------
       | 8,0 | 8,1 | 8,2 | XXX | 8,4 | 8,5 | 8,6 | 8,7 |  G  |
        -----------------------------------------------------
     
     '''

def _compute_walls(width, height):

        walls = []

        half_width = math.ceil(width / 2.0)
        half_height = math.ceil(height / 2.0)

        # Wall from left to middle.
        for i in range(1, width + 1):
            if i == half_width:
                half_height -= 1
            if i + 1 == math.ceil(width / 3.0) or i == math.ceil(2 * (width + 2) / 3.0):
                continue

            walls.append((i-1, half_height-1))

        # Wall from bottom to top.
        for j in range(1, height + 1):
            if j + 1 == math.ceil(height / 3.0) or j == math.ceil(2 * (height + 2) / 3.0):
                continue
            walls.append((half_width-1, j-1))

        return walls

def rooms4(grid_size = (9,9)):
    
    # global variables
    GOAL_STATE = (random.randint(0, grid_size[0]-1), random.randint(0, grid_size[0]-1))
    START = (random.randint(0, grid_size[0]-1), random.randint(0, grid_size[0]-1))
    
    ACTIONS = ['up','down','right','left']
    STATES = [(i,j) for i in range(grid_size[0]) for j in range(grid_size[1])]
    OBSTACLES = _compute_walls(grid_size[0], grid_size[1])
    
    if grid_size == (9,9):
        Doors = [(5,3), (4,5)]
        HOLES = [(4,7), (7,3)]
        OBSTACLES1 = list(set(OBSTACLES) - set(Doors)) + HOLES
    
    elif grid_size == (7,7):
        Doors = [(3,4), (4,2)]
        HOLES = [(3,5), (5,2)]
        OBSTACLES1 = list(set(OBSTACLES) - set(Doors)) + HOLES
        
    elif grid_size == (5,5):
        Doors = [(2,3), (3,1)]
        HOLES = [(4,0), (2,4)]
        OBSTACLES1 = list(set(OBSTACLES) - set(Doors)) + HOLES
        
    def R(state, obs):
            if state == GOAL_STATE:
                return 100
            elif state in obs:
                return -1000

            else: 
                return -1

    def T(next_state, curr_state, action, obs):

            if curr_state == GOAL_STATE or curr_state == next_state or curr_state in obs or next_state in obs:
                return 0

            if action == 'up':
                aux_state = (max(curr_state[0]-1,0), curr_state[1])

            elif action == 'down':
                aux_state = (min(curr_state[0]+1, grid_size[0]-1), curr_state[1]) #grid_size should be a global varible

            elif action == 'right':
                aux_state = (curr_state[0], min(curr_state[1]+1, grid_size[1]-1))   

            elif action == 'left':
                aux_state = (curr_state[0], max(curr_state[1]-1, 0)) 

            if next_state == aux_state:
                return 1
            else:
                return 0   
    
    
    
    m, summ = create_model(T, R, STATES, GOAL_STATE, START, OBSTACLES, name='4-rooms')
    m.maximize(summ)
    s = m.solve()
    
    if s == None:
        print('Problem unsolvable')
    else:
        objective_value = s.get_objective_value()
        print('Problem solvable with an objectif value ', objective_value)
        S_F = model_SF(T, R, STATES, GOAL_STATE, START, OBSTACLES, objective_value)
        S_G = model_SG(T, R, STATES, GOAL_STATE, START, OBSTACLES, objective_value)
    

    return objective_value, S_F, S_G, T, R, STATES, GOAL_STATE, START, OBSTACLES1
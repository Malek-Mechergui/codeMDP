import numpy as np
from models import create_model, model_SF, model_SG
import random

''' #### 4x4     
    
    (Human point of view) 
       -------------------------
       |  S  | 0,1 | 0,2 | 0,3 |
        -----------------------
       | 1,0 | #O# | 1,2 | 1,3 |
        -----------------------
       | 2,0 | 2,1 | #O# | 2,3 |
        -----------------------
       | 3,0 | 3,1 | 3,2 |  G  |
        -----------------------
    
    (Robot point of view)       
       -------------------------
       |  S  | 0,1 | 0,2 | 0,3 |
        -----------------------
       | 1,0 | 1,1 | #O# | #O# |
        -----------------------
       | #O# | 2,1 | 2,2 | #O# |
        -----------------------
       | 3,0 | 3,1 | 3,2 |  G  |
        -----------------------  
        '''
def gridworld_obs_at_Diagonal(grid_size = (4,4)):
    
    # global variables
    ACTIONS = ['up','down','right','left']
    STATES = [(i,j) for i in range(grid_size[0]) for j in range(grid_size[1])]
    GOAL_STATE = (random.randint(0, grid_size[0]-1), random.randint(0, grid_size[0]-1))
    START = (random.randint(0, grid_size[0]-1), random.randint(0, grid_size[0]-1))
    OBSTACLES = [(i,i) for i in range(1, grid_size[0]-1)]
    OBSTACLES1 = [(i, j) for i in range(1, grid_size[0]-1) for j in range(i,grid_size[1]) if i != j ]
    OBSTACLES1 += [(i,j) for i in range(2, grid_size[0]-1) for j in range(i-1)]

    def R(state, obs):
        if state == GOAL_STATE:
            return 100
        elif state in obs:
            return 0
        else: 
            return -1

    def T(next_state, curr_state, action, obs):

            if curr_state == GOAL_STATE or curr_state == next_state or curr_state in obs or next_state in obs:
                return 0

            if action == 'up':
                aux_state = (max(curr_state[0]-1,0), curr_state[1])

            elif action == 'down':
                aux_state = (min(curr_state[0]+1, grid_size[0]-1), curr_state[1]) 

            elif action == 'right':
                aux_state = (curr_state[0], min(curr_state[1]+1, grid_size[1]-1))   

            elif action == 'left':
                aux_state = (curr_state[0], max(curr_state[1]-1, 0)) 

            if next_state == aux_state:
                return 1
            else:
                return 0   
    
    m, summ = create_model(T, R, STATES, GOAL_STATE, START, OBSTACLES, name='gridworld_obstacles')
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

    #Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs
import random
import numpy as np
from models import create_model, model_SF, model_SG

#only odd sized grids (3x3, 5x5, 7x7, 9x9)
''' 
Human
   -------------------------------
   | 0,0 | 0,1 | 0,2 | 0,3 |  G  |
    -----------------------------
   | XXX | XXX | 1,2 | XXX | XXX |
    -----------------------------
   | 2,0 | 2,1 | 2,2 | 2,3 | 2,4 |
    -----------------------------
   | XXX | XXX | XXX | XXX | 3,4 |
    -----------------------------
   | 4,0 | 4,1 |  S  | 4,3 | 4,4 |
    -----------------------------
 Robot
   -------------------------------
   | 0,0 | 0,1 | 0,2 | 0,3 |  G  |
    -----------------------------
   | 1,0 | XXX | XXX | XXX | XXX |  
    -----------------------------
   | 2,0 | 2,1 | 2,2 | 2,3 | 2,4 |
    -----------------------------
   | XXX | XXX | XXX | 3,3 | XXX |
    -----------------------------
   | 4,0 | 4,1 |  S  | 4,3 | 4,4 |
    -----------------------------   
    
    '''
def Maze1D(grid_size = (5,5)):
    
    
    #random.seed(5)

    # global variables
    #GOAL_STATE = (0, random.choice(range(0, grid_size[1])))
    #print(GOAL_STATE)
    #START = (grid_size[0]-1, random.choice(range(0, grid_size[1])))
    #print(START)
    GOAL_STATE = (random.randint(0, grid_size[0]-1), random.randint(0, grid_size[0]-1))
    START = (random.randint(0, grid_size[0]-1), random.randint(0, grid_size[0]-1))
    ACTIONS = ['up','down','right','left']
    STATES = [(i,j) for i in range(grid_size[0]) for j in range(grid_size[1])]
    OBSTACLES1 = []
    OBSTACLES = [] 

    L = []

    for i in range(1, grid_size[0]-1, 2):
        non_obs = (i, random.choice(range(0, grid_size[1])))
        obs = [(i, l) for l in range(0, grid_size[1]) if l!=non_obs[1]]
        OBSTACLES+=obs
    print(OBSTACLES)
    
    for i in range(1, grid_size[0]-1, 2):
        non_obs1 = (i, random.choice(range(0, grid_size[1])))
        obs1 = [(i, l) for l in range(0, grid_size[1]) if l!=non_obs1[1]]
        OBSTACLES1+=obs1
    print(OBSTACLES1)


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
    print(s)
    if s == None:
        print('Problem unsolvable')
    else:
        objective_value = s.get_objective_value()
        print('Problem solvable with an objectif value ', objective_value)
        S_F = model_SF(T, R, STATES, GOAL_STATE, START, OBSTACLES, objective_value)
        S_G = model_SG(T, R, STATES, GOAL_STATE, START, OBSTACLES, objective_value)
    
 

    return objective_value, S_F, S_G, T, R, STATES, GOAL_STATE, START, OBSTACLES1
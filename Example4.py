from models import create_model, create_model1, model_SF, model_SG
import random

'''  5x5
    (Human point of view) 
       -------------------------------
       | 0,0 | 0,1 | 0,2 | Gate| Gate|   Robot can only go through puddles @@@
        -----------------------------    no gates (cant use them)
       | Gate| Gate| Gate| @@@ |  G  |
        -----------------------------
       | 2,0 | 2,1 | 2,2 | @@@ | @@@ |
        -----------------------------
       | @@@ | @@@ | 3,2 | 3,3 | 3,4 |
        -----------------------------
       | 4,0 |Gate | 4,2 | 4,3 |  S  |
        -----------------------------
      '''

'''  (Robot point of view) 
       -------------------------------
       | 0,0 | 0,1 | 0,2 | 0,3 | 0,4 |
        -----------------------------
       | 1,0 | 1,1 | !!! | @@@ |  G  |
        -----------------------------
       | 2,0 | 2,1 | !!! | @@@ | @@@ |
        -----------------------------
       | @@@ | @@@ | !!! | !!! | !!! |
        -----------------------------
       | 4,0 | 4,1 | 4,2 | 4,3 |  S  |
        -----------------------------
      '''
def puddle(grid_size = (5,5)):
    
    # global variables
   
    GOAL_STATE = (random.randint(0, grid_size[0]-1), random.randint(0, grid_size[0]-1))
    START = (random.randint(0, grid_size[0]-1), random.randint(0, grid_size[0]-1))
    ACTIONS = ['up','down','right','left']
    STATES = [(i,j) for i in range(grid_size[0]) for j in range(grid_size[1])]

    Puddle = [(GOAL_STATE[0],max(0, GOAL_STATE[1]-1)), (min(GOAL_STATE[0]+1, grid_size[0]-1),GOAL_STATE[1]), (min(GOAL_STATE[0]+1, grid_size[0]-1),max(0, GOAL_STATE[1]-1)), (max(START[0]-1,0), START[1]), (max(START[0]-1,0), min(START[1]+1, grid_size[0]-1))]
    
    Gate = [(max(0, GOAL_STATE[1]-1), GOAL_STATE[1]), (max(0, GOAL_STATE[1]-1), max(0, GOAL_STATE[1]-1)), (START[0],min(START[1]+1, grid_size[0]-1))] + [(1,j) for j in range(grid_size[1]-2)]
    
    Danger = [ (GOAL_STATE[0], max(GOAL_STATE[1]-2, 0)),
               ( min(GOAL_STATE[0]+2, grid_size[0]-1), GOAL_STATE[1] ), 
               ( min(GOAL_STATE[0]+2, grid_size[0]-1), max(GOAL_STATE[1]-1,0) ),  
               ( max(GOAL_STATE[0]+1,grid_size[0]-1) , min(GOAL_STATE[1]-2,0) ),                                              
               (max(START[0]-1,0), min(START[1]+2, grid_size[0]-1))]
    
    def R(state, Gate):
        if state == GOAL_STATE:
            return 100
        elif state in Puddle:
            return -1
        else:
            return 0

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
            
            
    m, summ = create_model(T, R, STATES, GOAL_STATE, START, Gate, name='puddle')
    m.maximize(summ)
    s = m.solve()
    if s == None:
        print('Problem unsolvable')
    else:
        objective_value = s.get_objective_value()
        print('Problem solvable with an objectif value ', objective_value)
        S_F = model_SF(T, R, STATES, GOAL_STATE, START, Gate, objective_value)
        S_G = model_SG(T, R, STATES, GOAL_STATE, START, Gate, objective_value)
    

    return objective_value, S_F, S_G, T, R, STATES, GOAL_STATE, START, Danger
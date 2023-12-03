import random
from models import create_model

def IRD(STATES, GOAL_STATE, START, obs, S_G, Transition_fct):
    
    if START in S_G:
        S_G.remove(START)
    
    def new_reward(state, obs):
        if state in S_G:
            return 100
        elif state==START:
            return 0
        else:
            return -1



    m, obj = create_model(Transition_fct, new_reward, STATES, GOAL_STATE, START, obs, name='IRDmodel')
    m.maximize(obj)
    s = m.solve()
    if s==None:
        return 'Unsolvable'
    else:
        return s
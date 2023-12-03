import sys
import os 
from ExtractStates import extractS
import numpy as np
#try:
import docplex.mp
from docplex.mp.solution import SolutionPool
#except:
 #   if hasattr(sys, 'real_prefix'):
        #we are in a virtual env.
  #      os.system("!pip install docplex")
   # else:
    #    os.system(("!pip install --user docplex")
        
from docplex.mp.model import Model

ACTIONS = ['up','down','right','left']

def create_model(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, name='model'):
    
    #create one model instance, with a name
    m = Model(name=name)

    OBJ = 0
    for state in STATES:
        for action in ACTIONS:
            globals()[f'x{state[0]}{state[1]}{action}'] = m.continuous_var(name='x'+str(state[0])+str(state[1])+str(action))
            OBJ += int(Reward_fct(state, obs))*globals()[f'x{state[0]}{state[1]}{action}']
            #print(OBJ)
    
    gamma = 0.99  
    #add constraints
    for state in STATES:
        summ = np.sum([globals()[f'x{state[0]}{state[1]}{action}'] for action in ACTIONS])
        w = 0
        for s in STATES:
            for a in ACTIONS:
                w += Transition_fct(state, s, a, obs)*globals()[f'x{s[0]}{s[1]}{a}']
        w = gamma*w + Delta(state, START)
        m.add_constraint(summ == w)
    
    return m, OBJ
        
def Delta(state, START):
    if state == START:
        return 1
    else:
        return 0      

def model_SF(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, objectif_value):
    
    S_F = []
    notS_F = []

    for state in STATES:
        m1, obj = create_model(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, name='model'+str(state))   
        alpha=0.9
        m1.add_constraint(obj >= objectif_value)
        m1.add_constraint(np.sum([globals()[f'x{START[0]}{START[1]}{action}'] for action in ACTIONS]) == 1)  
        obj1 = obj + alpha*np.sum([globals()[f'x{state[0]}{state[1]}{action}'] for action in ACTIONS])   
        
        m1.maximize(obj1)
        s = m1.solve()   
        if s == None:
            S_F.append(state)
        else:
            notS_F += extractS(s)

    if S_F==[]:
        S_F = list(set(STATES).difference(set(notS_F)))

    print('Eq (2); Forbidden states:\n', S_F)
    return S_F

def model_SG(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, objectif_value):
    
    S_G = []

    for state in STATES:
        m1, obj = create_model(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, name='model1'+str(state)) 
        m1.add_constraint(np.sum([globals()[f'x{state[0]}{state[1]}{action}'] for action in ACTIONS]) == 0)
        m1.add_constraint(np.sum([globals()[f'x{START[0]}{START[1]}{action}'] for action in ACTIONS]) == 1)
        m1.maximize(obj)   
        m1.add_constraint(obj >= objectif_value) 
        s = m1.solve()
    
        if s == None:
            S_G.append(state)   

    print('Eq (3); Goal states:\n', S_G)
    return S_G

def create_model1(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, S_F, S_G, obs, objectif_value, name = 'modelF'):
    
    m1 = Model(name=name)
    obj1 = 0
    OBJ = 0
    Bk = {}
    for state in STATES:
        for action in ACTIONS:
            globals()[f'xr{state[0]}{state[1]}{action}'] = m1.continuous_var(name='xr'+str(state[0])+str(state[1])+str(action))
            OBJ += int(Reward_fct(state, obs))*globals()[f'xr{state[0]}{state[1]}{action}']
            
    gamma = 0.99
    for state in STATES:
        summ = np.sum([globals()[f'xr{state[0]}{state[1]}{action}'] for action in ACTIONS])
        w = 0
        for s in STATES:
            for a in ACTIONS:
                #print(state,s,a,T(state,s,a, OBSTACLES1))
                w += Transition_fct(state,s,a, obs)*globals()[f'xr{s[0]}{s[1]}{a}']
        w = gamma*w + Delta(state,START)
        m1.add_constraint(summ == w) #constraint1
        
    for i in range(len(S_F)): 
        
        globals()[f'd{i}'] = m1.continuous_var(name='d'+str(i))
        m1.add_constraint(np.sum([globals()[f'xr{S_F[i][0]}{S_F[i][1]}{action}'] for action in ACTIONS]) - globals()[f'd{i}'] == 0)
        Bk['d'+str(i)] = S_F[i]
        obj1 -= globals()[f'd{i}'] 
    
    for i in range(len(S_G)):
        globals()[f'd{i+len(S_F)}'] = m1.continuous_var(name='d'+str(i+len(S_F)))
        m1.add_constraint(np.sum([globals()[f'xr{S_G[i][0]}{S_G[i][1]}{action}'] for action in ACTIONS]) + globals()[f'd{i+len(S_F)}'] >= 0)
       
        Bk['d'+str(i+len(S_F))] = S_G[i]
        obj1 -= globals()[f'd{i+len(S_F)}'] 
    m1.add_constraint(OBJ >= objectif_value) 
    #print(Bk)
    return m1,obj1,Bk


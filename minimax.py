from ExtractStates import extractS, extractSA
from itertools import chain, combinations
import sys
import cplex
import docplex.mp
from models import create_model
import time

ACTIONS = ['up','down','right','left']

def powerset(s):
    return set(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

def satisfy(phi, beta):
    for (L, Q) in beta:
        if set(L).issubset(phi) and not set(phi).intersection(Q):
            return False
    
    return True
          
def DomPol(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, start_time):
    
    P = []
    relF = []
    checked = []
    agenda = powerset(relF) - set(checked)
    beta = []

    while len(agenda)!= 0 and (time.time() - start_time <= 1800):
        F = min(agenda, key=len)
        if satisfy(F, beta):
            m, obj = create_model(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, name='modelMMR')
            #m.print_information()
            for s in F:
                for action in ACTIONS:
                    globals()[f'x{s[0]}{s[1]}{action}'] = m.continuous_var(name='x'+str(s[0])+str(s[1])+str(action))
                    m.add_constraint(globals()[f'x{s[0]}{s[1]}{action}'] == 0)
            m.maximize(obj)
            s = m.solve()
            #print(s)
            if s!=None:
                P.append(extractSA(s))
                beta.append((F, extractS(s)))
                relF.append(extractS(s))
            else:
                #print('unsolvable')
                beta.append((F, []))
        checked.append(F)
        agenda = powerset(relF[-1]) - set(checked)
    return P, relF

def utility(q, c, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, start_time):
    chg = set(c).intersection(set(q))
    m, obj = create_model(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, name='model')
    for s in (set(STATES)-chg):
        if (time.time() - start_time) <= 1800:
            for action in ACTIONS:
                globals()[f'x{s[0]}{s[1]}{action}'] = m.continuous_var(name='x'+str(s[0])+str(s[1])+str(action))
                m.add_constraint(globals()[f'x{s[0]}{s[1]}{action}'] == 0)
    m.maximize(obj)
    s = m.solve() 
    return s

def minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, k=2):
    
    start_time = time.time()
    P, relF = DomPol(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, start_time)
    relevant = list(set(list(chain(*relF))))
    #print(relF)
    
    #k=4
    L3={}
    for comb in combinations(relevant, k):
        if (time.time() - start_time <= 1800):
            for c in powerset(comb):
                if utility(comb, c, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, start_time) != None and (time.time() - start_time <= 1800):
                    L3[comb, c] = utility(comb, c, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, start_time).get_objective_value()
    if (time.time() - start_time <= 1800) and len(L3)!=0:
        print('Value of the safely-optimal policy {', max(L3, key=L3.get),'} after the user’s response', max(L3))
    
    L4 = {}
    for chg in powerset(relevant):
        if (time.time() - start_time <= 1800):
            for q in combinations(relevant, k):
                if (time.time() - start_time <= 1800):
                    for q1 in combinations(relevant, k):
                        if q1 != q and (utility(chg, q, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs,start_time) != None) and (utility(chg, q1, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, start_time)!=None) and (time.time() - start_time <= 1800):
                            L4[chg, q, q1] = utility(chg, q, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, start_time).get_objective_value() - utility(chg, q1, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs, start_time).get_objective_value()

    if time.time() - start_time > 1800:
        return 'Timeout'
    if len(L4)==0:
        return []
    else:
        print('Pairwise maximum regret', max(L4.values()))
        print('The agent should ask the minimax-regret (', k ,'-feature) query:', min(L4, key=L4.get))
          
        MMR = min(L4, key=L4.get)
        return MMR
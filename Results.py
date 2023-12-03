from models import create_model, create_model1, model_SF, model_SG

def results(objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, obs):
     
    m1, summ1, Bookkeep = create_model1(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, S_F, S_G, obs, objective_value, name = 'modelF')
    m1.maximize(summ1)
    s = m1.solve()
    if s == None:
        return('Problem unsolvable', '\n')
    
    else: 
        m1.print_solution()
        #print(Bookkeep)
        return s, Bookkeep
        
    
            
         
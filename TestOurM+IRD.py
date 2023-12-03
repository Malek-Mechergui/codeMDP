import time
from itertools import count
from multiprocessing import Process
from Results import results
from Example1 import gridworld_obs_at_Diagonal
from Example2 import rooms4
from Example4 import puddle
from MotivExample import MotivExample
from IRD import IRD
from Example5 import Maze1D


f = open('resultsM+IRD.txt', 'w')
f.write('\n')


    
f.write('********************************Example4 - puddle(3x3)*************************************')
f.write('\n')
f.write('Our method')
f.write('\n')
grid_size=(3,3)

objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = puddle(grid_size)
start_time = time.time()
s, bk = results(objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines = ['Goal \n',str(GOAL_STATE), '\nStart\n' , str(START), str(s), 'Bookkeeping \n', str(bk), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines)
f.write('\n')

f.write('IRD')
f.write('\n')
start_time = time.time()
s1 = IRD(STATES, GOAL_STATE, START, OBSTACLES1, S_G, Transition_fct)
lines2 = [str(s1), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines2)
f.write('\n')
f.write('\n')

f.write('********************************Example4 - puddle(5x5)*************************************')
f.write('\n')
f.write('Our method')
f.write('\n')
grid_size=(5,5)

objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = puddle(grid_size)
start_time = time.time()
s, bk = results(objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines = ['Goal \n',str(GOAL_STATE), '\nStart\n' , str(START), str(s), 'Bookkeeping \n', str(bk), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines)
f.write('\n')

f.write('IRD')
f.write('\n')
start_time = time.time()
s1 = IRD(STATES, GOAL_STATE, START, OBSTACLES1, S_G, Transition_fct)
lines2 = [str(s1), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines2)
f.write('\n')


    





f.close()



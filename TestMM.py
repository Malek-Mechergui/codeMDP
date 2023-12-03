import time
from itertools import count
from multiprocessing import Process
from Results import results
from Example1 import gridworld_obs_at_Diagonal
from Example2 import rooms4
from Example4 import puddle
from MotivExample import MotivExample
from minimax import minimax_regret
from Example5 import Maze1D


f = open('results1.txt', 'w')
f.write('\n')
    
f.write('********************************Example4 - puddle(3x3)*************************************')
f.write('\n')

grid_size=(3,3)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = puddle(grid_size)


f.write('Minimax regret')
f.write('\n')
start_time = time.time()
MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines1 = ['For k = 2','\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines1)
f.write('\n')


f.write('********************************Example4 - puddle(5x5)*************************************')
f.write('\n')

grid_size=(5,5)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = puddle(grid_size)

f.write('Minimax regret')
f.write('\n')
start_time = time.time()
MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines1 = ['For k = 2','\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines1)
f.write('\n')


f.write('********************************Example4 - puddle(7x7)*************************************')
f.write('\n')

grid_size=(7,7)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = puddle(grid_size)


f.write('Minimax regret')
f.write('\n')
start_time = time.time()
MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines1 = ['For k = 2','\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines1)
f.write('\n')


f.write('********************************Example5 - Maze1D (3x3) results*************************************')
f.write('\n')


grid_size = (3,3)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = Maze1D(grid_size)

f.write('Minimax regret')
f.write('\n')
start_time = time.time()
MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines1 = ['For k = 2','\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines1)
f.write('\n')


    
f.write('********************************Example5 - Maze1D (5x5) results*************************************')
f.write('\n')


grid_size = (5,5)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = Maze1D(grid_size)


f.write('Minimax regret')
f.write('\n')
start_time = time.time()
MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines1 = ['For k = 2','\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines1)
f.write('\n')


f.write('********************************Example5 - Maze1D (7x7) results*************************************')
f.write('\n')

grid_size = (7,7)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = Maze1D(grid_size)


f.write('Minimax regret')
f.write('\n')
start_time = time.time()
MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines1 = ['For k = 2','\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines1)
f.write('\n')


f.close()



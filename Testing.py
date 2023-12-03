import time
from itertools import count
from multiprocessing import Process
from Results import results
from minimax import minimax_regret
from Example1 import gridworld_obs_at_Diagonal
from Example2 import rooms4
from Example4 import puddle
from MotivExample import MotivExample
from IRD import IRD

f = open('results1.txt', 'w')
f.write('\n')

f.write('********************************Motiation Example (4x4) results*************************************')
f.write('\n')
f.write('Our method')
f.write('\n')

grid_size = (4,4)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = MotivExample(grid_size)
s, bk = results(objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines = [str(s), 'Bookkeeping \n', str(bk), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines)
f.write('\n')

f.write('IRD')
f.write('\n')
start_time = time.time()
s1 = IRD(STATES, GOAL_STATE, START, OBSTACLES1, S_G, Transition_fct)
lines2 = [str(s1), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines2)
f.write('\n')

f.write('Minimax regret')
f.write('\n')
for k in [1,2,3,4]: #1 query about 1,2,3,4 states (features)
    start_time = time.time()
    MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1, k)
    lines1 = ['For k = ',str(k),'\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
    f.writelines(lines1)
    f.write('\n')
    
f.write('********************************Motiation Example (5x5) results*************************************')
f.write('\n')
f.write('Our method')
f.write('\n')

grid_size = (5,5)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = MotivExample(grid_size)
s, bk = results(objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines = [str(s), 'Bookkeeping \n', str(bk), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines)
f.write('\n')

f.write('IRD')
f.write('\n')
start_time = time.time()
s1 = IRD(STATES, GOAL_STATE, START, OBSTACLES1, S_G, Transition_fct)
lines2 = [str(s1), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines2)
f.write('\n')

f.write('Minimax regret')
f.write('\n')
for k in [1,2,3,4]: #1 query about 1,2,3,4 states (features)
    start_time = time.time()
    MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1, k)
    lines1 = ['For k = ',str(k),'\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
    f.writelines(lines1)
    f.write('\n')

f.write('********************************Motiation Example (9x9) results*************************************')
f.write('\n')
f.write('Our method')
f.write('\n')

grid_size = (9,9)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = MotivExample(grid_size)
s, bk = results(objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines = [str(s), 'Bookkeeping \n', str(bk), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines)
f.write('\n')

f.write('IRD')
f.write('\n')
start_time = time.time()
s1 = IRD(STATES, GOAL_STATE, START, OBSTACLES1, S_G, Transition_fct)
lines2 = [str(s1), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines2)
f.write('\n')

f.write('Minimax regret')
f.write('\n')
for k in [1,2,3,4]: #1 query about 1,2,3,4 states (features)
    start_time = time.time()
    MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1, k)
    lines1 = ['For k = ',str(k),'\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
    f.writelines(lines1)
    f.write('\n')

f.write('********************************Example1 - gridworld_obs_at_Diagonal (4x4) *************************************')
f.write('\n')
f.write('Our method')
f.write('\n')

grid_size = (4,4)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = gridworld_obs_at_Diagonal(grid_size)
s, bk = results(objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines = [str(s), 'Bookkeeping \n', str(bk), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines)
f.write('\n')

f.write('IRD')
f.write('\n')
start_time = time.time()
s1 = IRD(STATES, GOAL_STATE, START, OBSTACLES1, S_G, Transition_fct)
lines2 = [str(s1), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines2)
f.write('\n')

f.write('Minimax regret')
f.write('\n')
for k in [1,2,3,4]: #1 query about 1,2,3,4 states (features)
    start_time = time.time()
    MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1, k)
    lines1 = ['For k = ',str(k),'\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
    f.writelines(lines1)
    f.write('\n')

f.write('********************************Example1 - gridworld_obs_at_Diagonal (5x5) *************************************')
f.write('\n')
f.write('Our method')
f.write('\n')

grid_size = (5,5)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = gridworld_obs_at_Diagonal(grid_size)
s, bk = results(objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines = [str(s), 'Bookkeeping \n', str(bk), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines)
f.write('\n')

f.write('IRD')
f.write('\n')
start_time = time.time()
s1 = IRD(STATES, GOAL_STATE, START, OBSTACLES1, S_G, Transition_fct)
lines2 = [str(s1), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines2)
f.write('\n')

f.write('Minimax regret')
f.write('\n')
for k in [1,2,3,4]: #1 query about 1,2,3,4 states (features)
    start_time = time.time()
    MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1, k)
    lines1 = ['For k = ',str(k),'\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
    f.writelines(lines1)
    f.write('\n')

f.write('********************************Example1 - gridworld_obs_at_Diagonal (9x9) *************************************')
f.write('\n')
f.write('Our method')
f.write('\n')

grid_size = (9,9)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = gridworld_obs_at_Diagonal(grid_size)
s, bk = results(objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines = [str(s), 'Bookkeeping \n', str(bk), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines)
f.write('\n')

f.write('IRD')
f.write('\n')
start_time = time.time()
s1 = IRD(STATES, GOAL_STATE, START, OBSTACLES1, S_G, Transition_fct)
lines2 = [str(s1), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines2)
f.write('\n')

f.write('Minimax regret')
f.write('\n')
for k in [1,2,3,4]: #1 query about 1,2,3,4 states (features)
    start_time = time.time()
    MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1, k)
    lines1 = ['For k = ',str(k),'\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
    f.writelines(lines1)
    f.write('\n')

f.write('********************************Example2 - rooms4 (5x5) *************************************')
f.write('\n')
f.write('Our method')
f.write('\n')
grid_size = (5,5)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = rooms4(grid_size)
s, bk = results(objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines = [str(s), 'Bookkeeping \n', str(bk), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines)
f.write('\n')

f.write('IRD')
f.write('\n')
start_time = time.time()
s1 = IRD(STATES, GOAL_STATE, START, OBSTACLES1, S_G, Transition_fct)
lines2 = [str(s1), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines2)
f.write('\n')

f.write('Minimax regret')
f.write('\n')
for k in [1,2,3,4]: #1 query about 1,2,3,4 states (features)
    start_time = time.time()
    MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1, k)
    lines1 = ['For k = ',str(k),'\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
    f.writelines(lines1)
    f.write('\n')
    
f.write('********************************Example2 - rooms4 (7x7) *************************************')
f.write('\n')
f.write('Our method')
f.write('\n')
grid_size = (7,7)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = rooms4(grid_size)
s, bk = results(objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines = [str(s), 'Bookkeeping \n', str(bk), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines)
f.write('\n')

f.write('IRD')
f.write('\n')
start_time = time.time()
s1 = IRD(STATES, GOAL_STATE, START, OBSTACLES1, S_G, Transition_fct)
lines2 = [str(s1), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines2)
f.write('\n')

f.write('Minimax regret')
f.write('\n')
for k in [1,2,3,4]: #1 query about 1,2,3,4 states (features)
    start_time = time.time()
    MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1, k)
    lines1 = ['For k = ',str(k),'\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
    f.writelines(lines1)
    f.write('\n')

f.write('********************************Example2 - rooms4 (9x9) *************************************')
f.write('\n')
f.write('Our method')
f.write('\n')
grid_size = (9,9)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = rooms4(grid_size)
s, bk = results(objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines = [str(s), 'Bookkeeping \n', str(bk), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines)
f.write('\n')

f.write('IRD')
f.write('\n')
start_time = time.time()
s1 = IRD(STATES, GOAL_STATE, START, OBSTACLES1, S_G, Transition_fct)
lines2 = [str(s1), '\nExecution time \n', str((time.time() - start_time))]
f.writelines(lines2)
f.write('\n')

f.write('Minimax regret')
f.write('\n')
for k in [1,2,3,4]: #1 query about 1,2,3,4 states (features)
    start_time = time.time()
    MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1, k)
    lines1 = ['For k = ',str(k),'\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
    f.writelines(lines1)
    f.write('\n')

    
    
f.write('********************************Example4 - puddle(3x3)*************************************')
f.write('\n')
f.write('Our method')
f.write('\n')
grid_size=(3,3)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = puddle(grid_size)
s, bk = results(objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines = [str(s), 'Bookkeeping \n', str(bk), '\nExecution time \n', str((time.time() - start_time))]
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
f.write('Minimax regret')
f.write('\n')

f.write('Minimax regret')
f.write('\n')
for k in [1,2,3,4]: #1 query about 1,2,3,4 states (features)
    start_time = time.time()
    MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1, k)
    lines1 = ['For k = ',str(k),'\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
    f.writelines(lines1)
    f.write('\n')
    
f.write('********************************Example4 - puddle(5x5)*************************************')
f.write('\n')
f.write('Our method')
f.write('\n')
grid_size=(5,5)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = puddle(grid_size)
s, bk = results(objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines = [str(s), 'Bookkeeping \n', str(bk), '\nExecution time \n', str((time.time() - start_time))]
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
f.write('Minimax regret')
f.write('\n')

f.write('Minimax regret')
f.write('\n')
for k in [1,2,3,4]: #1 query about 1,2,3,4 states (features)
    start_time = time.time()
    MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1, k)
    lines1 = ['For k = ',str(k),'\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
    f.writelines(lines1)
    f.write('\n')

f.write('********************************Example4 - puddle(7x7)*************************************')
f.write('\n')
f.write('Our method')
f.write('\n')
grid_size=(7,7)
start_time = time.time()
objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1 = puddle(grid_size)
s, bk = results(objective_value, S_F, S_G, Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1)
lines = [str(s), 'Bookkeeping \n', str(bk), '\nExecution time \n', str((time.time() - start_time))]
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
f.write('Minimax regret')
f.write('\n')

f.write('Minimax regret')
f.write('\n')
for k in [1,2,3,4]: #1 query about 1,2,3,4 states (features)
    start_time = time.time()
    MMR = minimax_regret(Transition_fct, Reward_fct, STATES, GOAL_STATE, START, OBSTACLES1, k)
    lines1 = ['For k = ',str(k),'\nMMR\n', str(MMR), '\nExecution time \n', str((time.time() - start_time))]
    f.writelines(lines1)
    f.write('\n')

f.close()



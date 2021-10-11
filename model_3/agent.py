import os, sys
if __name__ == '__main__':
    import monitor

project = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project)
from kaggle_environments import make, evaluate
from interfaces import tracker
from model_3 import mind

env = make("connectx", debug=True)
tracker = tracker.tracker()
def agent(obs, config):
    tracker.watch(obs, config)
    mind.think(obs, config)
    action = mind.make_move()
    tracker.set_action(action)
    return action
time_step = env.reset()
print(time_step)
env.run([agent, "negamax"])

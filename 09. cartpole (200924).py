import gym
import numpy as np
import random

env = gym.make('Pendulum-v0')
goal_steps = 500

for _ in range(30): # 30번 수행
    obs = env.reset() # 게임 초기화
    for i in range(goal_steps): # 환경으로부터
        obs, reward, done, info = env.step(env.action_space.sample())

        if done:
            break

        env.render()
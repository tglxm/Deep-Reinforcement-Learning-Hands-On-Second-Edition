import gym
env = gym.make('SpaceInvaders-v0')
env.reset()
for i in range(1000):
	env.render()
	o,r,d,i = env.step(env.action_space.sample())
	if d:
		env.reset()

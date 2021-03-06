




def train_agent(env,agent,episodes,save_every_n ,save_dir):
	total_rewards= []
	average_rewards = []
	snake_lengths = []
	create_path(save_dir)

	for episode in range(episodes):
		total_reward = 0
		current_state = env.reset()
		done = False
		snake_len = 0
		actions_done = 0
		while not done:
			action = agent.get_action(current_state)
			new_state, reward, done, _ = env.step(action)
			total_reward += reward
			if reward == env.food_reward:
				snake_len += 1
			actions_done += 1
			if actions_done > 100:
				print(f'Actions_done:{actions_done} \t Snake Len {snake_len} Total rewards: {total_reward} ')

			agent.remember(current_state,action,reward,new_state,done)
			agent.learn()
			current_state = new_state



		total_rewards.append(total_reward)
		average_reward = sum(total_rewards) / len(total_rewards)
		average_rewards.append(average_reward)
		snake_lengths.append(snake_len)
		print(f"Episode {episode} ended \t Snake length: {snake_len} Reward: {total_reward} \t Average reward {average_reward}")
		if episode % save_every_n == 0:
			agent.save_model(f"{save_dir}after_episode_{episode}.h5")

	with open(f"{save_dir}file.txt", 'w') as output:
		for total,average in zip(total_rewards,average_rewards):
			output.write(f'{total}:{average} \n')

	agent.save_model(f"{save_dir}after_training.h5")

def create_path(path):
	import os
	os.makedirs(path, exist_ok=True)


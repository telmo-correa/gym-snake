#!/usr/bin/env python3

import gym
from gym_snake.register import env_list


def test_reproducible(env_name):
    """ Tests that multiple instances of the grid with same seed have the same encoding. """

    # Verify that the same seed always produces the same environment
    for i in range(5):
        seed = 42 + i
        env1 = gym.make(env_name)
        env1.seed(seed)
        grid1 = env1.grid

        env2 = gym.make(env_name)
        env2.seed(seed)
        grid2 = env2.grid
        assert grid1 == grid2


def test_smoke(env_name):
    """ Runs a few episodes randomly in the environment as a smoke test. """

    env = gym.make(env_name)
    env.max_steps = min(env.max_steps, 200)

    is_multiagent = hasattr(env.action_space, '__iter__')

    for i_episode in range(10):
        env.reset()
        # env.render()
        for t in range(env.max_steps):
            if is_multiagent:
                action = [k.sample() for k in env.action_space]
            else:
                action = env.action_space.sample()

            observation, reward, done, info = env.step(action)
            # env.render()

            if is_multiagent:
                assert len(observation) == len(action)
                assert len(reward) == len(action)
                assert len(done) == len(action)

                if False not in done:
                    # Episode finished
                    break

            else:
                if done:
                    # Episode finished
                    break


def pytest_generate_tests(metafunc):
    metafunc.parametrize("env_name", env_list)

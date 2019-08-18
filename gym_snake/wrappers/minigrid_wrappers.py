# Wrappers adapted from https://github.com/maximecb/gym-minigrid/blob/master/gym_minigrid/wrappers.py
# Distributed under the following license:

"""
BSD 3-Clause License

Copyright (c) 2017, Maxime Chevalier-Boisvert
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import gym


class ReseedWrapper(gym.core.Wrapper):
    """
    Wrapper to always regenerate an environment with the same set of seeds.
    This can be used to force an environment to always keep the same
    configuration when reset.
    """

    def __init__(self, env, seeds=(0, ), seed_idx=0):
        self.seeds = list(seeds)
        self.seed_idx = seed_idx
        super(ReseedWrapper, self).__init__(env)

    def reset(self, **kwargs):
        seed = self.seeds[self.seed_idx]
        self.seed_idx = (self.seed_idx + 1) % len(self.seeds)
        self.env.seed(seed)
        return self.env.reset(**kwargs)

    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        return obs, reward, done, info


class RGBImgObsWrapper(gym.core.ObservationWrapper):
    """
    Wrapper to use fully observable RGB image as the only observation output,
    This can be used to have the agent to solve the environment in pixel space.
    """

    def __init__(self, env):
        super(RGBImgObsWrapper, self).__init__(env)

        sample_observation = env.render(mode='rgb_array')
        is_multiagent = hasattr(env.action_space, '__iter__')

        if is_multiagent:
            self.observation_space = [
                gym.spaces.Box(
                    low=0,
                    high=255,
                    shape=obs.shape,
                    dtype='uint8'
                )
                for obs in sample_observation
            ]
        else:
            self.observation_space = gym.spaces.Box(
                low=0,
                high=255,
                shape=sample_observation.shape,
                dtype='uint8'
            )

    def observation(self, obs):
        env = self.unwrapped
        return env.render(mode='rgb_array')

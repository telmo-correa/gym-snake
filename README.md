# Snake Environment (gym-snake)

[![Build Status](https://travis-ci.org/telmo-correa/gym-snake.svg?branch=master)](https://travis-ci.org/telmo-correa/gym-snake.svg?branch=master)

This is a set of OpenAI Gym environments representing variants on the classic Snake game.

<p align="center">
<img src="https://github.com/telmo-correa/gym-snake/raw/master/figures/Snake-8x8-v0.gif"/>
<img src="https://github.com/telmo-correa/gym-snake/raw/master/figures/Snake-Hex-8x8-v0.gif"/>
</p>

Requirements:
- Python 3.5+
- OpenAI Gym
- NumPy
- PyQT 5 for graphics

Please use this bibtex if you want to cite this repository in your publications:

```
@misc{gym_snake,
  author = {Correa, Telmo},
  title = {Snake Environment for OpenAI Gym},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/telmo-correa/gym-snake}},
}
```

## Installation

You can clone this repository and install all dependencies with pip:

```
git clone https://github.com/telmo-correa/gym-snake.git
cd gym-snake
pip install -e .
```

## Basic Usage

There is a UI application which allows you to manually control single-agent environments with the arrow keys:

```
./manual_control.py
```

The environment being run can be selected with the `--env-name` option, eg:

```
./manual_control.py --env-name Snake-Hex-8x8-v0
```


## Design

#### Inspiration

This environment was created as a study in response to 
[OpenAI's requests for research](https://openai.com/blog/requests-for-research-2/) problems.

Code architecture and renderer are adapted from the excellent [gym-minigrid](https://github.com/maximecb/gym-minigrid)
 environment (see original license in 
 [`rendering.py`](https://github.com/telmo-correa/gym-snake/blob/master/gym_snake/rendering.py)).

#### Structure of the world
- The world is a grid of tiles:
    * NxM square tiles, or
    * NxM hex tiles
- Each tile can contain an apple, part of a snake (a queue of connected tiles), or be empty.
- Each agent controls its own snake.  Until the agent is done, at each step it can
take one of three actions, on square tiles, or one of five actions, on hex tiles:
    * move forward
    * turn left and move forward
    * turn right and move forward
    * turn left twice and move forward (hex only)
    * turn right twice and move forward (hex only)
- If a snake tries to move out of bounds or into the body of a snake, it dies
-- the agent is done and all further inputs are ignored.
- If a snake moves into an apple, the apple is removed, the snake body grows in size
by 1, and a new apple is generated in a random empty tile**.
- All agents are marked as done when a set number of time steps is reached (default 1000).
- The following rewards are provided to each live agent by default:
    * Eating an apple: +1
    * Collision: -1
    * Timeout: 0
    * Default reward each time step: 0

#### Rule variants

- Single apple: snakes die immediately after collecting an apple.
- No contraction: snake bodies just extend at each step, instead of only when collecting an apple.  
This creates a tron-like ever-growing trail behind each agent.

#### Observations

The world state is fully observable by all agents.

A rectangular image with one pixel per tile is provided for each agent.  Pixels have distinct
values for:

- Empty tile
- Apple
- Own agent's snake body
- Own agent's snake head
- Another agent's snake body
- Another agent's snake head
- Dead/done agent's snake body
- Dead/done agent's snake head

#### Multi-agent scenarios

Some of the environments included in this package are multi-agent environments -- more than one snake is being
controlled, with potentially competitive rewards.

OpenAI gym environments do not have a standardized interface to represent this.

In this package, they are implememented in the same manner as the one in the 
[Multi-Agent Particle Environments (MPE)](https://github.com/openai/multiagent-particle-envs) presented with the 
[MADDPG](https://github.com/openai/maddpg) paper:

- `env.action_space` is a list of action spaces, one for each agent.
- `env.observation_space` is a list of observation spaces, one for each agent.
- `env.step` expects a list of actions to be executed simultaneously as input, and it returns a tuple `observations, 
rewards, dones, {}`, with each element being a list with one element per agent.

## Included Environments

The environments below are implemented in the 
[gym_snake/envs](https://github.com/telmo-correa/gym-snake/blob/master/gym_snake/envs) directory.

### Dead apple

An agent receives a reward and dies whenever it collects an apple.

| Environment name                | # Agents | Grid type | Grid size | Initial snake size  |
|---------------------------------|----------|-----------|-----------|---------------------|
| Snake-4x4-DeadApple-v0          | 1        | square    | 4x4       | 2                   |
| Snake-8x8-DeadApple-v0          | 1        | square    | 8x8       | 4                   |
| Snake-16x16-DeadApple-v0        | 1        | square    | 16x16     | 4                   |
| Snake-Hex-4x4-DeadApple-v0      | 1        | hex       | 4x4       | 2                   |
| Snake-Hex-8x8-DeadApple-v0      | 1        | hex       | 8x8       | 4                   |
| Snake-Hex-16x16-DeadApple-v0    | 1        | hex       | 16x16     | 4                   |
| Snake-4x4-DeadApple-2s-v0       | 2        | square    | 4x4       | 2                   |
| Snake-8x8-DeadApple-2s-v0       | 2        | square    | 8x8       | 4                   |
| Snake-16x16-DeadApple-2s-v0     | 2        | square    | 16x16     | 4                   |
| Snake-Hex-4x4-DeadApple-2s-v0   | 2        | hex       | 4x4       | 2                   |
| Snake-Hex-8x8-DeadApple-2s-v0   | 2        | hex       | 8x8       | 4                   |
| Snake-Hex-16x16-DeadApple-2s-v0 | 2        | hex       | 16x16     | 4                   |
| Snake-4x4-DeadApple-3s-v0       | 3        | square    | 4x4       | 2                   |
| Snake-8x8-DeadApple-3s-v0       | 3        | square    | 8x8       | 4                   |
| Snake-16x16-DeadApple-3s-v0     | 3        | square    | 16x16     | 4                   |
| Snake-Hex-4x4-DeadApple-3s-v0   | 3        | hex       | 4x4       | 2                   |
| Snake-Hex-8x8-DeadApple-3s-v0   | 3        | hex       | 8x8       | 4                   |
| Snake-Hex-16x16-DeadApple-3s-v0 | 3        | hex       | 16x16     | 4                   |

### Classic

An agent receives a reward whenever it collects an apple, and a new apple is spawned in an empty location.

| Environment name      | # Agents | Grid type | Grid size | Initial snake size  |
|-----------------------|----------|-----------|-----------|---------------------|
| Snake-4x4-v0          | 1        | square    | 4x4       | 2                   |
| Snake-8x8-v0          | 1        | square    | 8x8       | 4                   |
| Snake-16x16-v0        | 1        | square    | 16x16     | 4                   |
| Snake-Hex-4x4-v0      | 1        | hex       | 4x4       | 2                   |
| Snake-Hex-8x8-v0      | 1        | hex       | 8x8       | 4                   |
| Snake-Hex-16x16-v0    | 1        | hex       | 16x16     | 4                   |
| Snake-4x4-2s-v0       | 2        | square    | 4x4       | 2                   |
| Snake-8x8-2s-v0       | 2        | square    | 8x8       | 4                   |
| Snake-16x16-2s-v0     | 2        | square    | 16x16     | 4                   |
| Snake-Hex-4x4-2s-v0   | 2        | hex       | 4x4       | 2                   |
| Snake-Hex-8x8-2s-v0   | 2        | hex       | 8x8       | 4                   |
| Snake-Hex-16x16-2s-v0 | 2        | hex       | 16x16     | 4                   |
| Snake-4x4-3s-v0       | 3        | square    | 4x4       | 2                   |
| Snake-8x8-3s-v0       | 3        | square    | 8x8       | 4                   |
| Snake-16x16-3s-v0     | 3        | square    | 16x16     | 4                   |
| Snake-Hex-4x4-3s-v0   | 3        | hex       | 4x4       | 2                   |
| Snake-Hex-8x8-3s-v0   | 3        | hex       | 8x8       | 4                   |
| Snake-Hex-16x16-3s-v0 | 3        | hex       | 16x16     | 4                   |

### 4 apples

Same as classic, but four apples are present at all times.

| Environment name         | # Agents | Grid type | Grid size | Initial snake size  |
|--------------------------|----------|-----------|-----------|---------------------|
| Snake-4x4-4a-v0          | 1        | square    | 4x4       | 2                   |
| Snake-8x8-4a-v0          | 1        | square    | 8x8       | 4                   |
| Snake-16x16-4a-v0        | 1        | square    | 16x16     | 4                   |
| Snake-Hex-4x4-4a-v0      | 1        | hex       | 4x4       | 2                   |
| Snake-Hex-8x8-4a-v0      | 1        | hex       | 8x8       | 4                   |
| Snake-Hex-16x16-4a-v0    | 1        | hex       | 16x16     | 4                   |
| Snake-4x4-4a-2s-v0       | 2        | square    | 4x4       | 2                   |
| Snake-8x8-4a-2s-v0       | 2        | square    | 8x8       | 4                   |
| Snake-16x16-4a-2s-v0     | 2        | square    | 16x16     | 4                   |
| Snake-Hex-4x4-4a-2s-v0   | 2        | hex       | 4x4       | 2                   |
| Snake-Hex-8x8-4a-2s-v0   | 2        | hex       | 8x8       | 4                   |
| Snake-Hex-16x16-4a-2s-v0 | 2        | hex       | 16x16     | 4                   |
| Snake-4x4-4a-3s-v0       | 3        | square    | 4x4       | 2                   |
| Snake-8x8-4a-3s-v0       | 3        | square    | 8x8       | 4                   |
| Snake-16x16-4a-3s-v0     | 3        | square    | 16x16     | 4                   |
| Snake-Hex-4x4-4a-3s-v0   | 3        | hex       | 4x4       | 2                   |
| Snake-Hex-8x8-4a-3s-v0   | 3        | hex       | 8x8       | 4                   |
| Snake-Hex-16x16-4a-3s-v0 | 3        | hex       | 16x16     | 4                   |

### Expand

No apples, but snakes expand at every action while alive -- and receive a reward for doing so.
Equivalent to there being apples in all empty squares.

| Environment name             | # Agents | Grid type | Grid size | Initial snake size  |
|------------------------------|----------|-----------|-----------|---------------------|
| Snake-4x4-Expand-v0          | 1        | square    | 4x4       | 2                   |
| Snake-8x8-Expand-v0          | 1        | square    | 8x8       | 4                   |
| Snake-16x16-Expand-v0        | 1        | square    | 16x16     | 4                   |
| Snake-Hex-4x4-Expand-v0      | 1        | hex       | 4x4       | 2                   |
| Snake-Hex-8x8-Expand-v0      | 1        | hex       | 8x8       | 4                   |
| Snake-Hex-16x16-Expand-v0    | 1        | hex       | 16x16     | 4                   |
| Snake-4x4-Expand-2s-v0       | 2        | square    | 4x4       | 2                   |
| Snake-8x8-Expand-2s-v0       | 2        | square    | 8x8       | 4                   |
| Snake-16x16-Expand-2s-v0     | 2        | square    | 16x16     | 4                   |
| Snake-Hex-4x4-Expand-2s-v0   | 2        | hex       | 4x4       | 2                   |
| Snake-Hex-8x8-Expand-2s-v0   | 2        | hex       | 8x8       | 4                   |
| Snake-Hex-16x16-Expand-2s-v0 | 2        | hex       | 16x16     | 4                   |
| Snake-4x4-Expand-3s-v0       | 3        | square    | 4x4       | 2                   |
| Snake-8x8-Expand-3s-v0       | 3        | square    | 8x8       | 4                   |
| Snake-16x16-Expand-3s-v0     | 3        | square    | 16x16     | 4                   |
| Snake-Hex-4x4-Expand-3s-v0   | 3        | hex       | 4x4       | 2                   |
| Snake-Hex-8x8-Expand-3s-v0   | 3        | hex       | 8x8       | 4                   |
| Snake-Hex-16x16-Expand-3s-v0 | 3        | hex       | 16x16     | 4                   |

## License

Rendering code and some of the wrappers are under the BSD-3 license of their original distribution.

Remaining code is under a new BSD-3 license specific to this repository.

🐍 🍎
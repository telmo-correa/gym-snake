#!/usr/bin/env python

from __future__ import division, print_function

import sys
import gym
import time
from optparse import OptionParser

import gym_snake
from gym_snake.envs.constants import GridType, Action4, Action6
from PyQt5.QtCore import Qt

is_done = False


def main():
    parser = OptionParser()
    parser.add_option(
        "-e",
        "--env-name",
        dest="env_name",
        help="gym-snake environment to load",
        default='Snake-8x8-v0'
    )
    (options, args) = parser.parse_args()

    # Load the gym environment
    env = gym.make(options.env_name)

    def resetEnv():
        global is_done

        is_done = False
        env.reset()

    resetEnv()

    # Create a window to render into
    renderer = env.render('human')

    def keyDownCb(keyName):
        global is_done

        if keyName == Qt.Key_Escape:
            sys.exit(0)

        if keyName == Qt.Key_Backspace or is_done:
            resetEnv()
            return

        action = None
        if env.grid_type == GridType.square:
            if keyName == Qt.Key_Left or keyName == Qt.Key_A or keyName == Qt.Key_4:
                action = Action4.left
            elif keyName == Qt.Key_Right or keyName == Qt.Key_D or keyName == Qt.Key_6:
                action = Action4.right
            elif keyName == Qt.Key_Up or keyName == Qt.Key_Space or keyName == Qt.Key_Return or keyName == Qt.Key_W or keyName == Qt.Key_8:
                action = Action4.forward
            else:
                print("unknown key %s" % keyName)
                return

        elif env.grid_type == GridType.hex:
            if keyName == Qt.Key_Left or keyName == Qt.Key_Q or keyName == Qt.Key_7:
                action = Action6.left
            elif keyName == Qt.Key_Right or keyName == Qt.Key_E or keyName == Qt.Key_9:
                action = Action6.right
            elif keyName == Qt.Key_Up or keyName == Qt.Key_Space or keyName == Qt.Key_Return or keyName == Qt.Key_W or keyName == Qt.Key_8:
                action = Action6.forward
            elif keyName == Qt.Key_A or keyName == Qt.Key_4:
                action = Action6.left_left
            elif keyName == Qt.Key_D or keyName == Qt.Key_6:
                action = Action6.right_right

            else:
                print("unknown key %s" % keyName)
                return

        else:
            print('Unknown grid type: ', env.grid_type)

        if action is None:
            return

        obs, reward, done, info = env.step(action)

        print('step=%s, reward=%.2f' % (env.step_count, reward))

        if done:
            print('done!')
            is_done = True

    renderer.window.setKeyDownCb(keyDownCb)

    while True:
        env.render('human')
        time.sleep(0.01)

        # If the window was closed
        if renderer.window is None:
            break


if __name__ == "__main__":
    main()

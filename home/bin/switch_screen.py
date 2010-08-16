#!/usr/bin/env python

"""Script for move mouse to another monitor"""

import marshal
import os

from optparse import OptionParser

MIDDLE = 1437
TEMP_DIR = os.path.join('/tmp/')

def get_mouse_position():
    """
    Calls xmousepos a parse output
    """
    raw = os.popen('xmousepos').read().strip().split(' ')
    return [int(item) for item in raw]

def detect_screen():
    """
    Detects on shich screen we are.
    """
    mouse_pos = get_mouse_position()
    if mouse_pos[0] < MIDDLE:
        return "right", "left"
    else:
        return "left", "right"

def parse_command_line():
    """Examines options and does preliminary checking."""
    parser = OptionParser("run [options]")
    parser.add_option("--screen",
                  dest="screen",
                  type="choice",
                  default="left",
                  choices=("left", "right"),
                  help="Move pointer to left or right screen.")
    return parser.parse_args()

def get_last_position(screen):
    """
    This tries to get last position on target screen. If not found return defaults.
    """
    filename = os.path.join(TEMP_DIR, "switch_%s" % screen)
    if os.path.exists(filename):
        _file = open(filename, 'rb')
        position = marshal.load(_file)
        _file.close()
    else:
        position = []

    return position

def save_last(screen):
    """
    Saves last screen position.
    """
    filename = os.path.join(TEMP_DIR, "switch_%s" % screen)
    _file = open(filename, 'wb')
    marshal.dump(get_mouse_position(), _file)
    _file.close()

def move_to(mouse_pos):
    """
    Moves pointer to mouse_pos
    """
    os.system("xte 'mousemove %d %d'" % (mouse_pos[0], mouse_pos[1]))

def main():
    """
    Parse command line, get last position or default and move pointer
    """
    options, args = parse_command_line() # pylint: disable-msg=W0612
    move_to_screen, actual_screen = detect_screen()
    
    if actual_screen != options.screen:
        new_mouse_pos = get_last_position(move_to_screen)
        save_last(actual_screen)
        move_to(new_mouse_pos)

if __name__ == '__main__':
    main()

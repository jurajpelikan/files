#!/usr/bin/env python
"""
Utility for "installation" and "uninstallation" files.
"""


import os
import shutil
from optparse import OptionParser

def parse_command_line():
    """
    Examines command line options and does preliminary checking.
    """
    parser = OptionParser("create_symlinks [options]")
    parser.add_option(
        "--restore", action="store_true", dest="restore",
        help="Remove created symlinks and restore files from archive.")
    return parser.parse_args()



def get_all_files(path):
    """
    Return all files in path with relative paths.
    """
    # save old path
    old_path = os.getcwd()

    # change dir so we get relative names
    os.chdir(path)

    find = 'find . -type f -print'
    files = [n.strip()[2:] for n in os.popen(find).readlines()]

    # return to original path
    os.chdir(old_path)

    return files

def main():
    """
    We are running from command line.
    """
    # this checks allow testing
    files_root = os.path.abspath(os.path.dirname(__file__))
    user_home = os.environ.get('HOME')
    opts, args = parse_command_line() # pylint: disable-msg=W0612
    create_or_restore(files_root, user_home, opts.restore)

def create_or_restore(files_root, user_home, restore_files=False):
    """
    This creates or restores files.
    """
    # prepare paths
    files_home = os.path.join(files_root, 'home')
    files_archive = os.path.join(files_root, 'archive')

    # create archive dir if not exists
    if not os.path.exists(files_archive):
        os.makedirs(files_archive)

    def create():
        """
        Create missing links and archive original files.
        WARNING: If the file already exists in archive it will be owerwriten.
        """
        # broken links does not exists
        if os.path.exists(target) or os.path.islink(target):
            # check for link
            if os.path.islink(target):
                # check if link is pointing source file
                if os.path.abspath(os.readlink(target)) == source:
                    return

            # create dir in archive if does not exists
            archive_dir = os.path.dirname(archive)
            if not os.path.exists(archive_dir):
                os.makedirs(archive_dir)

            # move target to archive
            shutil.move(target, archive)
            
        # create symlink
        os.symlink(source, target)

    def restore():
        """
        Remove all files links and restore originals.
        """
        # check for link
        if os.path.exists(target) and os.path.islink(target):
            # check if link is pointing source file
            if os.path.abspath(os.readlink(target)) == source:
                # it is one of our files - delete
                os.remove(target)

        # broken links does not exists
        if os.path.exists(archive) or os.path.islink(archive):
            shutil.move(archive, target)
        

    for _file in get_all_files(files_home):
        source = os.path.join(files_home, _file)
        target = os.path.join(user_home, _file)
        archive = os.path.join(files_archive, _file)
        if restore_files:
            restore()
        else:
            create()

if __name__ == '__main__':
    main()


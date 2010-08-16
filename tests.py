#!/usr/bin/env python

"""
Tests from create_symlinks.
"""
import os
import shutil
import unittest

from create_symlinks import create_or_restore

class CreateSymlinksTestCase(unittest.TestCase):
    """
    Check creating and restoring files.
    """

    def setUp(self): # pylint: disable-msg=C0103
        """
        Create sandbox and copy fake home and files.
        """
        pwd = os.path.abspath(os.path.dirname(__file__))
        self.sandbox = os.path.abspath(os.path.join(pwd, '.sandbox'))
        
        self.user_home = os.path.abspath(os.path.join(
            self.sandbox, 'test_home'))
        self.files_home = os.path.abspath(os.path.join(
            self.sandbox, 'home'))

        self.test_files = ['file', 'link', 'bin/file_in_dir', 'bin/link_in_dir']
        self.test_home_files = ['link', 'file_2', 'bin/file_in_dir', 'bin/link_in_dir']
        os.makedirs(self.sandbox)

        shutil.copytree(
            os.path.join(pwd, '.test_home'), self.user_home,
            symlinks=True
            )
        shutil.copytree(
            os.path.join(pwd, '.test_files'), self.files_home,
            symlinks=True
            )
        create_or_restore(self.sandbox, self.user_home)

        
    def test_create(self):
        """
        Check creation of symlinks.
        """
        for _file in self.test_files:
            self.assertTrue(os.path.islink(os.path.join(
                self.user_home, _file)),
                'Failed to create link: %s' % _file
                )
            self.assertEquals(os.readlink(os.path.join(
                self.user_home, _file)),
                os.path.abspath(os.path.join(self.files_home, _file)),
                'Badly created link: %s' % _file
                )
            
        for _file in self.test_home_files:
            self.assertTrue(os.path.exists(os.path.join(
                self.user_home, _file)),
                'Missing file: %s' % _file
                )

    def test_restore(self):
        """
        Check restoration of original.
        """
        create_or_restore(self.sandbox, self.user_home, restore_files=True)

        for _file in self.test_home_files:
            if 'link' in _file:
                self.assertEquals(
                    os.readlink(os.path.join(self.user_home, _file)),
                    'link_source',
                    'Failed to restore original link: %s' % _file
                    )
            else:
                self.assertFalse(os.path.islink(os.path.join(
                    self.user_home, _file)),
                    'Missing file: %s' % _file
                    )

        

    
    def tearDown(self): # pylint: disable-msg=C0103
        """
        Delete sandbox.
        """
        shutil.rmtree(self.sandbox)


if __name__ == '__main__':
    unittest.main()

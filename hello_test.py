#!/usr/bin/env python

import os

from avocado import Test
from avocado import main
from avocado.utils import archive
from avocado.utils import build
from avocado.utils import process


class helloTest(Test):

    """
    Execute the hellotest test suite.
    """
    def setUp(self):
        """
        Set default params and build the hellotest suite.
        """
        hello_tarball = self.params.get('hello_tarball',
                                       default='hellotest.tar.bz2')
        self.hello_length = self.params.get('hello_length', default=100)
        self.hello_loop = self.params.get('hello_loop', default=10)
        # Build the hellotest suite
        self.cwd = os.getcwd()
        tarball_path = os.path.join(self.datadir, hello_tarball)
        archive.extract(tarball_path, self.srcdir)
        self.srcdir = os.path.join(self.srcdir, 'hellotest')
        build.make(self.srcdir)

    def test(self):
        """
        Execute hellotest with the appropriate params.
        """
        os.chdir(self.srcdir)
        cmd = ('./hellotest %s %s' %
               (self.hello_length, self.hello_loop))
        process.system(cmd)
        os.chdir(self.cwd)


if __name__ == "__main__":
    main()

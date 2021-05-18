def setUp(self):
    # stress = 'http://people.seas.harvard.edu/~apw/stress/stress-1.0.4.tar.gz'
    stress = 'https://fossies.org/linux/privat/stress-1.0.4.tar.gz'
    tarball = self.fetch_asset(stress)
    archive.extract(tarball, self.srcdir)

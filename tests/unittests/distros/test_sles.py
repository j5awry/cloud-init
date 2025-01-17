# This file is part of cloud-init. See LICENSE file for license information.

from tests.unittests.helpers import CiTestCase

from . import _get_distro


class TestSLES(CiTestCase):

    def test_get_distro(self):
        distro = _get_distro("sles")
        self.assertEqual(distro.osfamily, 'suse')

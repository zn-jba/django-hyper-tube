# -*- coding: utf-8 -*-
from hstest import dynamic_test

from test.base import HyperTubeTest


class HyperTubeTestRunner(HyperTubeTest):

    funcs = [
        # 1 task
        HyperTubeTest.check_create_videos,
    ]

    @dynamic_test(data=funcs)
    def test(self, func):
        return func(self)


if __name__ == '__main__':
    HyperTubeTestRunner().run_tests()

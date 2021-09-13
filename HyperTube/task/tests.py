# -*- coding: utf-8 -*-
from hstest import dynamic_test

from test.base import HyperTubeTest


class HyperTubeTestRunner(HyperTubeTest):

    funcs = [
        # 1 task
        HyperTubeTest.check_create_videos,
        # 2 task
        HyperTubeTest.check_main_header,
        HyperTubeTest.check_main_page_login_link,
        HyperTubeTest.check_main_page_upload_link,
        HyperTubeTest.check_main_page_video_links,
        HyperTubeTest.check_main_page_video_count,
    ]

    @dynamic_test(data=funcs)
    def test(self, func):
        return func(self)


if __name__ == '__main__':
    HyperTubeTestRunner().run_tests()

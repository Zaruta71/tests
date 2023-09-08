import pytest
from tasks.task_1.task_1_3 import create_duration_couples


class TestDurationCouples:
    def test_duration_index(self):
        courses_list_ = [{'title': 'JavaTest', 'mentors': ['User1', 'User2'], 'duration': 14}]
        res_duration_index, res_mcount_index = create_duration_couples(courses_list=courses_list_)
        expected = [[14, 0]]
        assert res_duration_index == expected

    def test_mcount_index(self):
        courses_list_ = [{'title': 'JavaTest', 'mentors': ['User1', 'User2'], 'duration': 14}]
        res_duration_index, res_mcount_index = create_duration_couples(courses_list=courses_list_)
        expected = [[2, 0]]
        assert res_mcount_index == expected

import pytest
from tasks.task_1.task_1_2 import course_durations
from types import GeneratorType


class TestCourseDurations:
    def test_duration_generator(self):
        duration_dict_ = {14: [0]}
        courses_list_ = [{'title': 'JavaTest', 'mentors': ['User1', 'User2'], 'duration': 14}]
        res = course_durations(courses_list_=courses_list_, durations_dict_=duration_dict_)
        assert isinstance(res, GeneratorType)


import pytest
from tasks.task_1.task_1_1 import generate_course_list


@pytest.mark.parametrize(
    'courses,mentors,durations,expected',
    [
        (['Java'], [['User1', 'User2']], [14], [{'title': 'Java', 'mentors': ['User1', 'User2'], 'duration': 14}]),
        (['Python'], [['User1', 'User2']], [15], [{'title': 'Python', 'mentors': ['User1', 'User2'], 'duration': 15}])
    ]
)
def test_generate_data_with_params(courses, mentors, durations, expected):
    res = generate_course_list(courses, mentors, durations)
    assert res == expected


class TestGenerateCourseList:
    def test_generate_data(self):
        courses = ['Java']
        mentors = [['User1', 'User2']]
        durations = [14]
        res = generate_course_list(courses, mentors, durations)
        expected = [{'title': 'Java', 'mentors': ['User1', 'User2'], 'duration': 14}]
        assert res == expected

    def test_return_list(self):
        courses = ['Java']
        mentors = [['User1', 'User2']]
        durations = [14]
        res = generate_course_list(courses, mentors, durations)
        assert isinstance(res, list)

import pytest
from prepare_commit_msg import getJiraPrefix

provider: object = [
    ('feature/WEBDEV-163377-test', 'WEBDEV-163377'),
    ('bugfix/WEBDEV-333-test', 'WEBDEV-333'),
    ('feature/WEBDEV-333', 'WEBDEV-333'),
    ('feature/WEBDEV-22', 'WEBDEV-22'),
    ('feature/WEBDEV', None),
    ('feature/WEBDEV-something', None),
    ('feature/something', None),
]


@pytest.mark.parametrize("branch,expected", provider)
def test_check_commit_positive(branch: str, expected):
    result = getJiraPrefix(branch)
    assert (result == expected)

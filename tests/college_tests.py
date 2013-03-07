from libnemesis import College

def test_college_has_correct_users():
    c = College("college-1")
    users = set([u.username for u in c.users])
    expected_users = set(["teacher_coll1", "student_coll1_1", "student_coll1_2"])

    assert users == expected_users

def test_college_has_correct_name():
    c = College("college-1")
    assert c.name == "college the first"

def test_college_has_correct_teams():
    c = College("college-1")
    assert set([t.name for t in c.teams]) == set(["team-ABC", "team-DFE"])
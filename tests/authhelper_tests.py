from __future__ import unicode_literals

from libnemesis import AuthHelper

class FakeAuthorization:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class FakeRequest:
    def __init__(self, username=None, password=None):
        if username and password:
            self.authorization = FakeAuthorization(username, password)
        else:
            self.authorization = None

def test_authhelper_finds_invalid_users():
    x = AuthHelper(FakeRequest("wrong_user", "wrong_password"))
    assert not x.user_exists

def test_authhelper_finds_valid_users():
    x = AuthHelper(FakeRequest("student_coll1_1", "wrong_password"))
    assert x.user_exists

def test_authhelper_finds_valid_users_wrong_case():
    x = AuthHelper(FakeRequest("Student_Coll1_1", "wrong_password"))
    assert x.user_exists

def test_authhelper_finds_wrong_password():
    x = AuthHelper(FakeRequest("student_coll1_1", "wrong_password"))
    assert not x.password_correct

def test_authhelper_finds_right_password():
    x = AuthHelper(FakeRequest("student_coll1_1", "cows"))
    assert x.password_correct

def test_authhelper_finds_right_password_wrong_case_username():
    x = AuthHelper(FakeRequest("Student_Coll1_1", "cows"))
    assert x.password_correct

def test_authhelper_produces_correct_user():
    x = AuthHelper(FakeRequest("blueshirt", "blueshirt"))
    assert x.user.is_blueshirt

def test_authhelper_produces_correct_user_from_wrong_case():
    x = AuthHelper(FakeRequest("Student_Coll1_1", "cows"))
    assert x.user.username == "student_coll1_1"

def test_authhelper_produces_null_user():
    x = AuthHelper(FakeRequest("owiefjwqoi", "blueshirt"))
    assert not x.user.is_blueshirt

def test_authhelper_will_succeed_no_form():
    x = AuthHelper(FakeRequest())
    assert not x.auth_will_succeed

def test_authhelper_will_succeed_no_password():
    x = AuthHelper(FakeRequest("blueshirt"))
    assert not x.auth_will_succeed

def test_authhelper_will_succeed_wrong_password():
    x = AuthHelper(FakeRequest("blueshirt", "bees"))
    assert not x.auth_will_succeed

def test_authhelper_will_succeed_all_right():
    x = AuthHelper(FakeRequest("blueshirt", "blueshirt"))
    assert x.auth_will_succeed

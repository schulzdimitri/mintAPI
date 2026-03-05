import pytest

from src.drivers.password_handler import PasswordHandler

from .login_creator import LoginCreator

username = "test_user"
password = "password123"
hashed_password = PasswordHandler().encrypt_password(password)


class MockUserRepository:
    def get_user_by_username(self, username: str):
        return (10, username, hashed_password)
    
def test_create():
    login_creator = LoginCreator(MockUserRepository())
    response = login_creator.create(username, password)
    
    assert response["access"] == True
    assert response["username"] == username
    assert response["autorization"] is not None

def test_create_with_incorrect_password():
    login_creator = LoginCreator(MockUserRepository())
    response = login_creator.create(username, password)
    
    with pytest.raises(ValueError):
        login_creator.create(username, "wrong_password")
    
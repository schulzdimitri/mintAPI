from src.drivers.jwt_handler import JWTHandler
from src.drivers.password_handler import PasswordHandler
from src.models.interface.user_repository import UserRepositoryInterface

from .interfaces.login_creator import LoginCreatorInterface


class LoginCreator(LoginCreatorInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
        self.__jwt_driver = JWTHandler()
        self.__password_driver = PasswordHandler()

    def create(self, username: str, password: str) -> dict:
        user = self.__find_user(username)
        user_id = user[0]
        hashed_password = user[2]
        
        self.__verify_correct_password(password, hashed_password)
        token = self.__create_jwt_token(user_id)
        return self.__format_response(username, token)

    def __find_user(self, username: str) -> tuple[int, str, str]:
        user = self.__user_repository.get_user_by_username(username)
        if not user:
            raise ValueError("User not found")
        return user
    
    def __verify_correct_password(self, password: str, hashed_password: str) -> bool:
        is_password_correct = self.__password_driver.check_password(password, hashed_password)
        if not is_password_correct:
            raise ValueError("Incorrect password")
        return is_password_correct
    
    def __create_jwt_token(self, user_id: int) -> str:
        token = self.__jwt_driver.create_jwt_token({"user_id": user_id})
        return token
    
    def __format_response(self, username: str, token: str) -> dict:
        return {
            "access": True, 
            "username": username,
            "autorization": token  
        }
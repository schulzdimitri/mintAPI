import jwt
from flask import request

from src.drivers.jwt_handler import JWTHandler
from src.errors.types.http_unauthorized import HttpUnauthorizedError


def auth_jwt_verify():
    jwt_handler = JWTHandler()
    raw_token = request.headers.get('Authorization')
    user_id = request.headers.get("uid")
    
    if not raw_token or not user_id:
        raise HttpUnauthorizedError("Invalid Auth informations")
    
    token = raw_token.split()[1]
    token_info = jwt_handler.decode_jwt_token(token)
    token_uid = token_info["user_id"]
    
    if token_uid and user_id and (int(token_uid) == int(user_id)):
        return token_info
    
    raise HttpUnauthorizedError("User Unauthorized")
    
from datetime import datetime, timedelta, timezone

import jwt

from src.configs.jwt_configs import jwt_infos


class JWTHandler:
    def create_jwt_token(self, body: dict = {}) -> str:
        token = jwt.encode(
            payload={
                "exp": datetime.now(timezone.utc) + timedelta(hours=jwt_infos["ACCESS_TOKEN_EXPIRE_HOURS"]),
                **body
            },
            key=jwt_infos["JWT_KEY"],
            algorithm=jwt_infos["ALGORITHM"]
        )
        return token

    def decode_jwt_token(self, token: str) -> dict:
        token_info = jwt.decode(
            jwt=token,
            key=jwt_infos["JWT_KEY"],
            algorithms=jwt_infos["ALGORITHM"]
        )
        return token_info

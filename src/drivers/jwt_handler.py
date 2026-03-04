from datetime import datetime, timedelta, timezone

import jwt


class JWTHandler:
    def create_jwt_token(self, body: dict = {}) -> str:
        token = jwt.encode(
            payload={
                "exp": datetime.now(timezone.utc) + timedelta(hours=1),
                **body
            },
            key="5578dcf11fb3abf7491c4af06ec7db09a073963602b176f93765fa07355d1dde",
            algorithm="HS256"
        )
        return token

    def decode_jwt_token(self, token: str) -> dict:
        token_info = jwt.decode(
            jwt=token,
            key="5578dcf11fb3abf7491c4af06ec7db09a073963602b176f93765fa07355d1dde",
            algorithms=["HS256"]
        )
        return token_info

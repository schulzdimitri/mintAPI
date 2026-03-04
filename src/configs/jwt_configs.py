import os

jwt_infos = {
    "JWT_KEY": os.getenv("JWT_KEY"),
    "ALGORITHM": os.getenv("ALGORITHM"),
    "ACCESS_TOKEN_EXPIRE_HOURS": int(os.getenv("ACCESS_TOKEN_EXPIRE_HOURS"))
}
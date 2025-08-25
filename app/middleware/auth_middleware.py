from fastapi import HTTPException, Depends
from app.utils.jwt_helper import decode_token


def required_role(required_role: str):
    def role_checker(token: str = Depends(decode_token)):
        user_role = token.get('role')
        if user_role != required_role:
            raise HTTPException(status_code=403, detail="Forbidden")
        return True
    return role_checker
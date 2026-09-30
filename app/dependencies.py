from fastapi import (
    Depends,
    Header,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.entities import User
from app.utils.security import decode_token


def get_current_user(
    authorization: str | None = Header(default=None),
    db: Session = Depends(get_db),
):
    if (
        not authorization
        or not authorization.lower().startswith("bearer ")
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
        )

    token = authorization.split(" ", 1)[1]

    user_id = decode_token(token)

    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found",
        )

    return user
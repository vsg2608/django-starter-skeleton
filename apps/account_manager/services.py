from typing import Optional

from apps.account_manager.models import BaseUser


def user_create(
    *,
    email: str,
    username: str,
    is_active: bool = True,
    is_admin: bool = False,
    password: Optional[str] = None
) -> BaseUser:
    user = BaseUser.objects.create_user(
        email=email,
        username= username,
        is_active=is_active,
        is_admin=is_admin,
        password=password
    )

    return user

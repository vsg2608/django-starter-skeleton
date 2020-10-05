from apps.account_manager.models import BaseUser


def user_get_login_data(*, user: BaseUser):
    return {
        'id': user.id,
        'email': user.email,
        'username': user.username,
        'is_active': user.is_active,
        'is_admin': user.is_admin,
        'is_superuser': user.is_superuser,
    }

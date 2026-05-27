from __future__ import annotations


class LoginDataModel:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @classmethod
    def get_login_data(cls, variables: dict, is_valid: bool) -> LoginDataModel:
        user_type = 'standard' if is_valid else 'locked_out'
        return cls(
            variables['users'][user_type]['username'],
            variables['users'][user_type]['password']
        )

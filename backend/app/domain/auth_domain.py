def can_register_user(existing_user: bool) -> None:
if existing_user:
raise ValueError("EMAIL_ALREADY_EXISTS")




def validate_login(user_exists: bool, password_valid: bool) -> None:
if not user_exists or not password_valid:
raise ValueError("INVALID_CREDENTIALS")
class AuthError(Exception):
    def __init__(self, status_code: int = 401, detail: str = "Unauthorize"):
        self.status_code = status_code
        self.detail = detail

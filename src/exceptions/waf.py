from fastapi import HTTPException


class DuplicateKeyHTTPException(HTTPException):
    def __init__(self, detail=""):
        super(DuplicateKeyHTTPException, self).__init__(
            status_code=400, detail=detail
        )

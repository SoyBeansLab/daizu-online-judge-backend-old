from typing import List, Type, Dict
from fastapi import HTTPException
from fastapi.responses import JSONResponse


class APIError(Exception):
    status_code: int = 404
    detail: str = "Error"


class DuplicateKeyHTTPException(APIError):
    status_code = 400
    detail = "Duplicate key"


class NotFoundException(APIError):
    status_code = 404
    detail = "404 Not Found"


class SqlTransactionException(APIError):
    status_code = 500
    detail = "Internal Server Error"


async def api_error_handler(request, err: APIError):
    return JSONResponse(
        status_code=err.status_code, content={"detail": err.detail,},
    )


# https://tech.jxpress.net/entry/fastapi_error_definitions
def error_response(error_types: List[Type[APIError]]) -> Dict:
    d = {}
    for et in error_types:
        if not d.get(et.status_code):
            d[et.status_code] = {
                "description": f"{et.detail}",
                "content": {
                    "application/json": {"example": {"detail": et.detail}}
                },
            }
        else:
            d[et.status_code]["description"] += f"<br>{et.detail}"
    return d

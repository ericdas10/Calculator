from datetime import datetime
import json

from sqlalchemy.orm import Session
from app.model.request_log import RequestLog
from app.services import math_service
from app.services import cache_service

# def process_fibonacci(n: int, db: Session, user_id: int = None) -> str:
#     result = math_service.fibonacci(n)
#     return _save_request("fibonacci", {"n": n}, result, db, user_id)
#
# def process_factorial(n: int, db: Session, user_id: int = None) -> str:
#     result = math_service.factorial(n)
#     return _save_request("factorial", {"n": n}, result, db, user_id)
#
# def process_power(base: float, exponent: float, db: Session, user_id: int = None) -> str:
#     result = math_service.power(base, exponent)
#     return _save_request("pow", {"base": base, "exponent": exponent}, result, db, user_id)

def _save_request(operation: str, input_data: dict, result: int | float, db: Session, user_id: int = None) -> str:
    log = RequestLog(
        operation=operation,
        input_data=json.dumps(input_data),
        result=str(result),
        created_at=datetime.utcnow(),
        user_id=user_id
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return str(result)

def process_fibonacci(n: int, db: Session, user_id: int = None) -> str:
    result = cache_service.get_fibonacci(n, db)
    return _save_request("fibonacci", {"n": n}, result, db, user_id)

def process_factorial(n: int, db: Session, user_id: int = None) -> str:
    result = cache_service.get_factorial(n, db)
    return _save_request("factorial", {"n": n}, result, db, user_id)

def process_power(base: float, exponent: float, db: Session, user_id: int = None) -> str:
    result = cache_service.get_power(base, exponent, db)
    return _save_request("pow", {"base": base, "exponent": exponent}, result, db, user_id)


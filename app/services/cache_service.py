from sqlalchemy.orm import Session
from app.model.cache_entities import FibonacciCache, FactorialCache, PowCache

def get_fibonacci(n: int, db: Session) -> int:
    cached = db.query(FibonacciCache).filter_by(n=n).first()
    if cached:
        print(f"[CACHE HIT] fibonacci({n}) = {cached.result}")
        return cached.result

    seed = db.query(FibonacciCache).filter(FibonacciCache.n < n).order_by(FibonacciCache.n.desc()).first()

    if seed:
        a = seed.result
        b = db.query(FibonacciCache).filter_by(n=seed.n + 1).first()
        if b:
            b = b.result
            start = seed.n + 2
        else:
            # calculează b = fib(n0+1)
            b = a + get_fibonacci(seed.n - 1, db) if seed.n > 0 else 1
            _try_cache_fib(seed.n + 1, b, db)
            start = seed.n + 2

    for i in range(start, n + 1):
        a, b = b, a + b
        _try_cache_fib(i, b, db)

    db.commit()
    return b

def _try_cache_fib(n: int, result: int, db: Session):
    if not db.query(FibonacciCache).filter_by(n=n).first():
        db.add(FibonacciCache(n=n, result=result))


def get_factorial(n: int, db: Session) -> int:
    cached = db.query(FactorialCache).filter_by(n=n).first()
    if cached:
        print(f"[CACHE HIT] factorial({n}) = {cached.result}")
        return cached.result

    seed = db.query(FactorialCache).filter(FactorialCache.n < n).order_by(FactorialCache.n.desc()).first()

    if seed:
        result = seed.result
        start = seed.n + 1
    else:
        result = 1
        start = 1

    for i in range(start, n + 1):
        result *= i
        _try_cache_fact(i, result, db)

    db.commit()
    return result

def _try_cache_fact(n: int, result: int, db: Session):
    if not db.query(FactorialCache).filter_by(n=n).first():
        db.add(FactorialCache(n=n, result=result))


def get_power(base: float, exponent: float, db: Session) -> float:
    cached = db.query(PowCache).filter_by(base=base, exponent=exponent).first()
    if cached:
        print(f"[CACHE HIT] pow({base}, {exponent}) = {cached.result}")
        return cached.result

    result = base ** exponent
    db.add(PowCache(base=base, exponent=exponent, result=result))
    db.commit()
    return result

from pydantic import BaseModel, Field

class FibonacciRequest(BaseModel):
    n: int = Field(..., ge=0, description="Indexul n din sirul lui Fibonacci")

class PowRequest(BaseModel):
    base: float
    exponent: float

class FactorialRequest(BaseModel):
    n: int = Field(..., ge=0)

class OperationResult(BaseModel):
    result: str
    operation: str

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

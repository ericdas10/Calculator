from flask import Blueprint, request, jsonify
from app.model.schemas import FibonacciRequest, FactorialRequest, PowRequest, OperationResult, UserCreate, UserResponse
from app.repository.db import SessionLocal
from app.services import request_service, auth_service
from sqlalchemy.exc import SQLAlchemyError
import traceback

api = Blueprint('api', __name__)

@api.route("/fibonacci", methods=["POST"])
def fibonacci_endpoint():
    try:
        payload = FibonacciRequest(**request.json)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    db = SessionLocal()
    try:
        result = request_service.process_fibonacci(payload.n, db)
        return jsonify(OperationResult(result=result, operation="fibonacci").dict())
    finally:
        db.close()


@api.route("/factorial", methods=["POST"])
def factorial_endpoint():
    try:
        payload = FactorialRequest(**request.json)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    db = SessionLocal()
    try:
        result = request_service.process_factorial(payload.n, db)
        return jsonify(OperationResult(result=result, operation="factorial").dict())
    finally:
        db.close()


@api.route("/pow", methods=["POST"])
def power_endpoint():
    try:
        payload = PowRequest(**request.json)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    db = SessionLocal()
    try:
        result = request_service.process_power(payload.base, payload.exponent, db)
        return jsonify(OperationResult(result=result, operation="pow").dict())
    finally:
        db.close()

@api.route("/register", methods=["POST"])
def register_endpoint():
    try:
        user_data = UserCreate(**request.json)
    except Exception as e:
        return jsonify({"error": f"Invalid input: {str(e)}"}), 400

    db = SessionLocal()
    try:
        new_user = auth_service.register_user(user_data, db)
        return jsonify(UserResponse.from_orm(new_user).dict()), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except SQLAlchemyError as db_err:
        print("Database error:", db_err)             # log explicit
        traceback.print_exc()                           # log stacktrace complet
        return jsonify({"error": "Database error"}), 500
    finally:
        db.close()

@api.route("/login", methods=["POST"])
def login_endpoint():
    try:
        user_data = UserCreate(**request.json)
    except Exception as e:
        return jsonify({"error": f"Invalid input: {str(e)}"}), 400

    db = SessionLocal()
    try:
        user = auth_service.login_user(user_data, db)
        return jsonify(UserResponse.from_orm(user).dict()), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 401
    except SQLAlchemyError:
        return jsonify({"error": "Database error"}), 500
    finally:
        db.close()

@api.route("/logout", methods=["POST"])
def logout_endpoint():
    # Nu avem sesiune activă — doar simulăm logout
    return jsonify({"message": "Logged out (dummy)"}), 200


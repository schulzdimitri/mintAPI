from flask import Blueprint, jsonify

bank_account_bp = Blueprint('bank_routes', __name__)

@bank_account_bp.route('/', methods=['GET'])
def get_bank_accounts():
    bank_accounts = [
        {"id": 1, "name": "Checking Account", "balance": 1500.00},
        {"id": 2, "name": "Savings Account", "balance": 5000.00}
    ]
    return jsonify(bank_accounts, 200)
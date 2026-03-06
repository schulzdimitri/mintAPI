from flask import Flask, jsonify, request

from src.main.routes.bank_account_routes import bank_account_bp
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()

app = Flask(__name__)

app.register_blueprint(bank_account_bp)
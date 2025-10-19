from flask import Blueprint

loan_routes = Blueprint('loan_routes', __name__)

@loan_routes.route('/loans')
def all_loans():
    return "Loans route working!"

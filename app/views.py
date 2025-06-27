from flask import Blueprint, render_template, request
from .evaluator import evaluate_expression, variables

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        action = request.form.get('action')
        if action == "reset":
            variables.clear()
            result = "All variables reset."
        elif action == "view":
            result = "\n".join(f"{k} = {v}" for k, v in variables.items()) or "No variables defined."
        else:
            expr = request.form.get('expression')
            try:
                result = evaluate_expression(expr)
            except Exception as e:
                result = f"Error: {str(e)}"
    return render_template('index.html', result=result)
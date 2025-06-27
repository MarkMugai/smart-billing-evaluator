from app.evaluator import evaluate_expression, variables

def test_basic_math():
    assert evaluate_expression("2 + 3 * 4") == 14

def test_assignment():
    evaluate_expression("a = 10")
    assert variables['a'] == 10

def test_plusassign():
    evaluate_expression("a += 5")
    assert variables['a'] == 15

def test_logic():
    evaluate_expression("b = true")
    assert variables['b'] == True
    assert evaluate_expression("b && false") == False

def test_ternary():
    evaluate_expression("x = 200")
    result = evaluate_expression("x > 100 ? 500 : 0")
    assert result == 500

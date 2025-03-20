def check_parentheses(expression: str) -> bool:
    if expression.count("(") == expression.count(")"):
        return True
    else:
        return False

print(check_parentheses(")("))







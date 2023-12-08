from radon.complexity import cc_visit

def detect_high_cyclomatic_complexity(code):
    results = cc_visit(code)
    for result in results:
        if result.complexity > 2:
            return True
    return False


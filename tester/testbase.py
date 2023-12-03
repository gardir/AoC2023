

def test(f, test_cases):
    failed = False
    for params, expected in test_cases:
        try:
            actual = f(*params)
        except Exception as e:
            actual = e
        if actual != expected:
            failed = True
            print(f"{f.__name__}({params}) => {actual} (!= '{expected}')")
    if not failed:
        print(f"All for '{f.__name__}' OK!")
    return failed



def test(f, test_cases):
    failed = False
    for params, expected in test_cases:
        try:
            actual = f(params)
        except Exception as e:
            actual = e
        if actual != expected:
            failed = True
            print(f"extract({params}) => {actual} (!= '{expected}')")
    if not failed:
        print("All OK!")
    return failed

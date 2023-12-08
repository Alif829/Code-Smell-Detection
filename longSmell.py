def long_method_example(a, b):
    x = 10
    y = 20
    z = 30
    w = 40
    p = 50
    q = 60
    r = 70
    s = 80
    t = 90
    u = 100
    v = 110  # This will push the direct children count over 10


    if x > 5:  # Detected as a potential contributor to long method
        y = x

    for i in range(10):  # Another potential contributor
        x = x + i

    while y > 0:  # And another one
        y -= 1

    try:  # Yet another one
        z = x / y
    except ZeroDivisionError:
        z = 0

    return z  # Finally, this one too
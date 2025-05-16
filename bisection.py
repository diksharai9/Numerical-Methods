def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have opposite signs at endpoints a and b.")

    for i in range(1, max_iter + 1):
        c = (a + b) / 2.0
        fc = func(c)

        # Check for convergence
        if abs(fc) < tol or (b - a) / 2 < tol:
            return c, i, True

        # Update interval
        if func(a) * fc < 0:
            b = c
        else:
            a = c

    # Did not converge
    return c, max_iter, False


def f(x):
    return x**4 - x - 12

def slow_func(x):
    return x**5 - 0.5
root, iterations, converged = bisection_method(slow_func, 0, 1, tol=1e-8, max_iter=1000)


# root, iterations, converged = bisection_method(f, 1, 2)

if converged:
    print(f"Root found: {root} (in {iterations} iterations)")
else:
    print("Bisection method did not converge.")

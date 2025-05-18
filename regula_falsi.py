def regula_falsi(func, a, b, tol=1e-6, max_iter=100):

    fa = func(a)
    fb = func(b)

    if fa * fb >= 0:
        raise ValueError("The function must have opposite signs at endpoints a and b.")

    for i in range(1, max_iter + 1):
        # Compute the false position (linear interpolation)
        c = b - fb * (b - a) / (fb - fa)
        fc = func(c)

        if abs(fc) < tol:
            return c, i, True

        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    return c, max_iter, False  # Did not converge
def slow_func(x):
    return x**5 - 0.5
root, iterations, converged = regula_falsi(slow_func, 0, 1, tol=1e-8, max_iter=1000)

if converged:
    print(f"Root found: {root} (in {iterations} iterations)")
else:
    print("Regula Falsi method did not converge.")

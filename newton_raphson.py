def newton_raphson(func, derivative, x0, tol=1e-6, max_iter=100):

    x = x0

    for i in range(1, max_iter + 1):
        f_x = func(x)
        df_x = derivative(x)

        if df_x == 0:
            raise ZeroDivisionError(f"Derivative is zero at x = {x}. Try a different initial guess.")

        x_new = x - f_x / df_x

        if abs(x_new - x) < tol:
            return x_new, i, True

        x = x_new

    return x, max_iter, False  # Did not converge

# Define the function and its derivative
def slow_func(x):
    return x**5 - 0.5

def slow_func_derivative(x):
    return 5 * x**4

# Initial guess
initial_guess = 0.6

# Run Newton-Raphson
root, iterations, converged = newton_raphson(slow_func, slow_func_derivative, initial_guess, tol=1e-8)

# Output result
if converged:
    print(f"Root found: {root} (in {iterations} iterations)")
else:
    print("Newton-Raphson method did not converge.")

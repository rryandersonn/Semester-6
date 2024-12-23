#Ryan Anderson
#System of 2 Equations Solver

# import libraries
from sympy import symbols, Eq
from sympy.solvers import linsolve

# Define variables
x, y = symbols('x y')

# Input equations
# Example equations: 2x + 3y - 6 = 0 and x - y - 2 = 0
eq1 = Eq(5 * x + 3 * y - 6, 0)  # Replace with your equation
eq2 = Eq(x - y - 10, 0)          # Replace with your equation

# Solve the equations
solution = linsolve([eq1, eq2], (x, y))

# Display the solution
print("Solution:", solution)

#Ryan Anderson
#System of 3 Equations Solver

#import libraries
from sympy import symbols, Eq
from sympy.solvers import linsolve

# Define variables
x, y, z = symbols('x y z')

# Input equations
# Example equations: x + 2y + 3z = 6, 2x - y + z = 3, and -x + y + 2z = 0
eq1 = Eq(x + 2 * y + 3 * z, 6)   # Replace with your equation
eq2 = Eq(2 * x - y + z, 3)       # Replace with your equation
eq3 = Eq(-x + y + 2 * z, 0)      # Replace with your equation

# Solve the equations
solution = linsolve([eq1, eq2, eq3], (x, y, z))

# Display the solution
print("Solution:", solution)

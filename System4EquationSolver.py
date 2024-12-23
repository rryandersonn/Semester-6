#Ryan Anderson
#System of 4 Equation Solver 

# Import Libraries
from sympy import symbols, Eq
from sympy.solvers import linsolve

# Define variables
x, y, z, w = symbols('x y z w')

# Input equations
# Example equations: 
eq1 = Eq(x + 2 * y + z + w, 10)      # Replace with your equation
eq2 = Eq(2 * x - y + z - w, 0)   # Replace with your equation
eq3 = Eq(-x + y + 2 * z + w, 0)  # Replace with your equation
eq4 = Eq(x - y - z + 2 * w, 0)   # Replace with your equation

# Solve the equations
solution = linsolve([eq1, eq2, eq3, eq4], (x, y, z, w))

# Display the solution
print("Solution:", solution)

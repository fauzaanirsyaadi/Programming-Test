from pulp import *

# Create the LP problem object
prob = LpProblem("Carbohydrate Minimization", LpMinimize)

# Define the decision variables: amounts of rice, corn, and potato in grams
rice = LpVariable("Rice", lowBound=0)
corn = LpVariable("Corn", lowBound=0)
potato = LpVariable("Potato", lowBound=0)

# Define the objective function: minimize the total cost of food
prob += 0.28*rice + 0.21*corn + 0.17*potato

# Define the constraints: the total amount of carbohydrate should be around 400 grams
prob += 0.28*rice + 0.21*corn + 0.17*potato == 400
prob += rice + corn + potato >= 100

# Solve the LP problem
prob.solve()

# Print the status and the optimal solution
print("Status:", LpStatus[prob.status])
print("Minimum cost:", value(prob.objective))
print("Amount of rice (grams):", value(rice))
print("Amount of corn (grams):", value(corn))
print("Amount of potato (grams):", value(potato))

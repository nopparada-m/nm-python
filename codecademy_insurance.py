import numpy as np

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost("Maria", 31, 0, 23.1, 1, 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost("Rohan", 25, 1, 28.5, 3, 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost("Valentina", 53, 0, 31.4, 0, 1)

akira_insurance_cost = estimate_insurance_cost("Akira", 19, 0, 27.1, 0, 0)

# Add your code here
names = ["Maria", "Rohan", "Valentina", "Akira"]
insurance_costs = [4150.0, 5320.0, 35210.0, 2930.0]
insurance_data = list(zip(names, insurance_costs))
print("Here is the actual insurance cost data: " + str(insurance_data))

estimated_insurance_data = []
#for i in range(len(insurance_data)):
  #estimated_insurance_data.append(insurance_data[i])
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))
estimated_insurance_data.append(("Akira", akira_insurance_cost))
print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))

estimated_insurance_cost = []
estimated_insurance_cost.append(maria_insurance_cost)
estimated_insurance_cost.append(rohan_insurance_cost)
estimated_insurance_cost.append(valentina_insurance_cost)
estimated_insurance_cost.append(akira_insurance_cost)

difference = np.subtract(estimated_insurance_cost, insurance_costs)
print(list(difference))



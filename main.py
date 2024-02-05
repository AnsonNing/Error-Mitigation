from heisenberg_circuit import constructHeisenbergCircuit
from circuit_execution import execute_circuit, generate_scaled_circuits
from plot_results import plot_measurement_results
from extrapolation_methods import xgboost_extrapolation, mlp_extrapolation, linear_extrapolation, exponential_extrapolation, richardson_extrapolation, cubic_spline_extrapolation, polynomial_extrapolation


circuit = constructHeisenbergCircuit(5, 2, 0.1, -0.2)


circuits = []
numberOfSteps = 5
num_measurements = 5 
n_qubits = circuit.num_qubits

scaled_circuits = generate_scaled_circuits(circuit, numberOfSteps)

measurement_results = []  

for i in range(numberOfSteps):
    current_circuit = scaled_circuits[i].copy() 
    current_circuit.measure_all()  
    
    step_measurements = []
    for j in range(num_measurements):
        measurement_result = execute_circuit(current_circuit, shots=5000)
        step_measurements.append(measurement_result)
    
    measurement_results.append(step_measurements)


step_max_values = []
step_min_values = []
step_avg_values = []

for measurements in measurement_results:
    all_values = [measurement[n_qubits * "0"] / 5000 for measurement in measurements]
    step_max_values.append(max(all_values))
    step_min_values.append(min(all_values))
    step_avg_values.append(sum(all_values) / num_measurements)

#print(step_max_values)
#print(step_min_values )
#print(step_avg_values)


#plot_measurement_results(numberOfSteps, num_measurements, measurement_results, circuit.num_qubits)

methods = [linear_extrapolation, exponential_extrapolation, richardson_extrapolation, cubic_spline_extrapolation, polynomial_extrapolation, mlp_extrapolation, xgboost_extrapolation]
labels = ["Linear", "Exponential", "Richardson", "Cubic Spline", "Polynomial", "MLP", "XGBoost"]

x = range(1, numberOfSteps + 1)

extrapolated_max = [method(step_max_values, x) for method in methods]
extrapolated_min = [method(step_min_values, x) for method in methods]
extrapolated_avg = [method(step_avg_values, x) for method in methods]


for i, label in enumerate(labels):
    #print(f"{label} Max Extrapolation: {extrapolated_max[i]}")
    print(f"{label} Min Extrapolation: {extrapolated_min[i]}")
    #print(f"{label} Avg Extrapolation: {extrapolated_avg[i]}")
    print()

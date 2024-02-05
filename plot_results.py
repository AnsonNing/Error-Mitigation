# plot_results.py

import matplotlib.pyplot as plt

def plot_measurement_results(number_of_steps, num_measurements, measurement_results, n_qubits):
    plt.figure(figsize=(15, 8))

    for i in range(1, number_of_steps + 1):  
        x_values = [i] * num_measurements  
        y_values = []  
        
        for j in range(num_measurements):
            y_values.append(measurement_results[i - 1][j][n_qubits * "0"] / 5000)
        
        plt.plot(x_values, y_values, marker='o', color='r', linestyle='None', markersize=1)

    plt.xticks(range(number_of_steps + 1))  
    plt.xlabel('Number of Steps')
    plt.ylabel('Measurement Results')
    plt.title('Measurement Results for Each Step and Extrapolated Values at Step 0')
    plt.legend()
    plt.grid()
    plt.show()

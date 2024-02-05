from mitiq.zne.scaling import fold_global
from qiskit.providers.fake_provider import FakeKolkata
from qiskit_aer import AerSimulator

def execute_circuit(circuit, shots):
    n_qubits = circuit.num_qubits
    noisy_backend = FakeKolkata()
    
    noisy_result = noisy_backend.run(circuit, shots=shots).result()
    noisy_counts = noisy_result.get_counts(circuit)
    noisy_expectation_value = noisy_counts[n_qubits * "0"] / shots
    return noisy_counts  

def generate_scaled_circuits(base_circuit, number_of_steps):
    circuits = []

    for i in range(1, number_of_steps + 1):
        trotter_circuit = fold_global(base_circuit, scale_factor=i)
        circuits.append(trotter_circuit)

    return circuits



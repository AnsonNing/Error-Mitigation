from qiskit.circuit import Parameter
from qiskit import QuantumCircuit

def constructHeisenbergCircuit(qubits, depth, rotation_x=0.1, rotation_z=-0.2):
    trotter_layer = QuantumCircuit(qubits)

    # RX gates layer
    trotter_layer.rx(rotation_x, range(qubits))

    # CX gates layer
    for i in range(0, qubits - 1, 2):
        trotter_layer.cx(i, i + 1)

    # RZ gates layer
    for i in range(1, qubits, 2):
        trotter_layer.rz(rotation_z, i)

    # CX gates layer
    for i in range(0, qubits - 1, 2):
        trotter_layer.cx(i, i + 1)

    # CX gates layer
    for i in range(1, qubits - 1, 2):
        trotter_layer.cx(i, i + 1)

    # RX gates layer
    for i in range(2, qubits, 2):
        trotter_layer.rz(rotation_z, i)

    # CX gates layer
    for i in range(1, qubits - 1, 2):
        trotter_layer.cx(i, i + 1)

    circuit = QuantumCircuit(qubits)
    for _ in range(depth):
        circuit = circuit.compose(trotter_layer)

    return circuit
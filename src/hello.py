import qiskit
from qiskit ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit IBMQ
from configparser import RawConfigParser

# Setup the API key for the real quantum computer.
parser = RawConfigParser()
parser.read('config.ini')
IBMQ.enable_account(parser.get('IBM', 'key'))

# Setup a qubit.
qr = QuantumRegister(1)
cr = ClassicalRegister(1)
program = QuantumCircuit(qr, cr);

# Measure the value of the qubit.
program.measure(qr, cr);

# Execute the program in the (simulator).
print("Running on the simulator: qasm_simulator")
job = qiskit.execute(program, qiskit.Aer.get_backend('qasm_simulator'), shots=100)
print("Result:", str(job.result().get_counts()))

# Execute the program on a (real quantum computer).
backend = qiskit.providers.ibmq.least_busy(qiskit.IBMQ.backends(simulator=False))
print("Running on real quantum computer: ", backend.name())
job = qiskit.execute(program, backend, shots=100)
print("Result:", str(job.result().get_counts()))

# print(program.qasm())
# qc.draw()

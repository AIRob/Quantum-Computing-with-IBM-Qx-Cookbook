#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:07:00 2019

@author: hnorlen
"""

from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, Aer, execute

from IPython.core.display import display

q = QuantumRegister(1)
c = ClassicalRegister(1)
qc = QuantumCircuit(q, c)

qc.x(q[0])
qc.h(q[0])
qc.measure(q, c)

display(qc.draw('mpl'))

backend = Aer.get_backend('qasm_simulator')
job_sim = execute(qc, backend, shots=1)
sim_result = job_sim.result()

counts = sim_result.get_counts(qc)
              
from qiskit.visualization import plot_histogram
display(plot_histogram(counts).show())
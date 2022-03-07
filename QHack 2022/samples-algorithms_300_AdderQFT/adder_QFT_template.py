#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml


def qfunc_adder(m, wires):
    """Quantum function capable of adding m units to a basic state given as input.
    Args:
        - m (int): units to add.
        - wires (list(int)): list of wires in which the function will be executed on.
    """
    #bit_string = bin(m)[2:]
    
   
    
    
        
    
    qml.QFT(wires=wires)

    # QHACK #
    for i in range(2**len(wires)):
        if m==i:#bit_string == bin(i)[2:]:
            alpha = i*2*np.pi/(2**len(wires))
            gamma = 1
            for wire in range(len(wires),0,-1):
                qml.RZ(gamma*alpha, wires=wire-1)
                
                gamma *= 2
    # QHACK #

    qml.QFT(wires=wires).inv()


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    m = int(inputs[0])
    n_wires = int(inputs[1])
    wires = range(n_wires)

    dev = qml.device("default.qubit", wires=wires, shots=1)

    @qml.qnode(dev)
    def test_circuit():
        # Input:  |2^{N-1}>
        qml.PauliX(wires=0)

        qfunc_adder(m, wires)
        return qml.sample()
    qml.draw_mpl(test_circuit)
    output = test_circuit()
    print(*output, sep=",")
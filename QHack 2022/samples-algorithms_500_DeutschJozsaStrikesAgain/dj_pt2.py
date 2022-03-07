#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml




def deutsch_jozsa(fs):
    """Function that determines whether four given functions are all of the same type or not.
    Args:
        - fs (list(function)): A list of 4 quantum functions. Each of them will accept a 'wires' parameter.
        The first two wires refer to the input and the third to the output of the function.
    Returns:
        - (str) : "4 same" or "2 and 2"
    """
    f1,f2,f3,f4 = fs
    
    dev = qml.device("default.qubit", wires=8, shots = 1)
    @qml.qnode(dev)
    def circuit():
        def oracle(func):
            qml.Barrier(wires=range(3))
            qml.broadcast(qml.Hadamard, wires=range(2), pattern="single")
            
            func(range(3))
            
            qml.broadcast(qml.Hadamard, wires=range(2), pattern="single")
            qml.Barrier(wires=range(3))
            
        
        # QHACK #
        qml.PauliX(2)
        
        oracle(f1)
        qml.MultiControlledX(control_wires=range(2), wires=3, control_values='00')
        
        
        qml.adjoint(oracle)(f1)
        oracle(f2)
        qml.MultiControlledX(control_wires=range(2), wires=4, control_values='00')
        
        qml.adjoint(oracle)(f2)
        oracle(f3)
        qml.MultiControlledX(control_wires=range(2), wires=5, control_values='00')
        
        qml.adjoint(oracle)(f3)
        oracle(f4)
        qml.MultiControlledX(control_wires=range(2), wires=6, control_values='00')
        
        
        qml.MultiControlledX(control_wires=range(3,7), wires=7, control_values='1111')
        qml.MultiControlledX(control_wires=range(3,7), wires=7, control_values='0000')
        
        return qml.sample(wires=7)#7
    
    bit = circuit()
    
    if bit:
        return "4 same"
    else:
        return "2 and 2"
    
    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    numbers = [int(i) for i in inputs]

    # Definition of the four oracles we will work with.

    def f1(wires):
        qml.CNOT(wires=[wires[numbers[0]], wires[2]])
        qml.CNOT(wires=[wires[numbers[1]], wires[2]])

    def f2(wires):
        qml.CNOT(wires=[wires[numbers[2]], wires[2]])
        qml.CNOT(wires=[wires[numbers[3]], wires[2]])

    def f3(wires):
        qml.CNOT(wires=[wires[numbers[4]], wires[2]])
        qml.CNOT(wires=[wires[numbers[5]], wires[2]])
        qml.PauliX(wires=wires[2])

    def f4(wires):
        qml.CNOT(wires=[wires[numbers[6]], wires[2]])
        qml.CNOT(wires=[wires[numbers[7]], wires[2]])
        qml.PauliX(wires=wires[2])

    output = deutsch_jozsa([f1, f2, f3, f4])
    
    #drawer = qml.draw_mpl(deutsch_jozsa)
    #drawer([f1,f2,f3,f4])
    print(f"{output}")
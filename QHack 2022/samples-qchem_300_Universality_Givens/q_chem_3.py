#! /usr/bin/python3

import sys
import numpy as np


def givens_rotations(a, b, c, d):
    """Calculates the angles needed for a Givens rotation to out put the state with amplitudes a,b,c and d

    Args:
        - a,b,c,d (float): real numbers which represent the amplitude of the relevant basis states (see problem statement). Assume they are normalized.

    Returns:
        - (list(float)): a list of real numbers ranging in the intervals provided in the challenge statement, which represent the angles in the Givens rotations,
        in order, that must be applied.
    """

    # QHACK #
    theta_1_half = np.arccos(np.sqrt(a**2 + d**2))
    if theta_1_half > np.pi/2:
        theta_1 = 2*theta_1_half - 2*np.pi
    elif theta_1_half < -np.pi/2:
        theta_1 = 2*theta_1_half + 2*np.pi
    else:
        theta_1 = 2*theta_1_half
        
        
    #sin_theta_2 = c / np.sin(theta_1/2)
    #theta_2 = np.arcsin(sin_theta_2)
    
    if b > 0:
        theta_1 = - theta_1
        cos_theta_2 = b/(np.sqrt(b**2+c**2))
    else:
        cos_theta_2 = -b/(np.sqrt(b**2+c**2))
    
    theta_2_half = np.arccos(cos_theta_2)
    
    #print(theta_2_half)

    if theta_2_half > np.pi/2:
        theta_2 = 2*theta_2_half - 2*np.pi
        #print(theta_2)
    elif theta_2_half < -np.pi/2:
        theta_2 = 2*theta_2_half + 2*np.pi
        #print(theta_2)
    else:
        theta_2 = 2*theta_2_half
        #print(theta_2)

    
    if c < 0 and theta_1 > 0:
        theta_2 = - theta_2
    elif c > 0 and theta_1 < 0:
        theta_2 = - theta_2
    
    cos_theta_3 = a / np.sqrt(a**2 + d**2)#np.cos(theta_1/2)
    theta_3_half = np.arccos(cos_theta_3)
    
    if theta_3_half > np.pi/2:
        theta_3 = 2*theta_3_half - 2*np.pi
    elif theta_3_half < -np.pi/2:
        theta_3 = 2*theta_3_half + 2*np.pi
    else:
        theta_3 = 2*theta_3_half
    
    
    if d > 0:
        theta_3 = - theta_3

    # if (np.cos(theta_1/2)*np.sin(theta_3/2) / d > 0) and (np.sin(theta_1/2)*np.cos(theta_2/2) / b > 0):
    #     theta_1 = - theta_1
    #     theta_2 = - theta_2
    #     theta_3 = - theta_3
    

    
    

        
    

    return (theta_1, theta_2, theta_3)
    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    theta_1, theta_2, theta_3 = givens_rotations(
        float(inputs[0]), float(inputs[1]), float(inputs[2]), float(inputs[3])
    )
    print(*[theta_1, theta_2, theta_3], sep=",")
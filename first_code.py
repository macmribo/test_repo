import math
import os
import sys

import numpy as np
import requests

tot_output = np.array([5000, 10000])
flow_tbl = np.array([[350, 400], [275, 100]])  # Flows table/intermediate table
# Technical coefficient matrix
mx_A = flow_tbl.dot(np.linalg.inv(tot_output * np.identity(2)))
# Technology matrix
mx_B = np.linalg.inv(np.identity(2) - mx_A)
print(mx_A)
print(mx_B)

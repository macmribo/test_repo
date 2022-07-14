import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as ss
import numpy as np
import seaborn as sns
from random import seed
from random import random


# c_w =  2.2
# lamb_w = 10
# tim =  np.random.rand(1, 20)
# l_min = 10

# def a_function(c_w, tim, lamb_w, l_min):
#   funcy = (c_w/lamb_w)*np.power(np.divide(tim-l_min, lamb_w), (c_w-1))*np.exp((-1)*np.power(np.divide(tim-l_min, lamb_w), c_w))
#   return funcy

# funcy = a_function(c_w, tim, lamb_w, l_min)

# fig1, ax1 = plt.subplots()
# ax1.scatter(tim, funcy)
# plt.show()

yiers = np.arange(2016, 2020)
# Landfill tipping fee
ltf = 3 * 10**(-29)*np.exp(0.0344*yiers)
print("Tipping fee in 2019 will be: {}".format(ltf[3]))

# fig2, ax2 = plt.subplots()
# ax2.scatter(yiers, ltf)
# plt.show()


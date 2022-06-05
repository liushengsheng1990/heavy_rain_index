import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
data = np.random.normal(0,10,100)
res_freq = stats.relfreq(data,numbins=20)
pdf_value = res_freq.frequency
cdf_value = np.cumsum(res_freq.frequency)


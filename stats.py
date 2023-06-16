import math
import numpy as np
import scipy.stats as stats

x = [10,8,13,9,11,14,6,4,12,7,5]
y = [8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]

print(f'mean_x: {np.mean(x)}')
print(f'mean_y: {np.mean(y)}')


print(f'std_x: {np.std(x)}')
print(f'std_y: {np.std(y)}')

print(f'coercoeff_x_y: {np.corrcoef(x, y)}')

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

x1 = [10,8,13,9,11,14,6,4,12,7,5]
y1= [9.14,8.14,8.74,8.77,9.26,8.1,6.13,3.1,9.13,7.26,4.74]

print(f'mean_x: {np.mean(x)}')
print(f'mean_y: {np.mean(y)}')


print(f'std_x1: {np.std(x1)}')
print(f'std_y1: {np.std(y1)}')

print(f'coercoeff_x1_y1: {np.corrcoef(x1, y1)}')

x2=[10,8,13,9,11,14,6,4,12,7,5]
y2=[7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73]

print(f'mean_x2: {np.mean(x2)}')
print(f'mean_y2: {np.mean(y2)}')


print(f'std_x2: {np.std(x2)}')
print(f'std_y2: {np.std(y2)}')

print(f'coercoeff_x2_y2: {np.corrcoef(x2, y2)}')

x3=[8,8,8,8,8,8,8,19,8,8,8]
y3=[6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.5,5.56,7.91,6.89]

print(f'mean_x3: {np.mean(x3)}')
print(f'mean_y3: {np.mean(y3)}')


print(f'std_x3: {np.std(x3)}')
print(f'std_y3: {np.std(y3)}')

print(f'coercoeff_x3_y3: {np.corrcoef(x3, y3)}')
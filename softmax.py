import numpy as np
x = np.array([8,4,9,11,13])
def softmax(x):
    row_max = max(x) # read max of all row 
    x= x - row_max # read x - max x 
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp)
    s = x_exp / x_sum
    return s
output = softmax(x)
for n in range(len(output)):
    print('{} -> {}'.format(x[n], output[n]))
print('sum = ',np.sum(output))
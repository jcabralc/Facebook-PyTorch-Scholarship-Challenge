import numpy as np
X = [[1,1],[2,4],[5,-5],[-4,5]]
for x in X:
    score = 4*x[0] + 5*x[1] - 9
    sigmoidX = 1.0/(1 + np.exp(-score))
    print('{0} has probability of {1:.2f}%'.format(x,round(sigmoidX * 100)))
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
np.random.seed(2)

def load_csv(file_path):
    return pd.read_csv(file_path)


df = load_csv("datasets/financial.csv")
X_train, X_test, y_train, y_test = train_test_split(np.array(df["Marketing"]), np.array(df["Sales"]), test_size=0.2, random_state=42)
input_data = X_train.reshape(1, len(X_train)).T
real_outcome = y_train.reshape(1, len(y_train)).T

X = input_data
# Building Xbar 
one_matrix = np.ones((input_data.shape[0], 1))
Xbar = np.concatenate((one_matrix, input_data), axis = 1)
y = real_outcome

A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w_lr = np.dot(np.linalg.pinv(A), b)
print('Solution found by formula: w = ',w_lr.T)

# Display result
w = w_lr
w_0 = w[0][0]
w_1 = w[1][0]

# Draw the fitting line 
# plt.plot(X.T, y.T, 'b.')     # data 
# plt.plot(X_test, w_0 + X_test*w_1, 'r')   # the fitting line
# plt.show()

def grad(w):
    N = Xbar.shape[0]
    return 1/N * Xbar.T.dot(Xbar.dot(w) - y)

def cost(w):
    N = Xbar.shape[0]
    return .5/N*np.linalg.norm(y - Xbar.dot(w), 2)**2

def numerical_grad(w, cost):
    eps = 1e-4
    g = np.zeros_like(w)
    for i in range(len(w)):
        w_p = w.copy()
        w_n = w.copy()
        w_p[i] += eps 
        w_n[i] -= eps
        g[i] = (cost(w_p) - cost(w_n))/(2*eps)
    return g 

def check_grad(w, cost, grad):
    w = np.random.rand(w.shape[0], w.shape[1])
    grad1 = grad(w)
    grad2 = numerical_grad(w, cost)
    return True if np.linalg.norm(grad1 - grad2) < 1e-6 else False 

print( 'Checking gradient...', check_grad(np.random.rand(2, 1), cost, grad))

def myGD(w_init, grad, eta, gamma = 0.9):
    w = [w_init]
    for it in range(100):
        w_new = w[-1] - eta*grad(w[-1])
        if np.linalg.norm(grad(w_new))/len(w_new) < 1e-3:
            break 
        w.append(w_new)
    return (w, it) 

def has_converged(theta_new, grad):
    return np.linalg.norm(grad(theta_new))/len(theta_new) < 1e-3

def GD_momentum(theta_init, grad, eta, gamma):
    # Suppose we want to store history of theta
    theta = [theta_init]
    v_old = np.zeros_like(theta_init)
    for it in range(100000):
        v_new = gamma*v_old + eta*grad(theta[-1])
        theta_new = theta[-1] - v_new
        if has_converged(theta_new, grad):
            break 
        theta.append(theta_new)
        v_old = v_new
    return theta[-1], it 

w_init = np.array([[2], [1]])
(w1, it1) = GD_momentum(w_init, grad, 0.0001, 0.9)
print('Solution found by GD: w = ', w1, ',\nafter %d iterations.' %(it1+1))

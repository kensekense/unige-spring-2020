import numpy as np
import random

# TODO: import softmax, sigmoid and gradcheck_naive from your external
# python modules
from softmax import softmax
from sigmoid import sigmoid, sigmoid_grad
from gradcheck import gradcheck_naive


def forward_backward_prop(data, labels, params, dimensions):
    """
    Forward and backward propagation for a two-layer sigmoidal network

    Compute the forward propagation and for the cross entropy cost,
    and backward propagation for the gradients for all parameters.
    """

    ### Unpack network parameters (do not modify)
    ofs = 0
    Dx, H, Dy = (dimensions[0], dimensions[1], dimensions[2])

    W1 = np.reshape(params[ofs:ofs+ Dx * H], (Dx, H))
    ofs += Dx * H
    b1 = np.reshape(params[ofs:ofs + H], (1, H))
    ofs += H
    W2 = np.reshape(params[ofs:ofs + H * Dy], (H, Dy))
    ofs += H * Dy
    b2 = np.reshape(params[ofs:ofs + Dy], (1, Dy))

    ### YOUR CODE HERE: forward propagation, computing h, y, cost
    h = sigmoid(np.matmul(data,W1)+b1)
    y = softmax(np.matmul(h,W2)+b2)
    cost = -1*np.sum(labels*np.log(y)) #cross entropy loss?

    ### END YOUR CODE

    ### YOUR CODE HERE: backward propagation, computing the gradient
    grady = (y-labels)
    gradW2 = np.matmul(h.T,grady)
    gradb2 = np.sum(grady, axis=0)
    gradh = np.matmul(grady,W2.T)
    gradz1 = np.multiply(sigmoid_grad(h),gradh)
    gradW1 = np.matmul(data.T, gradz1)
    gradb1 = np.sum(gradz1, axis=0)

    ### END YOUR CODE

    ### Stack gradients (do not modify)
    grad = np.concatenate((gradW1.flatten(), gradb1.flatten(),
        gradW2.flatten(), gradb2.flatten()))

    return cost, grad

def sanity_check():
    """
    Set up fake data and parameters for the neural network, and test using
    gradcheck.
    """
    print('Running sanity check...')

    N = 20
    dimensions = [10, 5, 10]
    data = np.random.randn(N, dimensions[0])   # each row will be a datum
    labels = np.zeros((N, dimensions[2]))
    for i in range(N):
        labels[i,random.randint(0, dimensions[2]-1)] = 1

    params = np.random.randn((dimensions[0] + 1) * dimensions[1] + (
        dimensions[1] + 1) * dimensions[2], )

    gradcheck_naive(lambda params: forward_backward_prop(data, labels, params,
        dimensions), params)


def your_sanity_checks():
    """
    Use this space add any additional sanity checks by running:
        python q2_neural.py
    This function will not be called by the autograder, nor will
    your additional tests be graded.
    """
    print('Running your sanity checks...')
    ### YOUR CODE HERE

    ### END YOUR CODE


if __name__ == '__main__':
    sanity_check()
    your_sanity_checks()

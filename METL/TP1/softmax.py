import numpy as np


def softmax(x):
    """
    Compute the softmax function for each row of the input x.

    It is crucial that this function is optimized for speed because
    it will be used frequently in later code.
    You might find numpy functions np.exp, np.sum, np.reshape,
    np.max, and numpy broadcasting useful for this task. (numpy
    broadcasting documentation:
    http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

    You should also make sure that your code works for one
    dimensional inputs (treat the vector as a row), you might find
    it helpful for your later problems.
    """
    # YOUR CODE HERE
    max_i = np.max(x, axis=-1, keepdims=True)
    return np.exp(x - max_i)/np.sum(np.exp(x - max_i), axis=-1, keepdims=True)

def test_softmax_basic():
    """
    Some simple tests to get you started.
    Warning: these are not exhaustive.
    """
    print('Running basic tests...')
    test1 = softmax(np.array([1, 2]))
    print(test1)
    assert np.amax(np.fabs(test1 - np.array(
        [0.26894142, 0.73105858]))) <= 1e-6

    test2 = softmax(np.array([[1001, 1002], [3, 4]]))
    print(test2)
    assert np.amax(np.fabs(test2 - np.array(
        [[0.26894142, 0.73105858], [0.26894142, 0.73105858]]))) <= 1e-6

    test3 = softmax(np.array([[-1001, -1002]]))
    print(test3)
    assert np.amax(np.fabs(test3 - np.array(
        [0.73105858, 0.26894142]))) <= 1e-6

    #print('You should verify these results!\n')


def test_softmax():
    """
    Use this space to test your softmax implementation by running:
        python3 softmax.py
    """
    #print('Running your tests...')
    # YOUR CODE HERE
    from scipy.special import softmax as ss #disclaimer, only for testing purposes
    import time

    obtained = softmax(np.array([1]))
    print(obtained)
    resy = ss(np.array([1]))
    assert np.amax(np.fabs(obtained - resy) <= 1e-6)

    obtained = softmax(np.array([1,2,3,4,5]))
    print(obtained)
    resy = ss(np.array([1,2,3,4,5]))
    assert np.amax(np.fabs(obtained - resy) <= 1e-6)

    start = time.clock()
    calc = softmax(np.array([[1000,2,3],[4,5,6],[7,8,9],[1,2,3]]))
    end = time.clock()
    our_time = end-start
    start = time.clock()
    calc = ss(np.array([[1000,2,3],[4,5,6],[7,8,9],[1,2,3]]))
    end = time.clock()
    their_time = end-start
    consideration_for_speed = our_time - their_time
    print("time difference: ", consideration_for_speed)

    print("Tests passed")

if __name__ == '__main__':
    test_softmax_basic()
    test_softmax()

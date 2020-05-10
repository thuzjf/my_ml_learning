import numpy as np



def loss_func(y, g):
    return 0.5 * (y - g)**2

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def derivative_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))

def train(x, g, lr):
    epoch = 0
    losses = []
    w = np.random.rand(10)
    while epoch < 150:
        for i in range(x.shape[1]):
            beta = np.dot(w, x[:, i])
            y = sigmoid(beta)
            loss = loss_func(y, g[i])
            losses.append(loss)
            d = (y - g[i]) * derivative_sigmoid(beta) * x[:, i]
            w -= lr * d
            # print("epoch:{}, batch:{}, loss:{}".format(epoch, i, loss))
        epoch += 1
    return w, losses


if __name__ == '__main__':

    x = np.random.randn(10,600)
    g = (x.sum(0) > 0).astype(np.int32)
    lr = 0.05

    w, losses = train(x, g, lr=lr)

    # import matplotlib.pyplot as plt
    # plt.plot(np.array(losses))


    x1 = np.random.randn(10, 40)
    g1 = (x1.sum(0) > 0).astype(np.int32)
    for i in range(x1.shape[1]):
        pred = sigmoid(np.dot(w, x1[:,i]))
        print("ground_truth:{}, pred:{:.1f}, {}".format(g1[i], pred, 'right' if abs(g1[i]-pred)< 0.5 else 'wrong'))

import matplotlib.pyplot as plt
import numpy as np

def sincosgraph(period):
    x = np.arange(0,period,0.1)
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x,y,x,z)


if __name__ == '__main__':
    sincosgraph(2*np.pi)
    plt.xlabel('x values')
    plt.ylabel('sin(x) and cos(x) values')
    plt.title('Sin(x) and Cos(x) Graphs')
    plt.legend(['sin(x)', 'cos(x)'])
    plt.show()

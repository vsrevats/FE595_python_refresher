import matplotlib.pyplot as plt
import numpy as np

def sincosgraph(period):
    x = np.arange(0,period,0.1)
    y = np.sin(x)
    z = np.cos(x)
    v = np.tan(x)
    plt.plot(x,y,x,z,x,v)


if __name__ == '__main__':
    sincosgraph(2*np.pi)
    plt.xlabel('x values')
    plt.ylabel('sin(x), cos(x) and tan(x) values')
    plt.title('Sin(x), Cos(x) and Tan(x) Graphs')
    plt.legend(['sin(x)', 'cos(x)', 'tan(x)'])
    plt.show()

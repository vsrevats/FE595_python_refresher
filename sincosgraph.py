import matplotlib.pyplot as plt
import numpy as np

def sincosgraph(period):
    x = np.arange(0,period,0.1)
    y = np.sin(x)
    z = np.cos(x)
    t = np.tan(x)
    plt.plot(x,y,x,z,x,t)


if __name__ == '__main__':
    sincosgraph(2*np.pi)
    plt.xlim(0, 2 * np.pi)
    plt.ylim(-2, 2)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.title('Sin(x), Cos(x) and Tan(x) Graphs')
    plt.legend(['sin(x)', 'cos(x)', 'tan(x)'])
    plt.show()

#-*- coding;utf-8 -*-
#複数のグラフをmatplotlibを用いて表示
#http://retrofocus28.blogspot.com/2012/06/matplotlib-2.html
#https://qiita.com/kenichiro_nishioka/items/8e307e164a4e0a279734#
#https://www.sejuku.net/blog/61011

from matplotlib.pyplot import figure, show
#import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand

def main():
    fig = figure()
    #fig= plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(rand(10))
    ax1.set_yticks(np.arange(0,1.1,0.1))

    ax2 = fig.add_subplot(212)
    ax2.plot(rand(10),'o')
    show()


if __name__ == "__main__":
    main()

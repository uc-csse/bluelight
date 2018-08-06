import numpy as np
import pylab

data = np.frombuffer(open('out.bin','rb').read(),dtype='uint8')

dt=1.0/32000 * 1000#msec

pylab.plot(np.arange(0,len(data)*dt,dt),data)
pylab.show()

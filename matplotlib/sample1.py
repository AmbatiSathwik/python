import matplotlib.pyplot as plt
import numpy as np


#input only y values
plt.plot([1,2,3,9])
plt.show()

#input both x,y values string ro indicates as red circle
#no string default as blue line
plt.plot([1,2,3,4],[4,8,6,7],'ro')
plt.show()

#axis takes [x_min,x_max,y_min,y_max]
plt.plot([1,2,3,4],[4,8,6,7])
plt.axis([0,8,0,10])
plt.show()

array = np.array([0,1,2,3,4,5,6,7,8,9,10])
#red dashes blue squares green triangles 
plt.plot(array,array*2,'r--',array,array**2,'bs',array,array**3,'g^')
plt.show()

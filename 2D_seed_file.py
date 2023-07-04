# Basic packages
import numpy as np
import matplotlib.pyplot as plt

# font setting
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams["font.family"] = "Times New Roman"

# save path setting
import os
if not os.path.exists('Illustration'):
    os.makedirs('Illustration')

# function
def f(x):
    return x**2

# domain
x = np.linspace(-10, 10, 400)

# visualization
plt.figure(figsize=(6, 6))                                                
plt.plot(x, f(x), label='$y = x^2$', color='blue')                        
plt.xlabel('$x$', fontsize=11)                                            
plt.ylabel('$y$', fontsize=11)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid()
plt.legend()
plt.title('Plot of $y = x^2$', fontsize=11)
plt.savefig('Illustration/Figure 1.png', dpi=600, bbox_inches='tight')
plt.show()
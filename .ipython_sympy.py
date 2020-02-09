import pyperclip
from sympy import *
init_printing()

x,y,z = symbols('x, y, z')
a,b,c = symbols('a, b, c')
t = symbols('t')
phi,rho,theta = symbols('phi, rho, theta')

def texcpy():
    pyperclip.copy(latex(_))

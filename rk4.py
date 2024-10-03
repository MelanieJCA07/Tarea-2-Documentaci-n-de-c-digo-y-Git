import numpy as np
import matplotlib.pyplot as plt

def dyn_generator(oper, state):
    """ -i[O,y(t)].

    "O" es el  operador, i la variable compleja, "y(t)" es la funcion dependiente del tiempo.

    Examples:
        oOper operador lineal.
        yInit estado inicial.

        >>> oOper = np.array([[0, 1], [1, 0]])
        >>> yInit = np.array([[1, 0], [0, 0]])
        >>> dyn_generator(oOper, yInit)
       
    Args:
        oper (Numpy array): primer argumento (operador).
        state (Numpy array): Segundo argumento (estado).

    Returns:
    (Numpy array): Nos  devuelve el resultado luego de utilizar el operador -i[A.B] = -i(AB - BA).
    """
    return (np.dot(oper, state) - np.dot(state, oper)) * (-1.0j)

def rk4(func, oper, state, h):
    """ Runge-Kutta 4, el metodo numerico en el que se basa el código.

    Args:
        func (Function): primer argumento. Es la funcion a la que se le aplica el Rk4 obtenido de la función anterior.
        oper (Numpy array): Segundo argumento (operador lineal)
        state (Numpy array): Tercer argumento. Donde se reflejan las iteraciones, ya que es donde se cambia el estado inicial con el paso del tiempo.
        h (float): paso temporal

    Returns:
        (Numpy array): Devuelve el estado del sistema dinamico.
    Examples:
        >>> oOper = np.array([[0, 1], [1, 0]])
        >>> yInit = np.array([[1, 0], [0, 0]])
        >>> times=np.linspace(0,10,150)
        >>> h= times[1]-times[0]
        >>> print(rk4(dyn_generator,oOper, yInit, h))

    """
    k1 = h*func(oper,state)
    k2 = h*func(oper,state+(k1/2))
    k3 = h*func(oper,state+(k2/2))
    k4 = h*func(oper,state+k3)
    return state + (1/6)*(k1+(2*k2)+(2*k3)+k4)

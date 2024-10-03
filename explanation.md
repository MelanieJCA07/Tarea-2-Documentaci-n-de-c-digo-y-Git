# Explanation
En este programa, utilizaremos el método Runge-Kutta de orden 4, el cual es un método iterativo donde cada repetición nos da un punto temporal, los cuales se grafican para obtener una solución, esta estimación a la solución a un punto temporal, se realiza de la siguiente forma:

$$

    \\begin{aligned}
        y_n+1  = y_n +  \\frac{1}{6}(k_1 +2k_2 +2k_3 +k_4)
        k_1 = h*f(t_n , y_n ) \\\\
        k_2 = h*f(t_n + h/2 , y_n + (k_1)/2)\\\\
        k_3 = h*f(t_n + h/2 , y_n + (k_2)/2)\\\\
        k_4 = h*f(t_n + h , y_n + k_3)\\\\
    \\end{aligned}\n"
$$

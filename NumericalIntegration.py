import math as m
import numpy as np

def newton(f,Df,x0,epsilon,max_iter): 
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

def secant(f,a,b,N):
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print('Found solution after',n,'iterations.')
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))

def felezo(f,a,b,e,max_iter):
    n = 0
    while n < max_iter:
        c = (a + b) / 2
        if np.sign(f(c)) == np.sign(f(b)):
            b = c
        else:
            a = c
        if np.abs(a-b) < e:
            break
        n += 1
    print('Found solution after', n, 'iterations.')
    return c

def hur(f,a,b,epsilon,max_iter):
    for n in range(0, max_iter):
        c = b-f(b)*(b-a)/(f(b)-f(a))
        if np.sign(f(c)) == np.sign(f(b)):
            b = c
        else:
            a = c
        if np.abs(a-b) < epsilon:
            break
    print('Found solution after', n, 'iterations.')
    return c

def steffensen( f, x, a, epsilon, maxiter ):
    x1 = x + 8.0 * epsilon
    x0 = x + 4.0 * epsilon
    k = 0
    while k <= maxiter and abs( x - x0 ) >= epsilon:
        x2, x1, x0 = ( x1, x0, x )
        p1 = x  + a * f( x )
        p2 = p1 + a * f( p1 )
        x = x - ( ( p1 - x )**2 ) / ( p2 - 2 * p1 + x )
        k = k + 1
    if k > maxiter:
        print ("Error: exceeded %d iterations" % maxiter)
    rate = m.log( abs((x - x0) / (x0 - x1)) ) / \
           m.log( abs((x0 - x1) / (x1 - x2)) )
    print('Found solution after',k,'iterations.')
    return x

if __name__ == "__main__":
    
    maxiter = 1000
    epsilon = 1e-6

    f = lambda x: m.exp( x ) - 1
    df = lambda x: m.exp( x ) + 1

    print ("Finding root of f(x) = exp(x) - 1") 

    print ("\nNewton módszer:")
    x = newton( f, df, -1.5, epsilon, maxiter )
    print ("root = ", x)

    print ("\nFelező módszer:")
    x = felezo( f, -1, 2, epsilon, maxiter )
    print ("root = ", x)

    print ("\nHúr módszer:")
    x = hur( f, -1, 2, epsilon, maxiter )
    print ("root = ", x)

    print ("\nSzelő módszer:")
    x = secant( f, -1, 2, maxiter )
    print ("root = ", x)

    print ("\nSteffensen-féle módszer:")
    dfr = 2 * epsilon / ( f( x - epsilon ) - f( x + epsilon ) )
    x = steffensen( f, -1.5, dfr, epsilon, maxiter )
    print ("root = ", x)

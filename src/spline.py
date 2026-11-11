"""Spline cúbico natural paramétrico con parámetro centrípeto."""
import math
import numpy as np

def parametro_centripeto(puntos):
    t = [0.0]
    for p, q in zip(puntos[:-1], puntos[1:]):
        t.append(t[-1] + math.sqrt(float(np.linalg.norm(q-p))))
    return np.array(t, dtype=float)

def segundo_coeficiente(t, y):
    n = len(t)-1
    h = np.diff(t)
    m = n-1
    if m <= 0:
        return np.zeros(n+1)
    a = h[:-1].copy()
    b = 2*(h[:-1]+h[1:])
    c = h[1:].copy()
    r = 3*((y[2:]-y[1:-1])/h[1:]-(y[1:-1]-y[:-2])/h[:-1])
    for i in range(1, m):
        w = a[i]/b[i-1]
        b[i] -= w*c[i-1]
        r[i] -= w*r[i-1]
    z = np.zeros(m)
    z[-1] = r[-1]/b[-1]
    for i in range(m-2, -1, -1):
        z[i] = (r[i]-c[i]*z[i+1])/b[i]
    return np.r_[0, z, 0]

def coeficientes(t, y):
    h = np.diff(t)
    c = segundo_coeficiente(t, y)
    a = y[:-1]
    b = np.diff(y)/h - h*(2*c[:-1]+c[1:])/3
    d = np.diff(c)/(3*h)
    return np.column_stack((a,b,c[:-1],d))

def construir(puntos):
    p = np.asarray(puntos, dtype=float)
    if p.ndim != 2 or p.shape[1] != 2 or len(p) < 3:
        raise ValueError("Se requieren al menos 3 puntos bidimensionales.")
    if np.any(np.linalg.norm(np.diff(p, axis=0), axis=1) == 0):
        raise ValueError("Hay puntos consecutivos repetidos.")
    t = parametro_centripeto(p)
    return t, coeficientes(t,p[:,0]), coeficientes(t,p[:,1])

def evaluar(t, C, valores):
    valores = np.asarray(valores, dtype=float)
    salida = np.empty(valores.shape)
    for k, s in np.ndenumerate(valores):
        i = min(np.searchsorted(t[1:], s, side="right"), len(t)-2)
        u = s-t[i]
        a,b,c,d = C[i]
        salida[k] = a+b*u+c*u*u+d*u**3
    return salida

def errores_continuidad(t, cx, cy):
    errores = np.zeros(3)
    for i in range(1,len(t)-1):
        h = t[i]-t[i-1]
        for C in (cx,cy):
            a,b,c,d = C[i-1]
            izq = [a+b*h+c*h**2+d*h**3,
                   b+2*c*h+3*d*h**2,
                   2*c+6*d*h]
            a,b,c,d = C[i]
            der = [a,b,2*c]
            errores = np.maximum(errores, np.abs(np.array(izq)-np.array(der)))
    return dict(zip(("C0","C1","C2"), map(float, errores)))

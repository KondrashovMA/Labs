import math
import numpy
def makeDataKatkovNumpy ():
    '''
    Возвращает numpy массивы осей х1, х2 и z
    :return:
    '''
    x = numpy.arange (-2.5, 2.6, 0.01)
    y = numpy.arange (-2.5, 2.6, 0.01)
    xgrid, ygrid = numpy.meshgrid(x, y)
    A = 0.8
    zgrid = 0.5 * (xgrid ** 2 + ygrid ** 2) * \
            (2 * A + A *numpy.cos(1.5 * xgrid) *numpy.cos(3.14 * ygrid) + A * numpy.cos(numpy.sqrt(5)*xgrid)*numpy.cos(3.5*ygrid))
    #zgrid = numpy.sin (xgrid) * numpy.sin (ygrid) / (xgrid * ygrid)
    return xgrid, ygrid, zgrid
import sympy as smp
import math
import random


def makeKatkov(x1Crd=0, x2Crd=0):
    '''
    Вычисляет значение функции Каткова в одной точке
    :param x1Crd:
    :param x2Crd:
    :return:
    '''
    x1, x2 = smp.symbols('x1 x2')
    A = 0.8
    z = 0.5 * (x1 ** 2 + x2 ** 2) * \
            (2 * A + A *smp.cos(1.5 * x1) *smp.cos(3.14 * x2) + A * smp.cos(math.sqrt(5)*x1)*smp.cos(3.5*x2))
    res = z.subs([(x1, x1Crd), (x2, x2Crd)])
    return res

def makeDiiff (x1Crd=0, x2Crd=0, var = 1):
    '''
    Значение производной функции каткова по одной из координат
    :param x1Crd:
    :param x2Crd:
    :param var:
    :return:
    '''
    x1, x2 = smp.symbols('x1 x2')
    A = 0.8
    z = 0.5 * (x1 ** 2 + x2 ** 2) * \
            (2 * A + A *smp.cos(1.5 * x1) *smp.cos(3.14 * x2) + A * smp.cos(math.sqrt(5)*x1)*smp.cos(3.5*x2))
    if var==1:
        diffZ = smp.diff(z, x1)
        res = diffZ.subs([(x1, x1Crd), (x2, x2Crd)])
    elif var==2:
        diffZ = smp.diff(z, x2)
        res = diffZ.subs([(x1, x1Crd), (x2, x2Crd)])
    return res
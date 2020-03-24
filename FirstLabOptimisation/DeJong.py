import math
import numpy
def makeDataDeJongNumpy ():
    '''
    Возвращает numpy массивы осей х1, х2 и z
    :return:
    '''
    x = numpy.arange (-5, 5, 0.01)
    y = numpy.arange (-5, 5, 0.01)
    xgrid, ygrid = numpy.meshgrid(x, y)

   # X, Y = np.meshgrid(xs,ys)
    #Z = X - 1.4*Y + np.power(np.e, (0.01*X*X + 0.11*Y*Y))

    zgrid = 100 + (-100/(100*(numpy.power(xgrid,2) - ygrid) + numpy.power((1 - xgrid),2) ) )
    #zgrid = -100 / (100 * (numpy.power(xgrid,2) + numpy.power(ygrid,2)) + (1 - numpy.power(xgrid,2))) + 100

    #zgrid = numpy.sin (xgrid) * numpy.sin (ygrid) / (xgrid * ygrid)

    return xgrid, ygrid, zgrid
import sympy as smp
import math


def makeDeJong(x1Crd=0, x2Crd=0):
    '''
    Вычисляет значение функции Каткова в одной точке
    :param x1Crd:
    :param x2Crd:
    :return:
    '''
    x1, x2 = smp.symbols('x1 x2')

    #z = -100/(100 * (x1**2 + x2**2) + (1 - x1**2)) + 100
    z = -100 / (100 * (x1 ** 2 - x2) + (1 - x1)**2 ) + 100

    res = z.subs([(x1, x1Crd), (x2, x2Crd)])
    return res

def makeDeJongDiiff (x1Crd=0, x2Crd=0, var = 0):
    '''
    Значение производной функции каткова по одной из координат
    :param x1Crd:
    :param x2Crd:
    :param var:
    :return:
    '''
    x1, x2 = smp.symbols('x1 x2')
    #z = -100/(100 * (x1**2 + x2**2) + (1 - x1**2)) + 100
    z = -100 / (100 * (x1 ** 2 - x2) + (1 - x1) ** 2 ) + 100
    if var==1:
        diffZ = smp.diff(z, x1)
        res = diffZ.subs([(x1, x1Crd), (x2, x2Crd)])
    elif var==2:
        diffZ = smp.diff(z, x2)
        res = diffZ.subs([(x1, x1Crd), (x2, x2Crd)])
    return res
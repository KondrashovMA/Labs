#поиск минимума градиентым методом
import math
import random

import KatkovFunctions as ktk
#import DeJong as dj

def gradient():
    x1 = random.uniform(-2.5, 2.5)
    x2 = random.uniform(-2.5, 2.5)
    #x1 = random.uniform(-5, 5) #текущие значения
    #x2 = random.uniform(-5, 5)
    limit = 2.5

    lastX1, lastX2 = x1,x2 #значения на предыдущем шаге


    func = ktk.makeKatkov(x1, x2)
    #func = dj.makeDeJong(x1, x2)  # текущее значение функции

    q = 0.5
    eps = 10e-5
    #print("стартовое значение функции = ",func , " координаты х1, х2 ", x1, " ",x2)

    lastFunc = func #значение функции на предыдущем шаге
    for i in range(140):
        diffX1 = ktk.makeDiiff(x1,x2,1)
        diffX2 = ktk.makeDiiff(x1,x2,2)
        #diffX1 = dj.makeDeJongDiiff(x1, x2, 1)
        #diffX2 = dj.makeDeJongDiiff(x1, x2, 2)

        grad = math.sqrt(diffX1**2 + diffX2**2)
        x1 = x1 - q*diffX1
        x2 = x2 - q*diffX2

        if (not(x1<limit) or not(x1>-limit) or not(x2<limit) or not(x2>-limit)):
            x1 = lastX1
            x2 = lastX2
            func = lastFunc
            q = q / 2
            continue

        func = ktk.makeKatkov(x1,x2)
        #func = dj.makeDeJong(x1, x2)

        if(func>lastFunc): # если значение функции на шаге больше предыдущего, то возвращаемся назад и уменьшаем q
            x1 = lastX1
            x2 = lastX2
            func = lastFunc
            q = q/2
        else:
            lastFunc = func
            lastX1, lastX2 = x1, x2

        if ( grad < eps ):
            break

        print("функция на шаге  ",i," func = ",func, " координаты х1 =  ", x1, " x2 = ",x2, " grad = ",grad," q = ",q)

    return x1, x2, func

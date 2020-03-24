#поиск минимума методом имитации отжига
import random
import KatkovFunctions as ktk
import math
#import DeJong as dj

def decreaseTempBolc(tmp,i):
    return tmp/math.log(1+i,math.e) #по закону Коши

def decreaseTempKosh(tmp,i):
    return tmp/(1+i) #по закону Коши

def decreaseTempLine(tmp, i):
    return tmp*0.8

def getProbality(dE, tmp):
    #return 1/(1+math.exp(dE/tmp))
    return math.exp(-dE/tmp)

def SimulatedAnnealing():
    Tmax = 200
    Tmin = 0.01

    x1 = random.uniform(-2.5, 2.5)
    x2 = random.uniform(-2.5, 2.5)
    x1Res, x2Res = x1,x2

    limit = 2.5

    zRes = ktk.makeKatkov(x1,x2)
    #zRes = dj.makeDeJong(x1,x2)


    Ti = Tmax
    i=1
    q=0.15
    while(Ti>Tmin):

        diffX1 = ktk.makeDiiff(x1, x2, 1)
        diffX2 = ktk.makeDiiff(x1, x2, 2)
        #diffX1 = dj.makeDeJongDiiff(x1, x2, 1)
        #diffX2 = dj.makeDeJongDiiff(x1, x2, 2)

        x1 = -random.uniform(0, 0.4) * diffX1
        x2 = -random.uniform(0, 0.4) * diffX2

        if (not(x1<limit) or not(x1>-limit) or not(x2<limit) or not(x2>-limit)): #если вылетели за пределы функции
            x1, x2 = x1Res, x2Res
            Ti = decreaseTempKosh(Ti, i)
            # Ti = decreaseTempBolc(Ti, i)
            # Ti = decreaseTempLine(Ti, i)
            continue
        #x1 = random.uniform(-5, 5)
        #x2 = random.uniform(-5, 5)


        #z = dj.makeDeJong(x1, x2)
        z = ktk.makeKatkov(x1, x2)

        dE = z - zRes

        if(dE<0):
            x1Res, x2Res = x1, x2
            zRes = z
            P = None
            value = None

        else:
            P = getProbality(dE,Ti)
            value = random.uniform(0,1)
            if(value<=P):
                x1Res, x2Res = x1, x2
                zRes = z
        #if(math.fabs(dE)<eps):
        #    break
        Ti = decreaseTempKosh(Ti, i)

        #Ti = decreaseTempBolc(Ti, i)

        #Ti = decreaseTempLine(Ti, i)

        print("Итерация ", i, " температура = ", Ti, " x1 = ", x1, " x2 = ", x2, " z = ", z,
              " P = ", P, " value= ", value, "zRes = ",zRes)

        i = i + 1

    #print("результат при максимальной температуре = ", Tmax)
    #print(" x1 = ",x1Res," x2 = ",x2Res," z = ",zRes)
    return x1Res, x2Res, zRes


import matplotlib.pyplot as plt
import Gradient as grad
import SimulatedAnnealing as sim


import KatkovFunctions as kt
#import DeJong as dj

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


x,y,z = kt.makeDataKatkovNumpy()
#x,y,z = dj.makeDataDeJongNumpy()

fig = plt.figure()


x1grad, x2grad, zgrad = grad.gradient()
x1Sim, x2Sim, zSim = sim.SimulatedAnnealing()

#print(type(x1grad), type(x2grad), type(zgrad))

#print(type(x1Sim), type(x2Sim), type(zSim))


ax = fig.add_subplot(111, projection='3d')




fig1 = ax.scatter(float(x1grad), float(x2grad), float(zgrad), s=90.0,c = "red")


fig2 = ax.scatter(float(x1Sim), float(x2Sim), float(zSim), s=90.0,c = "blue")


fig3 = ax.plot_wireframe(x,y,z)

#приведение к float для окгругления
x1grad = float(x1grad); x2grad = float(x2grad); zgrad = float(zgrad)
x1Sim = float(x1Sim); x2Sim = float(x2Sim); zSim = float(zSim)

coordGrad ="(" + str(toFixed(x1grad,2))+", "+str( toFixed(x2grad,2) ) +", "+str( toFixed(zgrad,2)) +")"
coordSim ="(" + str(toFixed(float(x1Sim),2))+", "+str( toFixed(float(x2Sim),2) ) +", "+str( toFixed(float(zSim),2) )+")"

line_labels = ["Gradient (red)"+coordGrad, "Simulated (blue)"+coordSim]
fig.legend([fig1, fig2],              # List of the line objects
           labels= line_labels,       # The labels for each line
           loc="upper right",        # Position of the legend
           borderaxespad=0.1,         # Add little spacing around the legend box
           title="Legend Title")      # Title for the legend

#fig3 =ax.plot_surface(x, y, z, cmap='inferno')



plt.show()

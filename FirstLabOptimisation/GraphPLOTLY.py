import plotly.graph_objects as go
import numpy as np
#import KatkovFunctions as ktk
import Gradient as grad
import SimulatedAnnealing as sim
import DeJong as dj

xs = np.arange(-20, 20, 0.1)
ys = np.arange(-20, 20, 0.1)
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

#X, Y, Z = ktk.makeDataKatkovNumpy()
X,Y,Z = dj.makeDataDeJongNumpy()

xGrad, yGrad, zGrad = grad.gradient()
xSim, ySim, zSim = sim.SimulatedAnnealing()

x_dot = np.array([0])
y_dot = np.array([0])
z_dot = np.array([0])
x_dot[0] = float(xSim)
y_dot[0] = float(ySim)
z_dot[0] = float(zSim)

# Блок для поверхности
surface = go.Surface(
    opacity=0.75,
    x=X,
    y=Y,
    z=Z
    )
# Блок для точки
dotSim = go.Scatter3d(
    x=x_dot,
    y=y_dot,
    z=z_dot,
    name = "dot from simulated",
    mode='markers',
    marker=dict(
        size=3,
        line=dict(
            color='rgb(111, 203, 1)',
            width=0.5)
    )
)
x_dot[0] = float(xGrad)
y_dot[0] = float(yGrad)
z_dot[0] = float(zGrad)
dotGrad = go.Scatter3d(
    x=x_dot,
    y=y_dot,
    z=z_dot,
    name = "dot from Gradient",
    mode='markers',
    marker=dict(
        size=3,
        line=dict(
            color='rgb(255, 0, 127)',
            width=0.5)
    )
)

data = [surface, dotSim, dotGrad]
title1 = "Gradient(" + str(toFixed(xGrad,2)) + " " +str(toFixed(yGrad,2)) + " " +str(toFixed(zGrad,2)) +")"
title2 = "Simulated(" + str(toFixed(xSim,2)) + " " +str(toFixed(ySim,2)) + " " +str(toFixed(zSim,2)) +")"
layout = go.Layout(title=title1+"\n "+title2, autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

fig = go.Figure(data=data, layout=layout)

fig.update_layout(showlegend=True)

fig.show()
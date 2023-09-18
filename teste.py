# Arquivo de testes
import numpy as np
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d.axes3d import Axes3D
import RobPy as rp


a = rp.cria_vetor3([1, 2, 3])
b = rp.cria_vetor3([1, 2, 1])

fig: plt.Figure = plt.figure()
ax = Axes3D(fig)
fig.add_axes(ax)
rp.plota_vetor3(a,color='r')
rp.plota_vetor3(b, vo=a)
plot.xlabel('Eixo X')
plot.ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

plot.plot(*args:    [vo[0][0],
                    v[0][0]+vo[0][0]],
                    [vo[1][0], v[1][0]+vo[1][0]],
                    [vo[2][0], v[2][0]+o[2][0]],
                    color='g',
                    linewidth=5)

plot.plot(*args:    [v[0][0]+vo[0][0]],
                    [v[1][0]+vo[1][0]],
                    [v[2][0]+vo[2][0]],
                    color='g',
                    marker = '>',
                    markersize = 15)
plot.show()

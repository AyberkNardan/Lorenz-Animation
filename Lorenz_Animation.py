import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si
from mpl_toolkits import mplot3d
from matplotlib import animation

plt.style.use("dark_background")

def f_lorenz(t,y):
      return np.array([10*(y[1]-y[0]),y[0]*(28-y[2])-y[1],y[0]*y[1]-(8/3)*y[2]])

t = np.linspace(0,50,5000)
y = list()
for x0,y0,z0 in zip([1,2,10],[2,4,5],[4,8,12]): #Arbitrary initial conditions.
      solnLorenz = si.solve_ivp(fun=f_lorenz, t_span=[0,50], y0=[x0,y0,z0],dense_output=True)
      y.append(solnLorenz.sol(t))

fig = plt.figure()
ax = plt.axes(projection="3d")

plt.axis("off")
dataSkip = 70

def update(i):
      if i//100<=40:
            ax.clear()
            ax.view_init(elev=360,azim=i/10)
            xv = y[0][0][i:i+dataSkip]
            yv = y[0][1][i:i+dataSkip]
            zv = y[0][2][i:i+dataSkip]
            xv1 = y[1][0][i:i+dataSkip]
            yv1 = y[1][1][i:i+dataSkip]
            zv1 = y[1][2][i:i+dataSkip]
            xv2 = y[2][0][i:i+dataSkip]
            yv2 = y[2][1][i:i+dataSkip]
            zv2 = y[2][2][i:i+dataSkip]
            ax.plot(xv,yv,zv,"pink")
            ax.plot(xv1,yv1,zv1,"green")
            ax.plot(xv2,yv2,zv2,"yellow")
            ax.set_xlim(-30,30)
            ax.set_ylim(-30,30)
            ax.set_zlim(0,50)
            
      elif 40<i//100<50:
            ax.view_init(elev=360,azim=i/10)
            xv = y[0][0][i:i+dataSkip]
            yv = y[0][1][i:i+dataSkip]
            zv = y[0][2][i:i+dataSkip]
            xv1 = y[1][0][i:i+dataSkip]
            yv1 = y[1][1][i:i+dataSkip]
            zv1 = y[1][2][i:i+dataSkip]
            xv2 = y[2][0][i:i+dataSkip]
            yv2 = y[2][1][i:i+dataSkip]
            zv2 = y[2][2][i:i+dataSkip]
            ax.plot(xv,yv,zv,"pink")
            ax.plot(xv1,yv1,zv1,"green")
            ax.plot(xv2,yv2,zv2,"yellow")
            ax.set_xlim(-30,30)
            ax.set_ylim(-30,30)
            ax.set_zlim(0,50)

      else:
            ax.view_init(elev=360,azim=i/10)
            xv = y[0][0][i:i+dataSkip]
            yv = y[0][1][i:i+dataSkip]
            zv = y[0][2][i:i+dataSkip]
            xv1 = y[1][0][i:i+dataSkip]
            yv1 = y[1][1][i:i+dataSkip]
            zv1 = y[1][2][i:i+dataSkip]
            xv2 = y[2][0][i:i+dataSkip]
            yv2 = y[2][1][i:i+dataSkip]
            zv2 = y[2][2][i:i+dataSkip]
            ax.plot(xv,yv,zv,"pink")
            ax.plot(xv1,yv1,zv1,"green")
            ax.plot(xv2,yv2,zv2,"yellow")
            ax.set_xlim(-30,30)
            ax.set_ylim(-30,30)
            ax.set_zlim(0,50)
      plt.axis("off")

anim = animation.FuncAnimation(fig,update,frames=np.arange(0,len(t)+1000, dataSkip//2),interval=100)
#anim.save("Lorenz.mp4",writer="ffmpeg") #To save the animation (the ffmpeg is needed to be downloaded to save the animation)
plt.show()

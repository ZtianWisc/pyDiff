import numpy as np
import matplotlib.pyplot as plt

num_of_lines = int(input("How many lines do you want?"))
t = np.arange(0.0, 3, 0.01)
y = [None] * num_of_lines
for i in range(num_of_lines):
    y[i] = 2 * i * np.sin(i*np.pi*t)

fig, ax = plt.subplots()
ax.set_title('Interactive spaghetti demo, \n Click on legend to hide a line')
lines = [None] * num_of_lines

for i in range(num_of_lines):
    lines[i] = ax.plot(t, y[i], lw=1, label=(str(i) + ' S'))
leg = ax.legend(loc="upper right", fancybox=True)
leg.get_frame().set_alpha(0.4)

lined = dict()
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(3)  # 3 pts tolerance
    lined[legline] = origline


def onpick(event):
    legline = event.artist
    origline, = lined[legline]
    vis = not origline.get_visible()
    origline.set_visible(vis)
    if vis:
        legline.set_alpha(1.0)
    else:
        legline.set_alpha(0.1)
    fig.canvas.draw()

fig.canvas.mpl_connect('pick_event', onpick)

plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import random

#lista
filelist = []
inverted_edf = []
for i in range(1,4):
    filelist.append("k%s.txt" %i)

def plot_hist(fname, data):
    # plot
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.hist(data, bins=10, histtype='stepfilled', facecolor='g', alpha=0.7)

    # ECDF
    sorted_ = np.sort(data)
    yvals = np.arange(len(sorted_))/float(len(sorted_))
    ax2.plot(sorted_, yvals, 'r-')

    #design
    fig.suptitle(fname)
    ax1.set_xlabel('spaziatura (m)')
    ax1.set_ylabel('EDF', color='g')
    ax2.set_ylabel('ECDF', color='r')
    plt.grid(True)
    plt.show()

# fratture
for fname in filelist:
    # comma cheker
    with open(fname, 'r+') as f:
        text = f.read()
        f.seek(0)
        f.truncate()
        f.write(text.replace(',', '.'))
    # read data
    data = np.loadtxt(fname)
    # plot
    plot_hist(fname, data)
    # EDF
    edf = lambda x: np.searchsorted(np.sort(data), x) / data.size
    slope_changes = sorted(set(data))
    inverted_edf.append(interp1d(edf(slope_changes).tolist() + [1.], slope_changes + [slope_changes[len(slope_changes)-1]]))

# volumi
n = 100
volumes = []
for i in range(n):
    volume = []
    for x, _ in enumerate(filelist):
        volume.append(float(inverted_edf[x](random.random())))
    volumes.append(volume)
plot_hist("volumi", [e[0]*e[1]*e[2] for e in volumes])

    
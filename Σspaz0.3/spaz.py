import matplotlib.pyplot as plt
import numpy as np

filelist = []

for i in range(1,5):
    filelist.append("k%s.txt" %i)

def ecdf(a, bins):
	norm_coef = len(a)
	sorted_ = np.sort(a)
	x = np.linspace(sorted_[0], sorted_[norm_coef], num=bins)
	y = np.zeros(bins)
	for j, asx in enumerate(x):
		i = 0
		sample = sorted_[i]
		while sample < asx:
			i += 1
			sample = sorted_[i]
		y[j] = i / norm_coef
	return a

for fname in filelist:
    
    data=np.loadtxt(fname)

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # EDF
    ax1.hist(data, bins=10, histtype='stepfilled', facecolor='#FFCC00', edgecolor = "none")

    # ECDF
    sorted_ = np.sort(data)
    yvals = np.arange(len(sorted_))/float(len(sorted_))
    ax2.plot(sorted_, yvals, 'k', linewidth=2)

    #design
    fig.suptitle(fname)
    ax1.set_xlabel('spaziatura (m)')
    ax1.set_ylabel('EDF', color='#FFCC00')
    ax2.set_ylabel('ECDF', color='k')
    plt.grid(True)
    
    #show
plt.show()
    
    #save to file
    #fig.savefig(fname[:len(fname)-4] + ".pdf")
    #fig.clf()


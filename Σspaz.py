import matplotlib.pyplot as plt
import numpy as np
    
#comma chekker
#for i in range(1,3):           
    #with open(("k%s.txt" %i), 'r+') as f:
        #text = f.read()
        #f.seek(0)
        #f.truncate()
        #f.write(text.replace(',', '.'))
        
            
#lista
filelist=[]

for i in range(1,5):
    filelist.append("k%s.txt" %i)

#graph
for fname in filelist:
    
    data=np.loadtxt(fname)
    
#%cumulative
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
 
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# EDF
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
    

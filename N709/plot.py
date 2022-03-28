"""
Plot glycan SASA from VMD as a function of probe radius.
"""

import numpy as np
import matplotlib.pyplot as plt

# import datasets
closed = np.loadtxt("SASA_closed.dat")
opened = np.loadtxt("SASA_open.dat")

# 2 panel figure
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,5), sharex=True, sharey=True)

# plot closed sasa
ax[0].plot(closed[:,0], closed[:,1], lw=1.5, label="G14")
ax[0].plot(closed[:,0], closed[:,2], lw=1.5, label="G38")
ax[0].plot(closed[:,0], closed[:,3], lw=1.5, label="G61")
ax[0].legend()
ax[0].set_ylabel("N709 SASA ($\AA^2$)")
ax[0].set_xlabel("Probe Radius ($\AA$)")
ax[0].set_title("Closed Spike")
ax[0].grid(True, alpha=0.3)

# plot opened sasa
ax[1].plot(opened[:,0], opened[:,1], lw=1.5, label="G14")
ax[1].plot(opened[:,0], opened[:,2], lw=1.5, label="G38")
ax[1].plot(opened[:,0], opened[:,3], lw=1.5, label="G61")
ax[1].legend()
ax[1].set_xlabel("Probe Radius ($\AA$)")
ax[1].set_title("Open Spike")
ax[1].grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig("SASA.png", dpi=300, transparent=True)
plt.show()

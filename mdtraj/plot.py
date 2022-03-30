"""
Plot glycan SASA from VMD as a function of probe radius.
"""

import numpy as np
import matplotlib.pyplot as plt

# import datasets
#glycan = "N234"
#gnames = ["G7", "G31", "G54"]
glycan = "N709"
gnames = ["G14", "G38", "G61"]
closed = np.loadtxt(f"SASA_closed_{glycan}.tsv")
opened = np.loadtxt(f"SASA_opened_{glycan}.tsv")

# 2 panel figure
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7,4), sharex=True, sharey=True)

# plot closed sasa
ax[0].plot(closed[:,0], closed[:,1], lw=1.5, label=gnames[0])
ax[0].plot(closed[:,0], closed[:,2], lw=1.5, label=gnames[1])
ax[0].plot(closed[:,0], closed[:,3], lw=1.5, label=gnames[2])
ax[0].legend()
ax[0].set_ylabel(f"{glycan} SASA ($\AA^2$)")
ax[0].set_xlabel("Probe Radius ($\AA$)")
ax[0].set_title("Closed Spike")
ax[0].grid(True, alpha=0.3)

# plot opened sasa
ax[1].plot(opened[:,0], opened[:,1], lw=1.5, label=gnames[0])
ax[1].plot(opened[:,0], opened[:,2], lw=1.5, label=gnames[1])
ax[1].plot(opened[:,0], opened[:,3], lw=1.5, label=gnames[2])
ax[1].legend()
ax[1].set_xlabel("Probe Radius ($\AA$)")
ax[1].set_title("Open Spike")
ax[1].grid(True, alpha=0.3)

ax[0].set_ylim(0,2250)

fig.tight_layout()
fig.savefig(f"SASA_{glycan}.png", dpi=300, transparent=False)
plt.show()

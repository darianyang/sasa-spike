"""
Use MDtraj to calculate the per-residue or per-atom SASA.
"""

import numpy as np
import mdtraj as md

closed = md.load("../spike_closed/spike_closed_pg.pdb")
#opened = md.load("../spike_open/spike_open_pg.pdb")

def calc_sasa(traj, radius=1.4, resname=None):
    """
    Parameters
    ----------
    traj : mdtraj trajectory object
    radius : float
        Solvent probe radius for SASA calculations (Angstroms)
    resname : str
        Optionally calculate partial SASA of a residue.
    """
    # convert from Angstrom to nm for mdtraj compatibility
    radius /= 10

    # calc sasa using the shrake_rupley method
    sasa = md.shrake_rupley(traj, probe_radius=radius)
    print(sasa)

    # total SASA
    total_sasa = sasa.sum(axis=1)
    print("Total SASA: ", total_sasa)

    #if resname is not None:
        



calc_sasa(closed)

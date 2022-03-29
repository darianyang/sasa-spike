"""
Use MDtraj to calculate the per-residue or per-atom SASA.
"""

import numpy as np
import mdtraj as md

closed = md.load("../spike_closed/spike_closed_pg.pdb")
opened = md.load("../spike_open/spike_open_pg.pdb")

def calc_sasa(traj, radius=1.4, atomrange=None):
    """
    Parameters
    ----------
    traj : mdtraj trajectory object
    radius : float
        Solvent probe radius for SASA calculations (Angstroms)
    atomrange : (int, int)
        Optionally calculate partial SASA of an atom range.
        Use the atom range that matches the indexing of the PDB file.

    Returns
    -------
    partial_sasa : float
        If atomrange argument is included.
    """
    # convert from Angstrom to nm for mdtraj compatibility
    radius /= 10

    # calc sasa using the shrake_rupley method
    sasa = md.shrake_rupley(traj, probe_radius=radius, mode="atom")

    # total SASA
    #total_sasa = sasa.sum(axis=1)
    #print("Total SASA (A^2): ", total_sasa * 10**2)

    if atomrange is not None:
        # python indexing array, starts at 0 instead of PDB numbering
        start = atomrange[0] - 1
        # exclusive and indexed by 0 so keep end atom number the same
        end = atomrange[1]
        # calc partial sasa of first frame (since PDB so 1 frame only)
        partial = sasa[0,start:end]
        return np.sum(partial) * 10**2
        

def calc_trimer(traj, atomranges, radius=1.4)
    """
    Parameters
    ----------
    traj : mdtraj trajectory object
    atomranges : ((start, end), (start, end), (start, end))
        Tuple of tuples designating the glycans on the 3 monomers.
    radius : float
        Solvent probe radius for SASA calculations (Angstroms)

    Returns
    -------
    partial_sasas : list
        Partial sasa values of each tuple in atomranges.
    """
    # calc partial sasa of each atomrange
    return [calc_sasa(traj, atomrange=atomrange, radius=radius) \
            for atomrange in atomranges
            ]

N234 = ((59922, 60144), (64727, 64970), (69455, 69698))
N709 = ((61272, 61452), (66206, 66365), (70941, 71100))
radii = [1.4] + [i for i in range(2,22)]

print(calc_trimer(closed, N234, radius=1.4))


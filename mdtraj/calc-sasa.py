"""
Use MDtraj to calculate the per-atom SASA.
"""

import numpy as np
import mdtraj as md
from tqdm.auto import tqdm

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
        

def calc_trimer_multi_radii(traj, atomranges, saveout):
    """
    Parameters
    ----------
    traj : mdtraj trajectory object
    atomranges : ((start, end), (start, end), (start, end))
        Tuple of tuples designating the glycans on the 3 monomers.
    saveout : str
        Output filename for the tsv.
    """
    # list of probe radii
    radii = [1.4] + [i for i in range(2,22)]
    
    # build numpy array of partial sasa at various radii
    # columns = probe_radius G1 G2 G3+
    radii_sasas = np.zeros(shape=(len(radii), len(atomranges) + 1)) 

    print(f"Beginning SASA calculations to generate {saveout}")
    for index, radius in enumerate(tqdm(radii)):
        # calc partial sasa of each atomrange
        single_sasa = [calc_sasa(traj, atomrange=atomrange, radius=radius) \
                       for atomrange in atomranges]

        # fill out array with partial sasa values
        radii_sasas[index, :] = [radius] + single_sasa

    # save the filled sasa values to tsv
    np.savetxt(saveout, radii_sasas, delimiter="\t")

N234 = ((59922, 60144), (64727, 64970), (69455, 69698))
N709 = ((61272, 61452), (66206, 66365), (70941, 71100))

calc_trimer_multi_radii(closed, N234, "SASA_closed_N234.tsv")
calc_trimer_multi_radii(opened, N234, "SASA_opened_N234.tsv")

calc_trimer_multi_radii(closed, N709, "SASA_closed_N709.tsv")
calc_trimer_multi_radii(opened, N709, "SASA_opened_N709.tsv")


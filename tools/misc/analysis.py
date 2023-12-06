import numpy as np
import pandas as pd
from scm.plams.interfaces.molecule.ase import fromASE as ASEtoSCM
from scm.plams.interfaces.molecule.ase import toASE as SCMtoASE
from ase.geometry.analysis import Analysis
from ase.geometry import get_distances
from ase.neighborlist import neighbor_list


def _elements_combinations(elemnts):
    el_product = np.meshgrid(elemnts, elemnts)
    el_i = el_product[0][np.where(np.triu(el_product[0]))]
    el_j = el_product[1][np.where(np.triu(el_product[1]))]
    return el_i, el_j


def _get_bond_elements(ase_mol):
    bonds_el = []
    elemnts = np.unique( ase_mol.get_chemical_symbols() )
    el_i, el_j = _elements_combinations(elemnts)
    analysis = Analysis(ase_mol)
    for ai, aj in zip(el_i, el_j):
        bonds = analysis.get_bonds(ai, aj, unique=True)
        if not len(bonds[0]) > 0:
            continue
        bonds_el.append( (ai, aj) )
    return bonds_el


def get_all_bonds(ase_mol, verbose = False):
    results_df = pd.DataFrame(columns=['ai', 'aj', 'Nbonds', 'bonds'])
    elemnts = np.unique( ase_mol.get_chemical_symbols() )
    el_i, el_j = _elements_combinations(elemnts)
    analysis = Analysis(ase_mol)
    for ai, aj in zip(el_i, el_j):
        bonds = analysis.get_bonds(ai, aj, unique=True)
        if not len(bonds[0]) > 0:
            continue
        results_df.loc[f'{ai}-{aj}', 'ai'] = ai
        results_df.loc[f'{ai}-{aj}', 'aj'] = aj
        results_df.loc[f'{ai}-{aj}', 'bonds'] = bonds[0]
        results_df.loc[f'{ai}-{aj}', 'Nbonds'] = len(bonds[0])
        if verbose:
            print(f"Found {len(bonds[0])} {ai}-{aj} bonds")
    return results_df


def get_all_angles(ase_mol, verbose = False, values=False):
    results_df = pd.DataFrame(columns=['ai', 'aj', 'ak', 'Nangles', 'angles', 'angles_values'])
    elemnts = np.unique( ase_mol.get_chemical_symbols() )
    el_product = np.meshgrid(elemnts, elemnts)
    el_j = elemnts
    el_i, el_k = _elements_combinations(elemnts)
    analysis = Analysis(ase_mol)
    for aj in el_j:
        for ai, ak in zip(el_i, el_k):
            angles = analysis.get_angles(ai, aj, ak, unique=True)
            if not len(angles[0]) > 0:
                continue
            results_df.loc[f'{ai}-{aj}-{ak}', 'ai'] = ai
            results_df.loc[f'{ai}-{aj}-{ak}', 'aj'] = aj
            results_df.loc[f'{ai}-{aj}-{ak}', 'ak'] = ak
            results_df.loc[f'{ai}-{aj}-{ak}', 'angles'] = angles[0]
            if values:
                results_df.loc[f'{ai}-{aj}-{ak}', 'angles_values'] =  analysis.get_values(angles, mic=True) # [analysis.get_angle_value(0, ijk) for ijk in angles]
            results_df.loc[f'{ai}-{aj}-{ak}', 'Nangles'] = len(angles[0])
            if verbose:
                print(f"Found {len(angles[0])} {ai}-{aj}-{ak} angles")
    return results_df


def get_all_dihedrals(ase_mol, verbose = False):
    results_df = pd.DataFrame(columns=['ai', 'aj', 'ak', 'al', 'Ndihedrals', 'dihedrals'])
    elemnts = np.unique( ase_mol.get_chemical_symbols() )
    el_product = np.meshgrid(elemnts, elemnts)
    bonds = _get_bond_elements(ase_mol)
    el_i, el_l = _elements_combinations(elemnts)
    analysis = Analysis(ase_mol)
    for (aj, ak) in bonds:
        for ai, al in zip(el_i, el_l):
            dihedrals = analysis.get_dihedrals(ai, aj, ak, al, unique=True)
            if not len(dihedrals[0]) > 0:
                continue
            results_df.loc[f'{ai}-{aj}-{ak}-{al}', 'ai'] = ai
            results_df.loc[f'{ai}-{aj}-{ak}-{al}', 'aj'] = aj
            results_df.loc[f'{ai}-{aj}-{ak}-{al}', 'ak'] = ak
            results_df.loc[f'{ai}-{aj}-{ak}-{al}', 'al'] = al
            results_df.loc[f'{ai}-{aj}-{ak}-{al}', 'dihedrals'] = dihedrals[0]
            results_df.loc[f'{ai}-{aj}-{ak}-{al}', 'Ndihedrals'] = len(dihedrals[0])
            if verbose:
                print(f"Found {len(dihedrals[0])} {ai}-{aj}-{ak}-{al} dihedrals")
    return results_df


def get_distances_atom(ase_mol, r, mic=False, vector=False):
        R = ase_mol.arrays['positions']
        if isinstance(r, int):
            p1 = [R[r]]
        else:
            p1 = [r]
        p2 = R
        cell = None
        pbc = None
        if mic:
            cell = ase_mol.cell
            pbc = ase_mol.pbc
        D, D_len = get_distances(p1, p2, cell=cell, pbc=pbc)
        if vector:
            D.shape = (-1, 3)
            return D
        else:
            D_len.shape = (-1,)
            return D_len
    

    
def get_surf_atoms(ase_mol, cutoff =3., coord_cutoff = 0.5): 
    i = neighbor_list('i', ase_mol, cutoff)
    coord = np.bincount(i)
    coord = (coord - coord.min()) / (coord.max() - coord.min())
    return np.where(coord <= coord_cutoff)[0]
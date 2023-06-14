
def get_all_sites(sites, lattice, supercell=[1, 1, 1]):
    Na, Nb, Nc = supercell
    A, B, C = lattice.matrix
    sites_list = []

    for na in range(Na):
        for nb in range(Nb):
            for nc in range(Nc):
                for site in sites:
                    r_site = site.site.coords + A * na + B * nb + C * nc
                    sites_list.append(r_site)
    return sites_list
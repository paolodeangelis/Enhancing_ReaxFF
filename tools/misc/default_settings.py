import scm.plams as scm

# Unit cells `Single Point`
settings_0_SP = scm.Settings()
settings_0_SP.input.AMS.task = "SinglePoint"
settings_0_SP.input.AMS.Properties.Gradients = "yes"
settings_0_SP.input.AMS.Properties.StressTensor = "yes"
settings_0_SP.input.AMS.Properties.Hessian = "yes"
settings_0_SP.input.AMS.Properties.PESPointCharacter = "no"
settings_0_SP.input.AMS.Properties.ElasticTensor = "no"
settings_0_SP.input.BAND.basis.type = "DZP"  # DZP Double zeta polarized basis.
# This type of basis sets is thus far provided only for the elements up to Kr (valence e in p-orbital d-orbital)
# Slater-type orbitals (STOs) orbital, with 3 "zeta" parametars to better descrive the electron dispersion (r>>r0)
# plus it can descrive the atom polarization since it add a p-function ()
settings_0_SP.input.BAND.xc.GGA = "PBE"  # Perdew-Burke-Ernzerhof (1996) Exchange-and-correlation (XC) functional
# (https://doi.org/10.1103/PhysRevLett.100.136406)
settings_0_SP.input.BAND.KSpace.Quality = "Good"


# Unit cells `Geometry Optimization`
settings_0_GO = scm.Settings()
settings_0_GO.input.AMS.task = "GeometryOptimization"
settings_0_GO.input.AMS.Properties.Gradients = "no"
settings_0_GO.input.AMS.Properties.StressTensor = "no"
settings_0_GO.input.AMS.Properties.Hessian = "no"
settings_0_GO.input.AMS.Properties.PESPointCharacter = "no"
settings_0_GO.input.AMS.Properties.ElasticTensor = "no"
settings_0_GO.input.AMS.GeometryOptimization.OptimizeLattice = "yes"
settings_0_GO.input.AMS.GeometryOptimization.PretendConverged = "yes"
settings_0_GO.input.AMS.GeometryOptimization.MaxIterations = 500
settings_0_GO.input.BAND.basis.type = "DZP"  # DZP Double zeta polarized basis.
# This type of basis sets is thus far provided only for the elements up to Kr (valence e in p-orbital d-orbital)
# Slater-type orbitals (STOs) orbital, with 3 "zeta" parametars to better descrive the electron dispersion (r>>r0)
# plus it can descrive the atom polarization since it add a p-function ()
settings_0_GO.input.BAND.xc.GGA = "PBE"  # Perdew-Burke-Ernzerhof (1996) Exchange-and-correlation (XC) functional
# (https://doi.org/10.1103/PhysRevLett.100.136406)
settings_0_GO.input.BAND.SCF.Iterations = 150
settings_0_GO.input.BAND.RadialDefaults.NR = (
    3000  # Options for the logarithmic radial grid of the basis functions used in the subprogram Dirac
)
settings_0_GO.input.BAND.CPVector = 128 * 2  # The code is vectorized and this key can be used to set the vector length
settings_0_GO.input.BAND.KGRPX = 10  # Absolute upper bound on the number of k-points processed together.


# Supercell`Single Point`
settings_1_SP = scm.Settings()
settings_1_SP.input.AMS.task = "SinglePoint"
settings_1_SP.input.AMS.Properties.Gradients = "yes"
settings_1_SP.input.AMS.Properties.StressTensor = "no"
settings_1_SP.input.AMS.Properties.Hessian = "no"
settings_1_SP.input.AMS.Properties.PESPointCharacter = "no"
settings_1_SP.input.AMS.Properties.ElasticTensor = "no"
settings_1_SP.input.AMS.GeometryOptimization.OptimizeLattice = "no"
settings_1_SP.input.BAND.basis.type = "DZP"  # DZP Double zeta polarized basis.
# This type of basis sets is thus far provided only for the elements up to Kr (valence e in p-orbital d-orbital)
# Slater-type orbitals (STOs) orbital, with 3 "zeta" parametars to better descrive the electron dispersion (r>>r0)
# plus it can descrive the atom polarization since it add a p-function ()
settings_1_SP.input.BAND.xc.GGA = "PBE"  # Perdew-Burke-Ernzerhof (1996) Exchange-and-correlation (XC) functional
# (https://doi.org/10.1103/PhysRevLett.100.136406)
settings_1_SP.input.BAND.KSpace.Quality = "Good"


# Supercell`Geometry Optimization`
settings_1_GO = scm.Settings()
settings_1_GO.input.AMS.task = "GeometryOptimization"
settings_1_GO.input.AMS.Properties.Gradients = "yes"
settings_1_GO.input.AMS.Properties.StressTensor = "no"
settings_1_GO.input.AMS.Properties.Hessian = "no"
settings_1_GO.input.AMS.Properties.PESPointCharacter = "no"
settings_1_GO.input.AMS.Properties.ElasticTensor = "no"
settings_1_GO.input.AMS.GeometryOptimization.OptimizeLattice = "no"
settings_1_GO.input.AMS.GeometryOptimization.PretendConverged = "yes"
settings_1_GO.input.AMS.GeometryOptimization.MaxIterations = 150
settings_1_GO.input.BAND.basis.type = "DZP"  # DZP Double zeta polarized basis.
# This type of basis sets is thus far provided only for the elements up to Kr (valence e in p-orbital d-orbital)
# Slater-type orbitals (STOs) orbital, with 3 "zeta" parametars to better descrive the electron dispersion (r>>r0)
# plus it can descrive the atom polarization since it add a p-function ()
settings_1_GO.input.BAND.xc.GGA = "PBE"  # Perdew-Burke-Ernzerhof (1996) Exchange-and-correlation (XC) functional
# (https://doi.org/10.1103/PhysRevLett.100.136406)
# settings_1_GO.input.BAND.xc.MetaGGA = 'postscf TPSS'   # A meta-GGA DFT functional in its original form includes the second derivative of the electron density
# TPSS: The 2003 meta-GGA (https://doi.org/10.1103/PhysRevLett.91.146401)
settings_1_GO.input.BAND.KSpace.Quality = "Good"


# Strain `Single Point`
settings_2_SP = scm.Settings()
settings_2_SP.input.AMS.task = "SinglePoint"
settings_2_SP.input.AMS.Properties.Gradients = "yes"
settings_2_SP.input.AMS.Properties.StressTensor = "no"
settings_2_SP.input.AMS.Properties.Hessian = "no"
settings_2_SP.input.AMS.Properties.PESPointCharacter = "no"
settings_2_SP.input.AMS.Properties.ElasticTensor = "no"
settings_2_SP.input.BAND.basis.type = "DZP"  # DZP Double zeta polarized basis.
# This type of basis sets is thus far provided only for the elements up to Kr (valence e in p-orbital d-orbital)
# Slater-type orbitals (STOs) orbital, with 3 "zeta" parametars to better descrive the electron dispersion (r>>r0)
# plus it can descrive the atom polarization since it add a p-function ()
settings_2_SP.input.BAND.xc.GGA = "PBE"  # Perdew-Burke-Ernzerhof (1996) Exchange-and-correlation (XC) functional
# (https://doi.org/10.1103/PhysRevLett.100.136406)


# Vacancies `Single Point`
settings_3_SP = scm.Settings()
settings_3_SP.input.AMS.task = "SinglePoint"
settings_3_SP.input.AMS.Properties.Gradients = "yes"
settings_3_SP.input.AMS.Properties.StressTensor = "no"
settings_3_SP.input.AMS.Properties.Hessian = "no"
settings_3_SP.input.AMS.Properties.PESPointCharacter = "no"
settings_3_SP.input.AMS.Properties.ElasticTensor = "no"
settings_3_SP.input.BAND.basis.type = "DZP"  # DZP Double zeta polarized basis.
# This type of basis sets is thus far provided only for the elements up to Kr (valence e in p-orbital d-orbital)
# Slater-type orbitals (STOs) orbital, with 3 "zeta" parametars to better descrive the electron dispersion (r>>r0)
# plus it can descrive the atom polarization since it add a p-function ()
settings_3_SP.input.BAND.xc.GGA = "PBE"  # Perdew-Burke-Ernzerhof (1996) Exchange-and-correlation (XC) functional
# (https://doi.org/10.1103/PhysRevLett.100.136406)


# Substitution `Single Point`
settings_4_SP = settings_3_SP

# Interstitial `Pre Optimization`
settings_5_PreO = scm.Settings()
settings_5_PreO.input.ams.task = "GeometryOptimization"
settings_5_PreO.input.ams.GeometryOptimization.OptimizeLattice = "yes"
settings_5_PreO.input.ams.GeometryOptimization.Convergence.Energy = scm.Units.convert(
    0.1, "kJ/mol", "Hartree"
)  # [Ha] The criterion for changes in the energy.
# The energy is considered converged when the change in energy is smaller than this threshold.
settings_5_PreO.input.ams.GeometryOptimization.Convergence.Gradients = scm.Units.convert(
    1000, "kJ/mol/Ang", "Hartree/Ang"
)  # [Ha/Ang] Threshold for nuclear gradients.
settings_5_PreO.input.ams.GeometryOptimization.Convergence.StressEnergyPerAtom = scm.Units.convert(
    50, "kJ/mol", "Hartree"
)  # [Ha] Threshold used when optimizing the
# lattice vectors. The stress is considered ‘converged’ when the maximum value of
# stress_tensor * cell_volume / number_of_atoms is smaller than this threshold
settings_5_PreO.input.ams.GeometryOptimization.Convergence.Step = (
    0.05  # [Ang] The maximum Cartesian step allowed for a converged geometry.
)
settings_5_PreO.input.ams.GeometryOptimization.PretendConverged = "yes"
settings_5_PreO.input.ams.GeometryOptimization.MaxIterations = 100
settings_5_PreO.input.BAND.basis.type = "DZ"  # DZP Double zeta polarized basis.
# This type of basis sets is thus far provided only for the elements up to Kr (valence e in p-orbital d-orbital)
# Slater-type orbitals (STOs) orbital, with 3 "zeta" parametars to better descrive the electron dispersion (r>>r0)
# plus it can descrive the atom polarization since it add a p-function ()
settings_5_PreO.input.BAND.basis.Core = "Medium"
settings_5_PreO.input.BAND.Dependency.Core = (
    0.8  # BAND calculates the overlap matrix of the core functions, and this should approximate the unit matrix.
)
# When the deviation is larger then the frozen-core overlap criterion the program stops.
# The default criterion (0.98) is fairly strict. The safest solution is to choose a smaller frozen core.
# For performance reasons, however, this may not be the preferred option.
# In practice you might still get reliable results by setting the criterion to 0.8
settings_5_PreO.input.BAND.xc.LDA = (
    "VWN"  # Parametrization of electron gas data given by Vosko, Wilk and Nusair (ref [1], formula version V).
)
# Among the available LDA options this is the more advanced one, including correlation effects to a fair extent.
# (https://doi.org/10.1139/p80-159)
settings_5_PreO.input.BAND.scf.mixing = 0.3  # Push a bit convergence
settings_5_PreO.input.BAND.numericalquality = "Basic"
settings_5_PreO.input.BAND.beckegrid.quality = "Basic"
settings_5_PreO.input.BAND.CPVector = (
    128 * 4
)  # The code is vectorized and this key can be used to set the vector length
settings_5_PreO.input.BAND.KGRPX = 6  # Absolute upper bound on the number of k-points processed together.

# Interstitial `Geometry Optimization`
settings_5_GO = scm.Settings()
settings_5_GO.input.AMS.task = "GeometryOptimization"
settings_5_GO.input.AMS.Properties.Gradients = "yes"
settings_5_GO.input.AMS.Properties.StressTensor = "no"
settings_5_GO.input.AMS.Properties.Hessian = "no"
settings_5_GO.input.AMS.Properties.PESPointCharacter = "no"
settings_5_GO.input.AMS.Properties.ElasticTensor = "no"
settings_5_GO.input.AMS.GeometryOptimization.OptimizeLattice = "no"
settings_5_GO.input.AMS.GeometryOptimization.Convergence.Energy = scm.Units.convert(
    0.1, "kJ/mol", "Hartree"
)  # [Ha] The criterion for changes in the energy.
# The energy is considered converged when the change in energy is smaller than this threshold.
settings_5_GO.input.AMS.GeometryOptimization.Convergence.Gradients = scm.Units.convert(
    1000, "kJ/mol/Ang", "Hartree/Ang"
)  # [Ha/Ang] Threshold for nuclear gradients.
settings_5_GO.input.AMS.GeometryOptimization.Convergence.StressEnergyPerAtom = scm.Units.convert(
    50, "kJ/mol", "Hartree"
)  # [Ha] Threshold used when optimizing the
# lattice vectors. The stress is considered ‘converged’ when the maximum value of
# stress_tensor * cell_volume / number_of_atoms is smaller than this threshold
settings_5_GO.input.AMS.GeometryOptimization.Convergence.Step = (
    0.05  # [Ang] The maximum Cartesian step allowed for a converged geometry.
)
settings_5_GO.input.AMS.GeometryOptimization.PretendConverged = "yes"
settings_5_GO.input.AMS.GeometryOptimization.MaxIterations = 100
settings_5_GO.input.BAND.basis.type = "DZP"  # DZP Double zeta polarized basis.
# This type of basis sets is thus far provided only for the elements up to Kr (valence e in p-orbital d-orbital)
# Slater-type orbitals (STOs) orbital, with 3 "zeta" parametars to better descrive the electron dispersion (r>>r0)
# plus it can descrive the atom polarization since it add a p-function ()
settings_5_GO.input.BAND.basis.Core = "Medium"
settings_5_GO.input.BAND.Dependency.Core = (
    0.8  # BAND calculates the overlap matrix of the core functions, and this should approximate the unit matrix.
)
# When the deviation is larger then the frozen-core overlap criterion the program stops.
# The default criterion (0.98) is fairly strict. The safest solution is to choose a smaller frozen core.
# For performance reasons, however, this may not be the preferred option.
# In practice you might still get reliable results by setting the criterion to 0.8
settings_5_GO.input.BAND.xc.GGA = "PBE"  # Perdew-Burke-Ernzerhof (1996) Exchange-and-correlation (XC) functional
# (https://doi.org/10.1103/PhysRevLett.100.136406)
settings_5_GO.input.BAND.xc.MetaGGA = "postscf TPSS"  # A meta-GGA DFT functional in its original form includes the second derivative of the electron density
# TPSS: The 2003 meta-GGA (https://doi.org/10.1103/PhysRevLett.91.146401)
settings_5_GO.input.BAND.scf.mixing = 0.3  # Push a bit convergence
settings_5_GO.input.BAND.numericalquality = "Normal"
settings_5_GO.input.BAND.beckegrid.quality = "Normal"
settings_5_GO.input.BAND.CPVector = 128 * 2  # The code is vectorized and this key can be used to set the vector length
settings_5_GO.input.BAND.KGRPX = 4  # Absolute upper bound on the number of k-points processed together.

# Slabs `Pre Optimization`
settings_6_PreO = scm.Settings()
settings_6_PreO.input.ams.task = "GeometryOptimization"
settings_6_PreO.input.ams.GeometryOptimization.OptimizeLattice = "no"
settings_6_PreO.input.ams.GeometryOptimization.Convergence.Energy = scm.Units.convert(
    0.1, "kJ/mol", "Hartree"
)  # [Ha] The criterion for changes in the energy.
# The energy is considered converged when the change in energy is smaller than this threshold.
settings_6_PreO.input.ams.GeometryOptimization.Convergence.Gradients = scm.Units.convert(
    100, "kJ/mol/Ang", "Hartree/Ang"
)  # [Ha/Ang] Threshold for nuclear gradients.
settings_6_PreO.input.ams.GeometryOptimization.Convergence.StressEnergyPerAtom = scm.Units.convert(
    100, "kJ/mol", "Hartree"
)  # [Ha] Threshold used when optimizing the
# lattice vectors. The stress is considered ‘converged’ when the maximum value of
# stress_tensor * cell_volume / number_of_atoms is smaller than this threshold
settings_6_PreO.input.ams.GeometryOptimization.Convergence.Step = (
    0.05  # [Ang] The maximum Cartesian step allowed for a converged geometry.
)
settings_6_PreO.input.ams.GeometryOptimization.PretendConverged = "yes"
settings_6_PreO.input.ams.GeometryOptimization.MaxIterations = 50
settings_6_PreO.input.BAND.basis.type = "SZ"  # DZ Double zeta basis.
# This type of basis sets is thus far provided only for the elements up to Kr (valence e in p-orbital d-orbital)
# Slater-type orbitals (STOs) orbital, with 3 "zeta" parametars to better descrive the electron dispersion (r>>r0)
settings_6_PreO.input.BAND.basis.Core = "Medium"
settings_6_PreO.input.BAND.Dependency.Core = (
    0.8  # BAND calculates the overlap matrix of the core functions, and this should approximate the unit matrix.
)
# When the deviation is larger then the frozen-core overlap criterion the program stops.
# The default criterion (0.98) is fairly strict. The safest solution is to choose a smaller frozen core.
# For performance reasons, however, this may not be the preferred option.
# In practice you might still get reliable results by setting the criterion to 0.8
settings_6_PreO.input.BAND.xc.GGA = "PBE"  # Perdew-Burke-Ernzerhof (1996) Exchange-and-correlation (XC) functional
#                                           # (https://doi.org/10.1103/PhysRevLett.100.136406)
settings_6_PreO.input.BAND.SCF.mixing = 0.1
settings_6_PreO.input.BAND.SCF.Iterations = 180
settings_6_PreO.input.BAND.SCF.Method = "MultiSecant"
settings_6_PreO.input.BAND.numericalquality = "Good"
settings_6_PreO.input.BAND.beckegrid.quality = "Normal"
settings_6_PreO.input.BAND.Convergence.Degenerate = (
    "Default"  # Smooths (slightly) occupation numbers around the Fermi level, so as to insure that nearly-degenerate
)
# states get (nearly-) identical occupations.
settings_6_PreO.input.BAND.RadialDefaults.NR = (
    10000  # Options for the logarithmic radial grid of the basis functions used in the subprogram Dirac
)

settings_6_PreO.input.BAND.CPVector = (
    128 * 4
)  # The code is vectorized and this key can be used to set the vector length
settings_6_PreO.input.BAND.KGRPX = 6  # Absolute upper bound on the number of k-points processed together.


# Slabs `Geometry Optimization`
settings_6_GO = scm.Settings()
settings_6_GO.input.AMS.task = "GeometryOptimization"
settings_6_GO.input.AMS.Properties.Gradients = "yes"
settings_6_GO.input.AMS.Properties.StressTensor = "no"
settings_6_GO.input.AMS.Properties.Hessian = "no"
settings_6_GO.input.AMS.Properties.PESPointCharacter = "no"
settings_6_GO.input.AMS.Properties.ElasticTensor = "no"
settings_6_GO.input.AMS.GeometryOptimization.OptimizeLattice = "no"
settings_6_GO.input.AMS.GeometryOptimization.Convergence.Energy = scm.Units.convert(
    0.1, "kJ/mol", "Hartree"
)  # [Ha] The criterion for changes in the energy.
# The energy is considered converged when the change in energy is smaller than this threshold.
settings_6_GO.input.AMS.GeometryOptimization.Convergence.Gradients = scm.Units.convert(
    1000, "kJ/mol/Ang", "Hartree/Ang"
)  # [Ha/Ang] Threshold for nuclear gradients.
settings_6_GO.input.AMS.GeometryOptimization.Convergence.StressEnergyPerAtom = scm.Units.convert(
    50, "kJ/mol", "Hartree"
)  # [Ha] Threshold used when optimizing the
# lattice vectors. The stress is considered ‘converged’ when the maximum value of
# stress_tensor * cell_volume / number_of_atoms is smaller than this threshold
settings_6_GO.input.AMS.GeometryOptimization.Convergence.Step = (
    0.05  # [Ang] The maximum Cartesian step allowed for a converged geometry.
)
settings_6_GO.input.AMS.GeometryOptimization.PretendConverged = "yes"
settings_6_GO.input.AMS.GeometryOptimization.MaxIterations = 15
settings_6_GO.input.BAND.basis.type = "DZP"  # DZP Double zeta polarized basis.
# This type of basis sets is thus far provided only for the elements up to Kr (valence e in p-orbital d-orbital)
# Slater-type orbitals (STOs) orbital, with 3 "zeta" parametars to better descrive the electron dispersion (r>>r0)
# plus it can descrive the atom polarization since it add a p-function ()
settings_6_GO.input.BAND.basis.Core = "Medium"
settings_6_GO.input.BAND.Dependency.Core = (
    0.8  # BAND calculates the overlap matrix of the core functions, and this should approximate the unit matrix.
)
# When the deviation is larger then the frozen-core overlap criterion the program stops.
# The default criterion (0.98) is fairly strict. The safest solution is to choose a smaller frozen core.
# For performance reasons, however, this may not be the preferred option.
# In practice you might still get reliable results by setting the criterion to 0.8
# settings_6_GO.input.BAND.xc.GGA = 'PBE'        # Perdew-Burke-Ernzerhof (1996) Exchange-and-correlation (XC) functional
# (https://doi.org/10.1103/PhysRevLett.100.136406)
settings_6_GO.input.BAND.xc.MetaGGA = (
    "TPSS"  # A meta-GGA DFT functional in its original form includes the second derivative of the electron density
)
# TPSS: The 2003 meta-GGA (https://doi.org/10.1103/PhysRevLett.91.146401)
settings_6_GO.input.BAND.SCF.mixing = 0.05
settings_6_GO.input.BAND.SCF.Iterations = 150
settings_6_GO.input.BAND.SCF.Method = "MultiSecant"
settings_6_GO.input.BAND.numericalquality = "Good"
settings_6_GO.input.BAND.beckegrid.quality = "Good"
settings_6_GO.input.BAND.Convergence.Degenerate = (
    "Default"  # Smooths (slightly) occupation numbers around the Fermi level, so as to insure that nearly-degenerate
)
# states get (nearly-) identical occupations.
settings_6_GO.input.BAND.RadialDefaults.NR = (
    10000  # Options for the logarithmic radial grid of the basis functions used in the subprogram Dirac
)

settings_6_GO.input.BAND.CPVector = 128 * 4  # The code is vectorized and this key can be used to set the vector length
settings_6_GO.input.BAND.KGRPX = 6  # Absolute upper bound on the number of k-points processed together.


# Amorphous `Ab Initio MD`
settings_MD = scm.Settings()
settings_MD.input.ams.task = "MolecularDynamics"
settings_MD.input.ams.MolecularDynamics.NSteps = 100000
settings_MD.input.ams.MolecularDynamics.TimeStep = 0.25
settings_MD.input.ams.MolecularDynamics.Trajectory.PrintFreq = 5
settings_MD.input.ams.MolecularDynamics.Trajectory.SamplingFreq = 50
settings_MD.input.ams.MolecularDynamics.InitialVelocities.Temperature = 300
settings_MD.input.ams.MolecularDynamics.Thermostat.Type = "Berendsen"
settings_MD.input.ams.MolecularDynamics.Thermostat.Temperature = 300
settings_MD.input.ams.MolecularDynamics.Thermostat.Tau = int(100 * 0.25)
# Engine
settings_MD.input.DFTB.Model = "NonSCC-GFN1-xTB"

# Amorphous `Single Point`
settings_7_SP = scm.Settings()
settings_7_SP.input.AMS.task = "SinglePoint"
settings_7_SP.input.AMS.Properties.Gradients = "yes"
settings_7_SP.input.AMS.Properties.StressTensor = "no"
settings_7_SP.input.AMS.Properties.Hessian = "no"
settings_7_SP.input.AMS.Properties.PESPointCharacter = "no"
settings_7_SP.input.AMS.Properties.ElasticTensor = "no"
settings_7_SP.input.AMS.GeometryOptimization.OptimizeLattice = "no"
settings_7_SP.input.BAND.basis.type = "DZP"  # DZP Double zeta polarized basis.
# This type of basis sets is thus far provided only for the elements up to Kr (valence e in p-orbital d-orbital)
# Slater-type orbitals (STOs) orbital, with 3 "zeta" parametars to better descrive the electron dispersion (r>>r0)
# plus it can descrive the atom polarization since it add a p-function ()
settings_7_SP.input.BAND.xc.GGA = "PBE"  # Perdew-Burke-Ernzerhof (1996) Exchange-and-correlation (XC) functional
# (https://doi.org/10.1103/PhysRevLett.100.136406)

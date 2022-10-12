import numpy as np
import h5py as h5
from effdiff import effdiff
from matplotlib import pyplot as plt

## Example
d = np.load('data/example_data.npz')

tr = d['tracer']
rac = d['rac']
dx = d['dx']
dy = d['dy']

N = 100 # resolution of Keff calculation
eng = effdiff.EffDiffEngine(rac,dx,dy,N)
result = eng.calc_Le2(tr)

# plot result
plt.plot(eng.A, result['Le2'])
plt.xlabel(r'A (m$^2$)')
plt.ylabel(r'$L_e^2$ (m$^2$)')
plt.title('Equivalent Length Squared')
plt.show()

## Load the data I want to use this with
f = h5.File("ens_mean_conc.jld2", "r")
np.shape(f["snapshots/Concentration/0"][:, :, :])

tr = np.transpose(f["snapshots/Concentration/10000"][1, :, :])
rac = np.ones_like(tr) * 0.25
dx = np.ones_like(tr) * np.transpose(f["grid/x"][:]) + 128
dy = np.ones_like(tr) * (f["grid/y"][:]) + 128

N = 100 # resolution of Keff calculation
eng = effdiff.EffDiffEngine(rac,dx,dy,N)
result = eng.calc_Le2(tr)

# plot result
plt.plot(eng.A, result['Le2'])
plt.xlabel(r'A (m$^2$)')
plt.ylabel(r'$L_e^2$ (m$^2$)')
plt.title('Equivalent Length Squared')
plt.show()
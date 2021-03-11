# Exercise 2-02: Make a PMF

import pandas as pd
import empiricaldist

gss = pd.read_hdf('input/gss.hdf5', 'gss')

# Compute the PMF for year
pmf_year = empiricaldist.Pmf.from_seq(gss['year'], normalize=False)

# Print the result
print(pmf_year)

#!/usr/bin/env python
"""
Self-test file, registration case
for OBS RINEX reader
"""
import xarray
from numpy.testing import run_module_suite
#
from pathlib import Path
import pyrinex as pr
#
rdir = Path(__file__).parent

# %% RINEX 2


def test_convenience():
    truth = xarray.open_dataset(rdir/'test2all.nc', group='OBS')

    obs, nav = pr.readrinex(rdir/'demo.10o')
    assert obs.equals(truth)

# %%
    print('loading NetCDF4 file')
    truth = xarray.open_dataset(rdir/'test2all.nc', group='NAV')
    obs, nav = pr.readrinex(rdir/'demo.10n')

    assert nav.equals(truth)


if __name__ == '__main__':
    run_module_suite()

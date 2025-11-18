from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
from astropy import units as u
import numpy as np

def query_gaia(ra, dec, radius_arcmin=12):
    center = SkyCoord(np.median(ra)*u.deg, np.median(dec)*u.deg)
    radius = radius_arcmin * u.arcmin

    Gaia.MAIN_GAIA_TABLE = "gaiadr3.gaia_source"
    Gaia.ROW_LIMIT = -1
    job = Gaia.cone_search_async(coordinate=center, radius=radius)
    results = job.get_results()

    mu = np.sqrt(results['pmra']**2 + results['pmdec']**2)
    mu_err = np.sqrt(results['pmra_error']**2 + results['pmdec_error']**2)
    snr = mu / mu_err
    results['SNR_mu'] = snr

    mask = (snr <= 0) | (snr > 3)
    return results[mask]


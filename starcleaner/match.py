from astropy.coordinates import SkyCoord, match_coordinates_sky
from astropy import units as u
import numpy as np

def match_sources(ra, dec, gaia_table, max_sep_arcsec=1):
    fuv_coords = SkyCoord(ra*u.deg, dec*u.deg)
    gaia_coords = SkyCoord(gaia_table['ra'], gaia_table['dec'])

    idx, d2d, _ = match_coordinates_sky(fuv_coords, gaia_coords)
    mask = d2d < max_sep_arcsec*u.arcsec

    return fuv_coords[mask], gaia_table[idx[mask]]


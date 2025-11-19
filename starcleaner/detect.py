import numpy as np
from astropy.stats import sigma_clipped_stats
from photutils.detection import DAOStarFinder

def detect_sources(data, fwhm=3, sigma=3):
    mean, median, std = sigma_clipped_stats(data, sigma=sigma)
    daofind = DAOStarFinder(fwhm=fwhm, threshold=3*std)
    sources = daofind(data - mean)
    return sources


import numpy as np
import astropy.units as u

def remove_central_and_inner_sources(sources, wcs, data, radius_arcsec=3):
    """
    Removes the central source and any detected sources 
    within `radius_arcsec` arcseconds of the image center.

    Parameters
    ----------
    sources : astropy Table
        Output of detect_sources() containing xcentroid, ycentroid
    
    wcs : astropy.wcs.WCS
        WCS of the image
    
    data : 2D numpy array
        Image array (to get image size)
    
    radius_arcsec : float
        Radius within which sources will be removed (default 3 arcsec)

    Returns
    -------
    cleaned_sources : astropy Table
        Sources with the central and inner ones removed
    """

    # --- Image center ---
    ny, nx = data.shape
    x_c = nx / 2
    y_c = ny / 2

    # Convert image center to RA/DEC
    center_sky = wcs.pixel_to_world(x_c, y_c)

    # Source sky coordinates
    source_sky = wcs.pixel_to_world(sources["xcentroid"], sources["ycentroid"])

    # Angular distances (arcsec)
    sep = source_sky.separation(center_sky).to(u.arcsec).value

    # Central source = minimum separation
    central_index = np.argmin(sep)

    # Mask of sources to remove
    remove_mask = (sep < radius_arcsec)
    remove_mask[central_index] = True  # explicitly remove central source

    # Return cleaned table
    cleaned_sources = sources[~remove_mask]

    return cleaned_sources


import numpy as np
from astropy.stats import sigma_clipped_stats
from photutils.detection import DAOStarFinder

def detect_sources(data, fwhm=3, sigma=3):
    mean, median, std = sigma_clipped_stats(data, sigma=sigma)
    daofind = DAOStarFinder(fwhm=fwhm, threshold=3*std)
    sources = daofind(data - mean)
    return sources


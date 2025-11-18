from astropy.io import fits
from astropy.wcs import WCS

def load_image(path):
    data, header = fits.getdata(path, header=True)
    return data, header, WCS(header)


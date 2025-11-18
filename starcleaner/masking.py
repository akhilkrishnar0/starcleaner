import numpy as np
from photutils.aperture import CircularAperture, EllipticalAperture

def create_star_mask(data, wcs, matched_coords, radius_arcsec=3):
    pixscale = abs(wcs.proj_plane_pixel_scales()[0]) * 3600
    r_pix = radius_arcsec / pixscale

    x, y = wcs.world_to_pixel(matched_coords)
    apertures = CircularAperture(np.transpose([x, y]), r=r_pix)

    mask = np.zeros_like(data, bool)
    for ap in apertures:
        m = ap.to_mask(method='center')
        mask |= m.to_image(data.shape).astype(bool)

    return mask

def create_ellipse_mask(data, x0, y0, sma, smb, theta=0):
    ellipse = EllipticalAperture((x0, y0), a=sma, b=smb, theta=theta)
    return ellipse.to_mask(method='center').to_image(data.shape).astype(bool)

def apply_mask(data, mask):
    masked = data.copy()
    masked[mask] = 0
    return masked


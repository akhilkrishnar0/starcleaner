from .io import load_image
from .detect import detect_sources
from .gaia import query_gaia
from .match import match_sources
from .masking import create_star_mask, create_ellipse_mask, apply_mask
from astropy.io import fits

def process_image(path, outpath, ellipse_params=None):
    data, header, wcs = load_image(path)

    sources = detect_sources(data)
    ra = wcs.pixel_to_world(sources['xcentroid'], sources['ycentroid']).ra.deg
    dec = wcs.pixel_to_world(sources['xcentroid'], sources['ycentroid']).dec.deg

    gaia = query_gaia(ra, dec)
    fuv_match, gaia_match = match_sources(ra, dec, gaia)

    star_mask = create_star_mask(data, wcs, fuv_match)

    if ellipse_params:
        x0, y0, sma, smb, theta = ellipse_params
        ell_mask = create_ellipse_mask(data, x0, y0, sma, smb, theta)
        star_mask |= ell_mask

    masked = apply_mask(data, star_mask)
    fits.writeto(outpath, masked, header, overwrite=True)

    return masked, gaia_match


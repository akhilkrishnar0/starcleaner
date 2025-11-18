import os
import pandas as pd
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib.pyplot as plt


def save_masked_star_data(df, fits_file, output_csv="masked_stars_with_wcs.csv"):
    hdu = fits.open(fits_file)
    w = WCS(hdu[0].header)
    ra, dec = w.all_pix2world(df["x"], df["y"], 0)
    df_out = df.copy()
    df_out["RA"] = ra
    df_out["DEC"] = dec
    df_out.to_csv(output_csv, index=False)
    hdu.close()
    return output_csv


def save_plot(df, fits_file, output_plot="masked_stars_plot.png"):
    hdu = fits.open(fits_file)
    w = WCS(hdu[0].header)
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection=w)
    ax.imshow(hdu[0].data, origin="lower", cmap="gray")
    ax.scatter(df["x"], df["y"], s=20, edgecolor="red", facecolor="none")
    ax.set_xlabel("RA")
    ax.set_ylabel("DEC")
    plt.savefig(output_plot, dpi=200)
    plt.close()
    hdu.close()
    return output_plot


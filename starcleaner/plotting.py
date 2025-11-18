import matplotlib.pyplot as plt
from astropy.visualization import simple_norm
from astropy.wcs import WCS

def plot_sources(data, wcs, sources, norm_percent=99.5, ax=None):
    if ax is None:
        fig, ax = plt.subplots(subplot_kw={"projection": wcs}, figsize=(7,7))

    norm = simple_norm(data, "log", percent=norm_percent)

    ax.imshow(data, origin="lower", cmap="gray", norm=norm)
    ax.scatter(
        sources["xcentroid"],
        sources["ycentroid"],
        s=12,
        edgecolor="yellow",
        facecolor="none",
        label="Detected Sources",
    )

    ax.set_xlabel("RA (J2000)")
    ax.set_ylabel("Dec (J2000)")
    ax.legend()
    ax.set_title("DAOStarFinder Detected Sources")

    return ax


def plot_matches(data, wcs, matched_fuv, norm_percent=99.5, ax=None):
    if ax is None:
        fig, ax = plt.subplots(subplot_kw={"projection": wcs}, figsize=(7,7))

    norm = simple_norm(data, "log", percent=99.5)
    ax.imshow(data, origin="lower", cmap="gray", norm=norm)

    ax.scatter(
        matched_fuv.ra.deg,
        matched_fuv.dec.deg,
        transform=ax.get_transform("icrs"),
        s=30,
        edgecolor="red",
        facecolor="none",
        label="Gaia Matched Stars",
    )

    ax.set_xlabel("RA (J2000)")
    ax.set_ylabel("Dec (J2000)")
    ax.legend()
    ax.set_title("Gaia Cross-Matched Stars")

    return ax


def plot_before_after_mask(original, masked, wcs, norm_percent=99.5):
    fig, axes = plt.subplots(
        1, 2, figsize=(13, 6),
        subplot_kw={"projection": wcs}
    )

    norm1 = simple_norm(original, "log", percent=norm_percent)
    axes[0].imshow(original, origin="lower", cmap="gray", norm=norm1)
    axes[0].set_title("Original Image")
    axes[0].set_xlabel("RA")
    axes[0].set_ylabel("Dec")

    norm2 = simple_norm(masked, "log", percent=norm_percent)
    axes[1].imshow(masked, origin="lower", cmap="gray", norm=norm2)
    axes[1].set_title("Star-Masked Image")
    axes[1].set_xlabel("RA")

    plt.tight_layout()
    return axes


def plot_all(data, wcs, sources, matched_fuv, norm_percent=99.5):
    fig, ax = plt.subplots(subplot_kw={"projection": wcs}, figsize=(8,8))

    norm = simple_norm(data, "log", percent=norm_percent)
    ax.imshow(data, origin="lower", cmap="gray", norm=norm)

    # DAO sources
    ax.scatter(
        sources["xcentroid"],
        sources["ycentroid"],
        s=12,
        edgecolor="yellow",
        facecolor="none",
        label="Detected Sources",
    )

    # Gaia matches
    ax.scatter(
        matched_fuv.ra.deg,
        matched_fuv.dec.deg,
        transform=ax.get_transform("icrs"),
        s=25,
        edgecolor="red",
        facecolor="none",
        label="Gaia Matches",
    )

    ax.set_xlabel("RA (J2000)")
    ax.set_ylabel("Dec (J2000)")
    ax.legend()
    ax.set_title("Detected Sources + Gaia Crossmatches")

    return ax


from setuptools import setup, find_packages

setup(
    name="galnamefix",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "astropy",
        "astroquery"
    ],
    python_requires='>=3.11',
)




## Example Usage
```

from starcleaner.pipeline import process_image

masked, gaia_matches = process_image(
    "downloaded_decals/NGC6902_g.fits",
    "final_images/g_bgsub_stacked_masked.fits",
    ellipse_params=(863.47, 688.04, 378, 40, 0)
)
```

## plot results

```
from starcleaner.plotting import (
    plot_sources,
    plot_matches,
    plot_before_after_mask,
    plot_all
)

# 1. Plot detected sources
plot_sources(fuv_data, wcs, sources)
plt.show()

# 2. Plot Gaia matches
plot_matches(fuv_data, wcs, matched_fuv)
plt.show()

# 3. Compare original vs masked image
plot_before_after_mask(fuv_data, fuv_masked, wcs)
plt.show()


# 4. Full combined panl
plot_all(fuv_data, wcs, sources, matched_fuv)
plt.show()
```


Final plot
<img width="1300" height="600" alt="masked" src="https://github.com/user-attachments/assets/ea86a096-033c-4ada-ac11-dd22b598d106" />


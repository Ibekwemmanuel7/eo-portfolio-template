import numpy as np
import rasterio
from rasterio.transform import from_origin

from eo_portfolio.io import raster_summary


def test_raster_summary_reads_metadata(tmp_path):
    path = tmp_path / "demo.tif"
    data = np.random.randint(0, 255, (3, 8, 8), dtype="uint8")
    transform = from_origin(0, 8, 1, 1)
    with rasterio.open(
        path, "w", driver="GTiff", height=8, width=8, count=3,
        dtype="uint8", crs="EPSG:4326", transform=transform,
    ) as dst:
        dst.write(data)
    info = raster_summary(str(path))
    assert info["bands"] == 3
    assert info["width"] == 8 and info["height"] == 8
    assert info["crs"] is not None
    assert len(info["bounds"]) == 4

"""io.py: small, tested raster/vector helpers used across the labs."""
import rasterio


def raster_summary(path: str) -> dict:
    """Open a raster and return a compact metadata summary."""
    with rasterio.open(path) as src:
        return {
            "bands": src.count,
            "width": src.width,
            "height": src.height,
            "crs": str(src.crs) if src.crs else None,
            "bounds": tuple(src.bounds),
        }

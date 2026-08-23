# eo-portfolio

Your Lillie Academy portfolio repository: every lab commits here with tests and CI.

## Run a lab in one click

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ibekwemmanuel7/eo-portfolio-template) [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Ibekwemmanuel7/eo-portfolio-template) [![Use this template](https://img.shields.io/badge/Use%20this%20template-2ea44f?logo=github)](https://github.com/Ibekwemmanuel7/eo-portfolio-template/generate)

![lab tests](https://github.com/Ibekwemmanuel7/eo-portfolio-template/actions/workflows/ci.yml/badge.svg)

## Where to run the labs

- **Phase 0 to Phase II (setup and classical ML):** run locally, or in the browser with **Codespaces** or **Google Colab**. No GPU needed.
- **Phase III (deep learning, Modules 7 to 9):** use a **free GPU notebook** (Google Colab or Kaggle).
- **Earth Engine step (Module 8 embeddings):** the Earth Engine Python API on the free noncommercial tier.
- **Phase IV (Module 11):** deploy to real cloud (containers and object storage); that is the skill being taught.

Data is read cloud-natively from STAC catalogs (Copernicus Data Space, Microsoft Planetary Computer, NASA Earthdata), so you rarely download whole scenes wherever you compute.

## Local setup

```bash
mamba env create -f environment.yml && mamba activate eo   # or: pip install -r requirements.txt
pip install -e .
pytest -q
```

## In Colab

Open a notebook via the badge above, then run the first cell:

```python
!pip install -q rasterio geopandas rioxarray xarray odc-stac pystac-client geodatasets scikit-learn earthaccess
```

## Layout

```
src/eo_portfolio/   tested helper code (import from your notebooks)
tests/              pytest tests, run in CI on every push
notebooks/          one notebook per lab
data/               small local scratch (kept out of git)
```

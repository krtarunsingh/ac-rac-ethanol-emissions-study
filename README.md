# A Data-Driven Comparative Assessment of Pollution from Ethanol Production and RAC Systems

This repository contains the manuscript, data tables, forecasting code, and generated charts for a global screening-level comparison of emissions from ethanol production, air-conditioning, refrigeration, and household cooling systems.

## Contents

- `research_paper_ac_refrigerator_ethanol_pollution_final.docx` — full manuscript
- `forecast_and_pollution_model.py` — reproducible Python model used for calculations and charts
- `forecast_timeseries.csv` — 2022–2050 forecast dataset
- `global_forecast_comparison.csv` — global comparison summary
- `per_unit_co2e_comparison.csv` — per-unit CO2e comparison for AC, refrigerator, and 1 litre ethanol
- `per_unit_screening_pollutants.csv` — screening estimates for SO2/SOx, NOx, VOC, and PM2.5
- `chart_*.png` — generated figures used in the paper

## Main Result

The screening model estimates that:

- 1 AC running for 24 hours: approximately 16.16 kg CO2e
- 1 refrigerator running for 24 hours: approximately 0.67 kg CO2e
- Production of 1 litre ethanol: approximately 1.11 kg CO2e on a life-cycle basis

The conclusion is that RAC systems are a larger global climate concern, while ethanol production plants can be a stronger local pollution concern when wastewater, VOC, odor, and boiler emissions are poorly controlled.

## How to Reproduce

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Run the model:

```bash
python forecast_and_pollution_model.py
```

## Scope

This is a screening-level research model, not a regulatory emissions inventory. The SO2/SOx, NOx, VOC, and PM2.5 results are directional estimates based on transparent assumptions and should be replaced with region-specific or plant-specific data where available.

## Data and Code Availability

All code, CSV files, and chart outputs are included in this repository. A permanent archived release can be created through Zenodo after publishing a GitHub release.

## Suggested Citation

Singh, T. (2026). A Data-Driven Comparative Assessment of Pollution from Ethanol Production and Refrigeration & Air-Conditioning Systems. GitHub/Zenodo repository.


## Author

Tarun, Independent Researcher (No Company), India. Correspondence: krtarunsingh@gmail.com


## Repository and DOI Placeholders

GitHub repository: https://github.com/krtarunsingh/ac-rac-ethanol-emissions-study

Zenodo DOI: https://doi.org/10.5281/zenodo.21021495

The manuscript has been finalized with the GitHub repository and Zenodo DOI listed below.

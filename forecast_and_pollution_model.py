"""
Reproducible screening model for:
- global AC/RAC vs ethanol emissions forecasting
- per-unit comparison: 1 AC, 1 refrigerator, 1 litre ethanol
- pollutant screening estimates for CO2e, SO2/SOx, NOx, VOC, PM2.5

Data anchors are from public sources:
IEA, UNEP Global Cooling Watch, Our World in Data, International Institute of Refrigeration,
RFA Annual Ethanol Production, Xu et al. 2022 ethanol LCA, EPA AP-42 methods.

This is a screening model, not a regulatory inventory.
Replace the assumptions with local appliance labels, local grid factors, or plant-specific permits
when more accurate data is available.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

GLOBAL_GRID_KG_CO2_PER_KWH = 0.445
AC_KW = 1.5
FRIDGE_KWH_PER_DAY = 1.5
AC_HOURS_FULL_DAY = 24
AC_HOURS_FULL_NIGHT = 8

AC_REFRIGERANT_CHARGE_KG = 0.8
AC_ANNUAL_LEAK_RATE = 0.03
AC_REFRIGERANT_GWP = 2088
FRIDGE_REFRIGERANT_CHARGE_KG = 0.10
FRIDGE_ANNUAL_LEAK_RATE = 0.01
FRIDGE_REFRIGERANT_GWP_OLD = 1430

ETHANOL_MJ_PER_LITER = 21.1
ETHANOL_LCA_GCO2E_PER_MJ = 52.4
ETHANOL_REFINING_GCO2E_PER_MJ = 25.6
ETHANOL_FERMENTATION_KG_CO2_PER_L = 0.75
LITER_PER_GALLON = 3.78541

rfa_ethanol_mgal = {2021: 26890, 2022: 27790, 2023: 29720, 2024: 31360, 2025: 32000}

def cagr(start, end, years):
    return (end / start) ** (1 / years) - 1

def exp_forecast(anchor_year, anchor_value, target_years, annual_growth):
    return {y: anchor_value * ((1 + annual_growth) ** (y - anchor_year)) for y in target_years}

def refrigerant_day_co2e(charge_kg, leak_rate, gwp):
    return charge_kg * leak_rate * gwp / 365

def ethanol_mgal_to_gtco2e(mgal, gco2e_per_mj=ETHANOL_LCA_GCO2E_PER_MJ):
    liters = mgal * 1e6 * LITER_PER_GALLON
    kg = liters * ETHANOL_MJ_PER_LITER * gco2e_per_mj / 1000
    return kg / 1e12

years = np.arange(2022, 2051)
ac_growth = cagr(1.75, 3.8, 2050 - 2022)
cooling_bau_growth = cagr(3.6, 7.2, 2050 - 2022)
cooling_sust_growth = cagr(3.6, 2.6, 2050 - 2022)
ethanol_moderated_growth = 0.015

ac_forecast = exp_forecast(2022, 1.75, years, ac_growth)
cooling_bau_forecast = exp_forecast(2022, 3.6, years, cooling_bau_growth)
cooling_sust_forecast = exp_forecast(2022, 3.6, years, cooling_sust_growth)

ethanol_moderated_forecast = {}
for y in years:
    if y <= 2025:
        ethanol_moderated_forecast[y] = np.interp(y, list(rfa_ethanol_mgal.keys()), list(rfa_ethanol_mgal.values()))
    else:
        ethanol_moderated_forecast[y] = rfa_ethanol_mgal[2025] * ((1 + ethanol_moderated_growth) ** (y - 2025))

forecast_df = pd.DataFrame({
    "year": years,
    "AC_only_GtCO2e_baseline": [ac_forecast[y] for y in years],
    "All_cooling_RAC_GtCO2e_BAU": [cooling_bau_forecast[y] for y in years],
    "All_cooling_RAC_GtCO2e_sustainable": [cooling_sust_forecast[y] for y in years],
    "Ethanol_LCA_GtCO2e_moderated": [ethanol_mgal_to_gtco2e(ethanol_moderated_forecast[y]) for y in years],
})

print(forecast_df.tail())
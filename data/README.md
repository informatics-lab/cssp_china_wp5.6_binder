# CSSP China WP5.6: Data Sources
The data used in this project has been sourced from the [KNMI Data Portal](https://climexp.knmi.nl/selectindex.cgi), [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means), [Japanese Meteorological Agency (JMA)](https://www.jma.go.jp/jma/index.html), [National Center for Atmospheric Research (NCAR)](https://climatedataguide.ucar.edu/) and [National Bureau of Statistics of China](http://www.stats.gov.cn/english/).

## Maize yield data:
Sourced from the [National Bureau of Statistics of China](http://www.stats.gov.cn/english/).

## Meteorological data:
Global gridded monthly mean 2m temperature, precipitation, mean sea-level pressure, soil moisture, snow amount, geopotential height at 850 hPa, 500 hPa and 200 hPa, and meridional and zonal winds at 200hPa for 1980-2016 are taken from the [ERA5 reanalysis dataset](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means).


## Climate index data:
Monthly climate indices are identified by their month and abbreviation in the format `<abbreviation>-<month_number>` e.g. `peu-5` represents Polar Eurasian index in May. Most of the climate indices used in this project were sourced from the [KNMI Data Portal](https://climexp.knmi.nl/selectindex.cgi), as published. Others were sourced from [JMA](https://www.jma.go.jp/jma/index.html) and [NCAR](https://climatedataguide.ucar.edu/), or manually calculated from ERA5 sea surface temperature reanalysis data sourced from the [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means), processed according to the literature (see table below).

| Code      | Name                                                | Source                                                                                                 | Reference                                                                                                                                    |
| --------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| NIN3      | El Nino 3                                           | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=UKMOData/hadisst1_nino3.4a&STATION=NINO3.4)          |                                                                                                                                              |
| IOD       | Indian Ocean Dipole                                 | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=UKMOData/hadisst1_dmi&STATION=DMI_HadISST1)          |                                                                                                                                              |
| SNAO      | Summer North Atlantic Oscillation                   | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=UCARData/snao_ucar&STATION=SNAO_ucar)                |                                                                                                                                              |
| EAWR      | East Atlantic/West Russia Pattern                   | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_ea_wr&STATION=CPC_EA/WR)                |                                                                                                                                              |
| PEU       | Polar Eurasian                                      | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_pol&STATION=CPC_POL)                    |                                                                                                                                              |
| SAM       | Southern Annular Mode                               | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=BASData/bas_sam&STATION=BAS_SAM)                     |                                                                                                                                              |
| SEU       | Eurasian Snowcover                                  | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=RutgersData/eurasia_snow&STATION=Eurasia_snow_cover) |                                                                                                                                              |
| NAO       | North Atlantic Oscillation                          | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=CRUData/nao&STATION=NAO-Gibraltar)                   |                                                                                                                                              |
| AO        | Arctic Oscillation                                  | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_ao&STATION=AO_CPC)                      |                                                                                                                                              |
| SCAND     | Scandinavian pattern                                | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_sca&STATION=CPC_SCA)                    |                                                                                                                                              |
| MJOPC1a/b | Madden-Julian Oscillation                           | [KNMI](https://climexp.knmi.nl/selectindex.cgi)                                                        | First principal components of MJO phases 4-5 [140°E-160°E] (a) and phases 8-10 [10°W-70°E] (b)                                               |
| SOI       | Southern Oscillation Index                          | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_soi&STATION=SOI)                        |                                                                                                                                              |
| QBO       | Quasi-Biennial Oscillation                          | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPNCAR40/nqbo&STATION=CDC_QBO)                     |                                                                                                                                              |
| PNA       | Pacific North American pattern                      | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_pna&STATION=CPC_PNA)                    |                                                                                                                                              |
| EA        | East Atlantic pattern                               | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_ea&STATION=CPC_EA)                      |                                                                                                                                              |
| NH_ICE    | Northern Hemisphere Sea-ice Area                    | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NSIDCData/N_ice_area&STATION=NH_seaice_area)         |                                                                                                                                              |
| NH_ICE2   | Northern Hemisphere Sea-ice Extent                  | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NSIDCData/N_ice_extent&STATION=NH_seaice_extent)     |                                                                                                                                              |
| PDO       | Pacific Decadal Oscillation                         | [JMA](https://www.data.jma.go.jp/gmd/kaiyou/data/db/climate/pdo/pdo.txt)                               |                                                                                                                                              |
| AMO       | Atlantic Multidecadal Oscillation                   | [NCAR](https://climatedataguide.ucar.edu/sites/default/files/2022-03/amo_monthly.10yrLP.txt)           | [Trenberth and Shea, 2006](https://climatedataguide.ucar.edu/climate-data/atlantic-multi-decadal-oscillation-amo)                            |
| CGT       | Circumglobal Teleconnection                         | [ERA5](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means) | Monthly mean of 200hPa geopotential height [35-40N, 60-70E] as defined in [Beverley et al., 2018](https://doi.org/10.1007/s00382-018-4371-4) |
| WPSH      | West Pacific Subtropical High                       | [ERA5](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means) | [Riyu, 2002](https://doi.org/10.1007/s00376-002-0061-5)                                                                                      |
| VAP       | Water vapour                                        | [ERA5](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means) | [Seabrook et al., 2023](https://doi.org/10.1029/2022GL101226)                                                                                |
| PSTRATU   | Northern Hemisphere polar stratospheric zonal winds | [ERA5](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means) | [Hauchecorne, 2021](https://doi.org/10.5281/ZENODO.5744919)                                                                                  |



## Jet index data:
To explain physical relationships between climate mechanisms represented by the climate indices used in this project, we calculated multiple jet phenomena from monthly [ERA5](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means) wind data at various pressure levels. These indices include:
| Code  | Name                       | Source | Reference                                                                                       |
| ----- | -------------------------- | ------ | ----------------------------------------------------------------------------------------------- |
| EASJU | Eurasian Subtropical Jet U | ERA5   | [Huang et al., 2014](https://doi.org/10.1175/JCLI-D-14-00067.1) or manually defined (see paper) |
| EASJV | Eurasian Subtropical Jet V | ERA5   | [Huang et al., 2014](https://doi.org/10.1175/JCLI-D-14-00067.1) or manually defined (see paper) |
| EAPJU | Eurasian Polar Jet U       | ERA5   | [Huang et al., 2014](https://doi.org/10.1175/JCLI-D-14-00067.1) or manually defined (see paper) |
| EAPJV | Eurasian Polar Jet V       | ERA5   | [Huang et al., 2014](https://doi.org/10.1175/JCLI-D-14-00067.1) or manually defined (see paper) |



## MJO Principle Components 

MJO data is split into phases, each phase indicates the position of the MJO around the equator. Each phase then is a time series of the amplitude of the MJO at that time. Given the nature of the MJO which enhances convection in the centre and suppress convection ahead and behind this centre. It's reasonable to assume that when using phases for this analysis ( 4 and 5 for example), we would see an equally strong correlation with opposite sign, since one is enhanced and the other suppressed. Ideally we want to incorporate all of this information into one index, we can do this with principle components. 

Initially running the method with all 10 phases from KNMI, certain phases came out as important and showed this behavior mentioned above. These phases were as follows: Phase 4 (140E), Phase 5 (160E), Phase 8 (10W), Phase 9 (20E) and Phase 10 (70E). From these we made two indices; PC1 of Phases 4 and 5, and  PC1 of Phases 8,9,10.

Codes used in this analysis are:
MJOPC1a = PC1 of phases 4 and 5 
MJOPC1b = PC1 of phases 8,9 and 10






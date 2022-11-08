# CSSP China WP5.6: Data Sources

The data used in this project has been sourced from the [KNMI Data Portal](https://climexp.knmi.nl/selectindex.cgi), [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/cdsapp#!/home) and [National Bureau of Statistics of China](http://www.stats.gov.cn/english/).

## Climate index data:
Monthly climate indices are identified by their month and abbreviation in the format `<abbreviation>-<month_number>` e.g. `peu-5` represents Polar Eurasian index in May. Most of the climate indices used in this project were sourced from the [KNMI Data Portal](https://climexp.knmi.nl/selectindex.cgi), as published. Others were manually calculated from ERA5 sea surface temperature data sourced from the [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/cdsapp#!/home), processed according to the literature (see table below).

| Code  | Name                                     | Source                                                                                        | Reference                                |
| ----- | ---------------------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------- |
| AO    | Arctic Oscillation                       | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_ao&STATION=AO_CPC)             |                                          |
| CGT   | Circumglobal Teleconnection              | ERA5                                                                                          | Monthly mean of 200hPa geopotential height (35-40N, 60-70E) as defined in [Beverley, J.D., Woolnough, S.J., Baker, L.H. et al 2018](https://doi.org/10.1007/s00382-018-4371-4)                                |
| EAWR  | East Atlantic/West Russia Pattern        | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_ea_wr&STATION=CPC_EA/WR)                                                                                            |                                          |
| ENSO  | El Nino Southern Oscillation             | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=UKMOData/hadisst1_nino3.4a&STATION=NINO3.4) |                                          |
| ESnow | Eurasian Snowcover                       |  [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=RutgersData/eurasia_snow&STATION=Eurasia_snow_cover)                                                                                             |                                          |
| IOD   | Indian Ocean Dipole                      |                                                                                               |                                          |
| NAO   | North Atlantic Oscillation               | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=CRUData/nao&STATION=NAO-Gibraltar)          |                                          |
| SNAO  | Summer North Atlantic Oscillation        | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_sca&STATION=CPC_SCA)           |                                          |
| PEU   | Polar Eurasian                           | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_pol&STATION=CPC_POL)           |                                          |
| WPSH  | West Pacific Subtropical High            |                                                                                               |                                          |
| AEA   | Atlantic Eurasian Teleconnection pattern |                                                                                               | https://doi.org/10.1088/1748-9326/aa9d33 |
| MJO   | Madden-Julian Oscillation                | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_mjo01_mean12&STATION=MJO_01)   |                                          |
| NIN3  | El Nino 3                                | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=UKMOData/hadisst1_nino3a&STATION=NINO3)     |                                          |
| PDO   | Pacific Decadal Oscillation              |  [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=UWData/pdo&STATION=PDO)                                                                                             |                                          |
| SCAND | Scandinavian pattern                     | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_sca&STATION=CPC_SCA)           |                                          |
| SOI   | Southern Oscillation Index               | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_soi&STATION=SOI)               |                                          |
| SAM   | Southern Annular Mode                    | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=BASData/bas_sam&STATION=BAS_SAM)            |                                          |
| QBO   | Quasi-Biennial Oscillation               | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPNCAR40/nqbo&STATION=CDC_QBO)            |                                          |
| PNA   | Pacific North American pattern           |  [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_pna&STATION=CPC_PNA)                                                                                             |                                          |
| EA    | East Atlantic pattern                    | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=NCEPData/cpc_ea&STATION=CPC_EA)             |                                          |
| AMO   | Atlantic Multidecadal Oscillation        | [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=UKMOData/amo_hadsst_ts&STATION=AMO_hadsst)  |                                          |
| SEU   |                                          |                                                                                               |                                          |



## Jet index data:
To explain physical relationships between climate mechanisms represented by the climate indices used in this project, we calculated multiple jet phenomena from ERA5 wind data at various pressure levels. These indices include:
| Code    | Name                          | Source | Reference                                 |
| ------- | ----------------------------- | ------ | ----------------------------------------- |
| EASJU   | Eurasian Subtropical Jet U    |        | https://doi.org/10.1175/JCLI-D-14-00067.1 |
| EASJV   | Eurasian Subtropical Jet V    |        | https://doi.org/10.1175/JCLI-D-14-00067.1 |
| EAPJU   | Eurasian Polar Jet U          |        | https://doi.org/10.1175/JCLI-D-14-00067.1 |
| EAPJV   | Eurasian Polar Jet V          |        | https://doi.org/10.1175/JCLI-D-14-00067.1 |
| PSTRATU | Stratospheric Final Warming U | ERA5   | https://zenodo.org/record/5744919         |
|         |                               |        |                                           |




## Temperature and precipitation data:
Copernicus Climate Change Service (C3S) (2017): ERA5: Fifth generation of ECMWF atmospheric reanalyses of the global climate. Copernicus Climate Change Service Climate Data Store (CDS), date of access ?? ???? 2021. https://cds.climate.copernicus.eu/cdsapp#!/home

## Maize yield data:
Sourced from the [National Bureau of Statistics of China](http://www.stats.gov.cn/english/).



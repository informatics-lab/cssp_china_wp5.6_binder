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
| SEU | Eurasian Snowcover                       |  [KNMI](https://climexp.knmi.nl/getindices.cgi?WMO=RutgersData/eurasia_snow&STATION=Eurasia_snow_cover)                                                                                             |                                          |
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
| 



## Jet index data:
To explain physical relationships between climate mechanisms represented by the climate indices used in this project, we calculated multiple jet phenomena from ERA5 wind data at various pressure levels. These indices include:
| Code    | Name                          | Source | Reference                                 |
| ------- | ----------------------------- | ------ | ----------------------------------------- |
| EASJU   | Eurasian Subtropical Jet U    |  ERA5      | https://doi.org/10.1175/JCLI-D-14-00067.1 |
| EASJV   | Eurasian Subtropical Jet V    |   ERA5     | https://doi.org/10.1175/JCLI-D-14-00067.1 |
| EAPJU   | Eurasian Polar Jet U          |   ERA5     | https://doi.org/10.1175/JCLI-D-14-00067.1 |
| EAPJV   | Eurasian Polar Jet V          |   ERA5     | https://doi.org/10.1175/JCLI-D-14-00067.1 |
| PSTRATU | Stratospheric Final Warming U | ERA5   | Hauchecorne, Alain. (2021). ERA5 dataset for the categorization of Stratospheric Final Warming (Version 1) [U60N]. Zenodo. https://doi.org/10.5281/zenodo.5744919        |
|         |                               |        |                                           |


## Principle Components 

MJO data is split into phases, each phase indicates the position of the MJO around the equator. Each phase then is a time series of the amplitude of the MJO at that time. Given the nature of the MJO which enhances convection in the centre and suppress convection ahead and behind this centre. It's reasonable to assume that when using phases for this analysis ( 4 and 5 for example), we would see an equally strong correlation with opposite sign, since one is enhanced and the other suppressed. Ideally we want to incorporate all of this information into one index, we can do this with principle components. 

Initially running the method with all 10 phases from KNMI, certain phases came out as important and showed this behavior mentioned above. These phases were as follows: Phase 4 (140E), Phase 5 (160E)
, Phase 8 (10W), Phase 9 (20E) and Phase 10 (70E). From these we made four indices, PC1 and PC2 of Phases 4 and 5 and  PC1 and PC2 of Phases 8,9,10.

In these are described in plots as:
mjopc1a = PC1 of phases 4 and 5 
mjopc1b = PC2 of phases 4 and 5
mjopc2a = PC1 of phases 8,9 and 10
mjopc2b = PC2 of phases 8,9 and 10

The convention here being a = PC1, b = PC2 and the 1 and 2 indicate which phases went into making that principle component 1 = Phases 4 and 5 and 2 = Phases 8,9 and 10. 

## Temperature and precipitation data:
Copernicus Climate Change Service (C3S) (2017): ERA5: Fifth generation of ECMWF atmospheric reanalyses of the global climate. Copernicus Climate Change Service Climate Data Store (CDS), date of access ?? ???? 2021. https://cds.climate.copernicus.eu/cdsapp#!/home

## Maize yield data:
Sourced from the [National Bureau of Statistics of China](http://www.stats.gov.cn/english/).



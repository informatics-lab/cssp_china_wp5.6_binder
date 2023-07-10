#!/usr/bin/env python

import cdsapi

c = cdsapi.Client()


def era5_request(year, target):
    """
        An ERA5 request for reanalysis single level data.
    """
    c.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'product_type':'monthly_averaged_reanalysis',
            'variable': 'volumetric_soil_water_layer_4',
            'year': year,
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
            'time': '00:00',
            'format':'netcdf'
        },
        target)


def era5_request_multi(year, target):
    """
        An ERA5 request for reanalysis multi level data.
    """
    c.retrieve(
	    'reanalysis-era5-pressure-levels-monthly-means',
        {
            'format': 'netcdf',
            'variable': [
                'u_component_of_wind', 'v_component_of_wind',
            ],
            'product_type': 'monthly_averaged_reanalysis',
            'pressure_level': '200',
            'year': year,
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
            'time': '00:00',
        },
        target)


if __name__ == '__main__':

    yearStart = 1979
    yearEnd = 2023
    for year in list(range(yearStart, yearEnd + 1)):
        target = '/data/users/ncreaser/ERA5_download/data/era5_200hpa_u_v_wind_%04d.nc' % (year)
        print(target)
        era5_request_multi(year, target)
    exit()

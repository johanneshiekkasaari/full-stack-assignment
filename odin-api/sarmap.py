from osgeo import gdal
import haversine as hs

def getMap():
    ds: gdal.Dataset = gdal.Open('SAR_image_20420212.png', gdal.GA_ReadOnly)
    corners = [
        (22.2908182629724, 59.91614254645401), #UL
        (22.578806773313246, 59.947751078236365), #UR
        (22.638044070378744, 59.809992490984754), #LR
        (22.351391574531174, 59.77847599974091), #LL
    ]
    ul = gdal.GCP(22.2908182629724,   59.91614254645401,  0, 0,              0)
    ur = gdal.GCP(22.578806773313246, 59.947751078236365, 0, ds.RasterXSize, 0)
    lr = gdal.GCP(22.638044070378744, 59.809992490984754, 0, ds.RasterXSize, ds.RasterYSize)
    ll = gdal.GCP(22.351391574531174, 59.77847599974091,  0, 0,              ds.RasterYSize)
    #ds.SetGCPs([ul, ur, lr, ll], ds.GetProjection)

    # calculate the resolution
    ulx = corners[0][0]
    uly = corners[0][1]
    xres = hs.haversine(corners[0], corners[1], unit=hs.Unit.METERS)/ ds.RasterXSize
    yres = hs.haversine(corners[0], corners[3], unit=hs.Unit.METERS)/ ds.RasterYSize *-1
    ds.SetGeoTransform([
        ulx, 
        xres, 
        0, 
        uly, 
        0, 
        yres,
    ]);

    return(ds)


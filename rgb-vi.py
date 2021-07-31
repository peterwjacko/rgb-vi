#%%
import rasterio as rio
from rasterio.plot import show

import numpy as np
np.seterr(divide='ignore', invalid='ignore')

#https://automating-gis-processes.github.io/CSC18/lessons/L6/raster-calculations.html

#%%
input_path = '/data/GIS/DroneImagery/currimundi-lake/25032021-processed/odm_orthophoto/odm_orthophoto.tif'
output_path = '/data/GIS/DroneImagery/currimundi-lake/25032021-processed/odm_orthophoto/output.tif'

image = rio.open(input_path)
image_transform = image.transform
image_shape = image.shape

R = image.read(1)
G = image.read(2)
B = image.read(3)

check = np.logical_or(R > 0, G > 0, B > 0)

#%%

def apply_vi(R, G, B, formula, image_shape, check):
    array = np.empty(image.shape, dtype=rio.uint8)
    array = np.where(check, formula, -9999)
    return array

#%%

def gr(image):
    '''
    Green Ratio = G/(G+R+B)
    '''
    GR = np.empty(image.shape, dtype=rio.uint8)
    R = image.read(1)
    G = image.read(2)
    B = image.read(3)
    check = np.logical_or(R > 0, G > 0, B > 0)
    GR = np.where(check, G/(G+R+B), -9999)
    
    return GR

#%%
# Green ratio #
GR = G/(G+R+B)

# Triangular Greenness Index #
TGI = G-0.39*R-0.61*B

# Visible Atmospheric Resistant Index #
VARI = (G-R)/(G+R-B)

# Green-red vegetation index #
GRVI = (G-R)/(G+R)

# Normalized green-red difference index #
NGBDI = (G-B)/(G+B)

# Green leaf index #
GLI = (2*G-R-B)/(2*G+R+B)

#Excess green # 
EXG = 2*G-R-B

# Red green-blue vegetation index #
RGBVI = (G^2-R*B)/(G^2+R*B)

# Modified green-red vegetation index #
MGRVI = (G^2-R^2)/(G^2+R^2)

# New green-red vegetation index #
NGRVI = (G^2+R^2)/(G^2-R^2)
## Zhang et al. 2019

# Red-Green Ratio Index #
RGRI = R/G

# Color Index of Vegetation #
CIVE = 0.441*R-0.881*G+0.385*B+18.787

# Vegetativen #
a = 0.667
VEG = G/(R^a*B^(1-a))

#%%
with rio.open(
    output_path,
    'w',
    driver='GTiff',
    height=image.shape[0],
    width=image.shape[1],
    count=1,
    dtype=rio.uint8,
    crs='+proj=latlong',
    transform=image_transform,
) as dst:
    dst.write(vi_array, 1)
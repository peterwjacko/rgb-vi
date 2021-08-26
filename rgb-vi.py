#%%
from pathlib import Path, PurePath
import rasterio as rio
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

#%%
input_path = Path("/path/to/image.tif")

#%%
class veg_index:
    def __init__(self, input_path):
        self.image = rio.open(str(PurePath(input_path)))
        self.image_transform = self.image.transform
        self.image_shape = self.image.shape
        self.image_crs = self.image.crs
        # NOTE: ensure that these band number match your RGB band numbers. Don't get caught out with RGBA images!
        self.bands = {
            'R': self.image.read(1),
            'G': self.image.read(2),
            'B': self.image.read(3)
            }
        self.check = np.logical_or(
            self.bands['R'] > 0, 
            self.bands['G'] > 0, 
            self.bands['B'] > 0
            )
        self.image = None
        
    def gcc(self):
        '''
        Green Chromatic Coordinate= G/(G+R+B)
        '''
        self.vi_name = '_GCC'
        GCC = np.empty(self.image_shape, dtype=np.float32)
        GCC = np.where(self.check, (self.bands['G'])/(self.bands['G']+self.bands['R']+self.bands['B']), -9999)
    
        return GCC
    
    def tgi(self):
        '''
        Triangular Greenness Index = G-0.39*R-0.61*B
        '''
        self.vi_name = '_TGI'
        TGI = np.where(self.check, self.bands['G']-0.39*self.bands['R']-0.61*self.bands['B'], -9999)

        return TGI
    
    def vari(self):
        '''
        Visible Atmospheric Resistant Index = (G-R)/(G+R-B)

        '''
        self.vi_name = '_VARI'
        VARI = np.empty(self.image_shape, dtype=np.float32)
        VARI = np.where(self.check, (self.bands['G']-self.bands['R'])/(self.bands['G']+self.bands['R']-self.bands['B']), -9999)

        return VARI

    def grvi(self):
        '''
        Green-red vegetation index = (G-R)/(G+R)

        '''
        self.vi_name = '_GRVI'
        GRVI = np.where(self.check, (self.bands['G']-self.bands['R'])/(self.bands['G']+self.bands['R']), -9999)

        return GRVI
    
    def ngrdi(self):
        '''
        Normalized green-red difference index = (G-B)/(G+B)

        '''
        self.vi_name = '_NGRDI'
        NGRDI = np.where(self.check, (self.bands['G']-self.bands['B'])/(self.bands['G']+self.bands['B']), -9999)

        return NGRDI  

    def gli(self):
        '''
        Green leaf index = (2*G-R-B)/(2*G+R+B)

        '''
        self.vi_name = '_GLI'
        GLI = np.where(self.check, (2*self.bands['G']-self.bands['R']-self.bands['B'])/(2*self.bands['G']+self.bands['R']+self.bands['B']), -9999)

        return GLI
        
    def exg(self):
        '''
        Excess green = 2*G-R-B

        '''
        self.vi_name = '_ExG'
        ExG = np.where(self.check, 2*self.bands['G']-self.bands['R']-self.bands['B'], -9999)

        return ExG
    
    def rgbvi(self):
        '''
        Red green-blue vegetation index = ((G**2)-R*B)/((G**2)+R*B)

        '''
        self.vi_name = '_RGBVI'
        RGBVI = np.where(self.check, ((self.bands['G']**2)-self.bands['R']*self.bands['B'])/((self.bands['G']**2)+self.bands['R']*self.bands['B']), -9999)

        return RGBVI          

    def mgrvi(self):
        '''
        Modified green-red vegetation index = ((G**2)-(R**2))/((G**2)+(R**2))

        '''
        self.vi_name = '_MGRVI'
        MGRVI = np.where(self.check, ((self.bands['G']**2)-(self.bands['R']**2))/((self.bands['G']**2)+(self.bands['R']**2)), -9999)

        return MGRVI
    
    def ngrvi(self):
        '''
        New green-red vegetation index = ((G**2)+(R**2))/((G**2)-(R**2))

        '''
        self.vi_name = '_NGRVI'
        NGRVI = np.where(self.check, ((self.bands['G']**2)-(self.bands['R']**2))/((self.bands['G']**2)+(self.bands['R']**2)), -9999)

        return NGRVI
    
    def rgri(self):
        '''
        Red-Green Ratio Index = R/G    

        '''
        self.vi_name = '_RGRI'
        RGRI = np.where(self.check, (self.bands['R'])/(self.bands['G']), -9999)

        return RGRI

    def cive(self):
        '''
        Color Index of Vegetation = 0.441*R-0.881*G+0.385*B+18.787  

        '''
        self.vi_name = '_CIVE'
        CIVE = np.where(self.check, 0.441*self.bands['R']-0.881*self.bands['G']+0.385*self.bands['B']+18.787, -9999)

        return CIVE

    def veg(self):
        '''
        Vegetativen = G/((R**a)*(B**(1-a)))
        a = 0.667  

        '''
        self.vi_name = '_VEG'
        a = 0.667
        VEG = np.where(self.check, (self.bands['G'])/((self.bands['R']**a)*(self.bands['B']*(1-a))), -9999)

        return VEG
    
#%%
def raster_export(input_path, output_array, vi_object):
        output_fn = input_path.stem + vi_object.vi_name
        output_ex = input_path.suffix
        output_dir = input_path.parent
        output_file = Path.joinpath(output_dir, output_fn).with_suffix(output_ex)
        print(output_file)
        with rio.open(
            str(PurePath(output_file)),
                'w',
                driver='GTiff',
                height=vi_object.image_shape[0],
                width=vi_object.image_shape[1],
                count=1,
                dtype=np.float32,
                crs=vi_object.image_crs,
                transform=vi_object.image_transform
                ) as dst:
                     dst.write(output_array, 1)    
#%%
# assign image class to object
image = veg_index(input_path)

#%%
# call veg index function and write new raster
vi = image.veg()

# write raster to file
raster_export(input_path=input_path, output_array=vi, vi_object=image)

#%%
# iterate through a list of vegetation indices
exec_methods = ["gcc", "tgi", "vari", "grvi", "ngrdi", "gli", "exg", "rgbvi", "mgrvi", "rgri", "cive", "veg"]
image = veg_index(input_path)
for method in exec_methods:
    output = getattr(image, method)()
    raster_export(input_path=input_path, output_array=output, vi_object=image)
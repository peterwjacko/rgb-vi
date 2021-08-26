# rgb-vi
![Banner](images/banner.png?raw=true)

Generate a selection of RGB vegetation indices using rasterio.

I used this as an opportunity to experiment with rasterio and python classes - there is probably a better way to do it. Some indices are playing up which I will have to fix.

Dependencies in environment.yml

Adapted from [Automating GIS processes](https://automating-gis-processes.github.io/CSC18/lessons/L6/raster-calculations.html)

NOTE: some of these indices were originally created using data from sensor with specific band wavelengths (e.g. RGRI) and therefore may not be appropriate for RGB colour space imagery.

## New Green-Red Vegetation Index
NGRVI = ((G**2)+(R**2))/((G**2)-(R**2))

Zhang, Xianlong, Fei Zhang, Yaxiao Qi, Laifei Deng, Xiaolong Wang, and Shengtian Yang. ‘New Research Methods for Vegetation Information Extraction Based on Visible Light Remote Sensing Images from an Unmanned Aerial Vehicle (UAV)’. International Journal of Applied Earth Observation and Geoinformation 78 (1 June 2019): 215–26. https://doi.org/10/gjhx6m.

## NGRDI
NGRDI = (G-B)/(G+B)

Tucker, Compton J. ‘Red and Photographic Infrared Linear Combinations for Monitoring Vegetation’. Remote Sensing of Environment 8, no. 2 (1 May 1979): 127–50. https://doi.org/10/d2t346.

## Visible Atmospheric Resistant Index
VARI = (G-R)/(G+R-B)

Gitelson, Anatoly A., Yoram J. Kaufman, Robert Stark, and Don Rundquist. ‘Novel Algorithms for Remote Estimation of Vegetation Fraction’. Remote Sensing of Environment 80, no. 1 (1 April 2002): 76–87. https://doi.org/10/fb3t2q.

## Red-Green Ratio Index 
RGRI = R/G  

Gamon, J. A., L. Serrano, and J. S. Surfus. ‘The Photochemical Reflectance Index: An Optical Indicator of Photosynthetic Radiation Use Efficiency across Species, Functional Types, and Nutrient Levels’. Oecologia 112, no. 4 (November 1997): 492–501. https://doi.org/10/bjbwkm.

## Modified green-red vegetation index 
MGRVI = ((G**2)-(R**2))/((G**2)+(R**2))

Bendig, Juliane, Kang Yu, Helge Aasen, Andreas Bolten, Simon Bennertz, Janis Broscheit, Martin L. Gnyp, and Georg Bareth. ‘Combining UAV-Based Plant Height from Crop Surface Models, Visible, and near Infrared Vegetation Indices for Biomass Monitoring in Barley’. International Journal of Applied Earth Observation and Geoinformation 39 (1 July 2015): 79–87. https://doi.org/10/f7d28f

## Excess green 
ExG = 2*G-R-B

M. Woebbecke, D., G. E. Meyer, K. Von Bargen, and D. A. Mortensen. ‘Color Indices for Weed Identification Under Various Soil, Residue, and Lighting Conditions’. Transactions of the ASAE 38, no. 1 (1995): 259–69. https://doi.org/10/gjtxm4.

## Color Index of Vegetation
CIVE = 0.441*R-0.881*G+0.385*B+18.787 

Kataoka, T., T. Kaneko, H. Okamoto, and S. Hata. ‘Crop Growth Estimation System Using Machine Vision’. In Proceedings 2003 IEEE/ASME International Conference on Advanced Intelligent Mechatronics (AIM 2003), 2:b1079-b1083 vol.2, 2003. https://doi.org/10/dxzmx5.

## Vegetativen 
VEG = G/((R**a)*(B**(1-a)))
a = 0.667

*Hague (2006) use a = 0.667 based on the centre wavelength of their camera's three colour filters. Consider changing from 0.667 to suit a specific camera*

Hague, T., N. D. Tillett, and H. Wheeler. ‘Automated Crop and Weed Monitoring in Widely Spaced Cereals’. Precision Agriculture 7, no. 1 (1 March 2006): 21–32. https://doi.org/10/ddwq3d.

## Red green-blue vegetation index 
RGBVI = ((G**2)-R*B)/((G**2)+R*B)

Bendig, Juliane, Kang Yu, Helge Aasen, Andreas Bolten, Simon Bennertz, Janis Broscheit, Martin L. Gnyp, and Georg Bareth. ‘Combining UAV-Based Plant Height from Crop Surface Models, Visible, and near Infrared Vegetation Indices for Biomass Monitoring in Barley’. International Journal of Applied Earth Observation and Geoinformation 39 (1 July 2015): 79–87. https://doi.org/10/f7d28f.

## Green leaf index 
GLI = (2*G-R-B)/(2*G+R+B)

Louhaichi, Mounir, Michael M. Borman, and Douglas E. Johnson. ‘Spatially Located Platform and Aerial Photography for Documentation of Grazing Impacts on Wheat’. Geocarto International 16, no. 1 (1 March 2001): 65–70. https://doi.org/10/bdz5sf.

## Green-red vegetation index 
GRVI = (G-R)/(G+R)

Rouse, J., R. H. Haas, J. A. Schell, and D. Deering. ‘Monitoring Vegetation Systems in the Great Plains with ERTS’. Undefined, 1973. https://www.semanticscholar.org/paper/Monitoring-vegetation-systems-in-the-great-plains-Rouse-Haas/fb2f60fe0fe2874e5cbf927a2556d719c32eac29.

## Triangular Greenness Index 
TGI = G-0.39*R-0.61*B

Hunt, E. Raymond, C. S. T. Daughtry, Jan U. H. Eitel, and Dan S. Long. ‘Remote Sensing Leaf Chlorophyll Content Using a Visible Band Index’. Agronomy Journal 103, no. 4 (2011): 1090–99. https://doi.org/10/c55v38.

## Green Chromatic Coordinate
GCC = G/(G+R+B)

M. Woebbecke, D., G. E. Meyer, K. Von Bargen, and D. A. Mortensen. ‘Color Indices for Weed Identification Under Various Soil, Residue, and Lighting Conditions’. Transactions of the ASAE 38, no. 1 (1995): 259–69. https://doi.org/10/gjtxm4.

## TODO: Elliptical Color Index
*Not implemented*

Lee, Moon-Kyu, Mahmood Reza Golzarian, and Inki Kim. ‘A New Color Index for Vegetation Segmentation and Classification’. Precision Agriculture 22, no. 1 (1 February 2021): 179–204. https://doi.org/10/gjhx6k.

bands = {
    R: 'Band1',
    G: 'Band2',
    B: 'Band3'
}

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
GLI = (2G-R-B)/(2G+R+B)

#Excess green # 
EXG = 2G-R-B

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
CIVE = 0.441*R−0.881*G+0.385*B+18.787

# Vegetativen #
a = 0.667
VEG = G/(R^a*B^(1−a))

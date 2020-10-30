import numpy as np
import pandas as pd
from sklearn.decomposition import pca 
from datasets import Leucegene

    # define a unit: 
    # lenght, duration, color hue, speed any thing ! # but let's stick to length
class Unit():
    def __init__(self, r,type="m" ):
        self.r = r
        self.type = "m"
    def __str__(self):
        print (self.r+self.type)
if __name__ == "__main__":
    # load data
    data = Leucegene.load_data(reload = True)
    # preprocess data
    data = Leucegene.preprocess(data)
    # project samples on pc1,2,3
    stars = Star().convert(data.projectwithpca(components = [0,1,2]))
    # create a galaxy
    pgalxy = PGalaxy( unit = 1e3, n_components = 3, groups=...)
    pggalxy.add_coordinates(stars)
    pggalxy.picture().save()
    pggalxy.animate(t=180).save() # in seconds


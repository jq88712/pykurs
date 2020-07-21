import pandas as pd
import numpy as np

pd.set_option('display.width', 700)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_colwidth', 100)
np.set_printoptions(linewidth=800)


f = open('example_file.txt', 'w')  # write
f.write('hello file')
f.close()

f_read = open('example_file.txt', 'r') # the 'r' flag means that we are going to read
mytext = f_read.read()
f_read.close()



class Auto:
    a = 1
    b = 2
    def fahren(self):
        self.gestartet = True
    def get_anz_raeder(self, x):
        self.d = x

a = Auto()
b = Auto()

b.get_anz_raeder()



import pandas

pandas.DataFrame()

import pandas as pd

pd.DataFrame()

from pandas import DataFrame

DataFrame()


import urllib.request

urllib.request.urlretrieve(
    "https://data.baltimorecity.gov/api/views/dz54-2aru/" +
    "rows.csv?accessType=DOWNLOAD",
    "cameras.csv")

import urllib.request as urlre

urlre.urlretrieve(
    "https://data.baltimorecity.gov/api/views/dz54-2aru/" +
    "rows.csv?accessType=DOWNLOAD",
    "cameras.csv")


import pandas as pd
import numpy as np

cameras = pd.read_csv("cameras.csv")

pd.set_option('display.width', 700)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_colwidth', 100)
np.set_printoptions(linewidth=800)


cameras.head()



cameras=pd.read_csv("https://data.baltimorecity.gov/api/views/dz54-2aru/"+
                    "rows.csv?accessType=DOWNLOAD")

cameras.to_csv("cameras_copy.csv", index=True)


from plotnine.data import mtcars
mtcars = mtcars.drop(["qsec", "wt"], axis=1, inplace=True)
mtcars.head(16)  # view the first 10 rows of the data frame

mtcars.mpg
mtcars['mpg']
mtcars[ ['mpg', 'cyl'] ].head()

mtcars[:3]
mtcars[::-5]


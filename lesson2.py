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

cameras.head()

cameras=pd.read_csv("https://data.baltimorecity.gov/api/views/dz54-2aru/"+
                    "rows.csv?accessType=DOWNLOAD")

cameras.to_csv("cameras_copy.csv", index=True)

from plotnine.data import mtcars
mtcars = mtcars.drop(["qsec", "wt"], axis=1, inplace=False)
mtcars.drop(["qsec", "wt"], axis=1, inplace=True)
mtcars.head(7)  # view the first 10 rows of the data frame

mtcars.mpg                       # in R: mtcars$mpg
mtcars['mpg']
mtcars[['mpg', 'cyl']].head()

type(mtcars.mpg)
type(mtcars['mpg'])
type(mtcars[['mpg']])

mtcars[:3]
mtcars[::-5]

# RICHTIG:
# ganze Tabelle = "dataset" = "Datenmenge" = "Datentabelle"
# Zeile = "data object", "data point" = "Datensatz"

mtcars[2]    # Fehler, da keine Spalte mit Namen "2" existiert
mtcars[2:3]  # die :-Notation splitted nach Zeilen
mtcars['mpg'][2]


row_names = [0, 3, 5, 7]

mtcars.loc[row_names, :]
mtcars.loc[3:6, 'mpg':'hp']

type(mtcars.loc[row_names, 'mpg'])
type(mtcars.loc[row_names, ['mpg', 'wt']])

# Suchen im Netz: "magic function Python"

mtcars.iloc[3:6,2:5]
mtcars.iloc[-8:-4,2:5]

mtcars2 = mtcars.set_index('name')
myrow = mtcars2.loc['Datsun 710':'Valiant', 'mpg':'hp']
type(myrow)

mtcars2.loc[2:5, 'mpg':'hp']   # funktioniert nicht, weil Position verwendet
mtcars2.iloc[2:5, 'mpg':'hp']  # funktioniert nicht, weil Namen verwendet

mtcars2.loc['Datsun 710':'Duster 360', 'mpg':'hp']
mtcars2.iloc[2:7, 0:4]

mtcars.loc[0:6, 'name':'hp']   # inklusive der hinteren Zahl
mtcars.iloc[2:7, 0:4]          # ohne die hintere Zahl



condition = mtcars["mpg"] > 21
mtcars.loc[condition, :]    # "magic function" __get_item__
mtcars.loc[ (mtcars.mpg > 20) & (mtcars.cyl==6), :]
mtcars.query('mpg>20 and cyl==6')

list(zip((mtcars.mpg > 20), (mtcars.cyl==6)))

mtcars2.loc['Mazda RX4', 'hp'] = 120  # "magic function" __set_item__

mtcars2.loc[:, 'am'] = 99

mtcars2.iloc[:, 8] = pd.Series(range(32))
mtcars2.drop('am', inplace=True)

mtcars2.loc[:, 'am'] = pd.Series(range(32))
mtcars.loc[:, 'am'] = 2*pd.Series(range(32))
mtcars2.loc[:, 'am'] = list(range(32))
mtcars2.loc[:, 'am'] = pd.Series(range(32)).values

mtcars.assign(am=pd.Series(range(32)))

mtcars2['new_col'] = 0
mtcars2.head()

mtcars2.loc[:,'new_col2']=3

mtcars2.assign(new_col3 = mtcars2.hp * 2).head()

mtcars2=mtcars2.drop(['new_col', 'new_col2'], axis=1)


condition = mtcars2.index.str.contains('Merc')
mtcars2.loc[~condition, :]

# bool ... element-wise
# and  ... &
# or   ... |
# not  ... ~

mtcars2.sort_values(by='disp', ascending=True).head()
mtcars2.sort_values(by=['gear', 'carb', 'disp'], ascending=[True, False, True]).head(10)

mtcars2.sort_index(ascending=False).head()


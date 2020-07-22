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

def myfct():
    return None

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


import urllib.request
urllib.request.urlretrieve("https://vincentarelbundock.github.io/" +
                           "Rdatasets/csv/datasets/airquality.csv",
                           "airquality.csv")
air_quality=pd.read_csv("airquality.csv")

air_quality = air_quality.drop("Unnamed: 0", axis=1) #droping ghost index

air_quality[['Month', 'Day', 'Ozone', 'Solar.R', 'Wind', 'Temp']]

air_quality.head()
long_airq = pd.melt(air_quality, id_vars=['Month','Day'], value_vars=['Wind', 'Temp'])
 #       >>> pd.melt(df, id_vars=['A'], value_vars=['B'])
long_airq.sort_values(by=['Month', 'Day'])

wide_airq = long_airq.pivot_table(index=['Month', 'Day'], columns="variable", values='value')
wide_airq.reset_index()




row_to_add = pd.DataFrame(data=np.array(([50,200,8,70,5,1],)),
                          columns=["Ozone","Solar.R","Wind","Temp","Month", "Day"])
air_quality.append(row_to_add).tail()

# BAD:
big_df = pd.DataFrame()
for i in range(10):
    small_df = fct()
    big_df = big_df.append(small_df)

# GOOD:
big_df_list = []  # Liste von DataFrames (jedes Element ist ein DataFrame)
for i in range(10):
    small_df = fct()
    big_df_list.append(small_df)
big_df = pd.concat(big_df_list)

air_quality['new_column']=0
air_quality.head()

number_of_rows = air_quality.shape[0]
new_array = np.arange(number_of_rows)
air_quality['new_column_2'] = new_array
air_quality.head()

a = np.arange(9).reshape((3,3))
b = np.arange(9,18).reshape((3,3))
df_a = pd.DataFrame(a, columns=["a","b","c"])
df_b = pd.DataFrame(b, columns=["a","e","f"])

pd.concat((df_a, df_b), axis=1)
pd.concat((df_a, df_b), axis=0)

df_b=pd.DataFrame(b,columns=["a","c","b"])
pd.concat((df_a, df_b), axis=0) # concatenate rows



import urllib.request
urllib.request.urlretrieve('https://vincentarelbundock.github.io/Rdatasets/csv/carData/States.csv',
                           "States.csv")
urllib.request.urlretrieve('https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/USstateAbbreviations.csv',
                           "USstateAbbreviations.csv")

edu_states=pd.read_csv("States.csv")
edu_states=edu_states.rename(columns={"Unnamed: 0": "abr"})
edu_states=edu_states[["abr","pop", "SATV"]].head()
edu_states

abr_states=pd.read_csv("USstateAbbreviations.csv")
abr_states=abr_states[["Name","ANSI.letters"]].head()
abr_states

pd.merge(edu_states, abr_states, left_on="abr", right_on="ANSI.letters")
pd.merge(edu_states, abr_states, left_on="abr", right_on="ANSI.letters", how='outer')
pd.merge(edu_states, abr_states, left_on="abr", right_on="ANSI.letters", how='right')
pd.merge(edu_states, abr_states, left_on="abr", right_on="ANSI.letters", how='left')



mtcars3 = mtcars2.drop(["drat", "vs", "disp"], axis=1)
mtcars3_stats = mtcars3.groupby(by=["cyl"]).describe()


mtcars3_statT = mtcars3_stats.\
    transpose().\
    reset_index().\
    rename(columns={'level_0': 'column_name', 'level_1': 'stat'})

mtcars3_statT = (mtcars3_stats.
                 transpose().
                 reset_index().
                 rename(columns={'level_0': 'column_name', 'level_1': 'stat'}))

mtcars3.groupby(by=["cyl"]).mean()

mtcars3.groupby(by=["cyl"]).aggregate(np.sum)

mtcars3.groupby(by=["cyl"]).agg([np.sum, np.mean, np.std])

mtcars3.groupby(by=["cyl", "am"]).agg([np.sum, np.mean, np.std])



mtcars.query('hp > 100').\
    sort_values(by=['gear', 'name'], ascending=True).\
    loc[:, ['hp','gear','mpg']].\
    assign(liter_km = lambda x: x.mpg * (1.6093/3.785441)).\
    groupby('gear').\
    mean()

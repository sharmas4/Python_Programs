import numpy as np
dt = np.dtype([('Country','S20'), ('density',np.int32), ('area', 'i4'),('population', 'i4')])
## for string, we can also use 'S21', 'S5' (it will clip string after 5 characters)
## 'i4' is similar to np.int32
population_table = np.array([
        ('Netherlands', 393, 41526, 16928800),
        ('Belgium', 337, 30510, 11007020),
        ('United Kingdom', 256, 243610, 62262000),
        ('Germany', 233, 357021, 81799600),
        ('Liechtenstein', 205, 160, 32842)
    ]
    , dtype=dt)


print(population_table)

print("List of countries: \n",population_table['Country'])  ## b at the
#starting of each string represents byte string (ASCII encoded, storable to machine/disk)

print('list of countries (in String, not bytes):\n',
      list(map(lambda x:x.decode('ASCII'),population_table['Country'])))


### To convert string x to byte: x.encode('ASCII')


print("subset of area: \n", population_table['area'][1:3])


### use save text to save the data in this array to a text file
'''
np.savetxt("polulation_table_Code_02.csv",
           population_table,
           fmt="%s;%d;%d;%d",
           delimiter=";")
'''



########### Example 2 ##############
# Figure out a data type definition for time records with entries for hours,
# minutes and seconds. Also add temperature to it.
print("\n","*"*75)
time_temp=np.dtype([('time',[('h',int),('m',int),('s',int)]),('temperature',np.float32)])

times_array=np.array([((11,41,17),20.8),((13,19,3),23.2)])

print('times_array:\n', times_array)


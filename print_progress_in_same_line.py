# in case of a huge number of iteration steps, it could be useful to print some data out for each iteration. To be informed about the progress of the processing.

# e.g. a for iteration

for index, row in data_geodataframe.iterrows():
  
  # do some important stuff
  
  # print information for each iteration in same line
  print('index = ' + str(index) + ' - Anzahl POIs = ' + str(len(pois)), end='\r')

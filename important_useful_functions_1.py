# some nice assistant functions for matplotlib plotting or data cleaning

def mm2inch(mm):
    return mm / 25.4

# to use RGB color format for matplotlib
def rgba2mpl(r,g,b,a=1.0):
    # build from 255,0,255,1 new form 1,0,1,1
    output = (0.0, 0.0, 0.0, 1.0)

    output = (r/255, g/255, b/255, a)

    return output

def rgb2hex(r,g,b):
    # build from 255,0,255,1 new hex color code

    return "#{:02x}{:02x}{:02x}".format(r,g,b)

# to label pie chart
def pie_label_function(pct):
    return ('%1.1f%%' % pct) if pct > 4 else ''

def my_level_list(data, values, threshold):
    # calc sum of all input data
    # determine for each value the percentage
    # organize output labels in reference to a threshold
    summe = 0.0
    summe = values.sum()
    
    list = []
    for i in range(len(data)):
        percentage = values[i] * 100 / float(summe)
        if percentage > threshold : #2%
            list.append(''+str(data[i]))
        else:
            list.append('')

    return list


# filter only tuples having no Null data
def tuples_notnull(col1, col2):
    temp_df = pd.DataFrame([col1, col2]).transpose()
    temp_df = temp_df.dropna()
    # length of final array
    n = len(temp_df)
    
    return np.array(temp_df[temp_df.columns[0]]), np.array(temp_df[temp_df.columns[1]]), n

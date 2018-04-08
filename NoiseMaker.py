import pandas as pd
from scipy.io import arff
import random
import decimal

data = arff.loadarff('test.arff')
df = pd.DataFrame(data[0])
count_noisepoints = 0
attributes_level = ["level0","level1","level2","level3","level4"]
attributes_car = ["car1","car2","car3","car4","car5","car6","car7","car8","car9","car10","car11","car12","car13","car14","car15","car16","car17","car18","car19","car20"]
attributes_zip = ["zipcode1","zipcode2","zipcode3","zipcode4","zipcode5","zipcode6","zipcode7","zipcode8","zipcode9"]
data_length = (len(df)*12)/3
data_points = data[0][0:10]

for line in data_points:
    for i in range(0,9):
        rand = random.randint(0, 9)
        if(rand >= 9): #skall generera brus pa 30% av datapunkterna
            if(i==3):
                line[i] = attributes_level[random.randint(0, 4)] #Ger random varde pa level
                #line[i] = "#"
            elif (i == 4):
                line[i] = attributes_car[random.randint(0, 19)] #Ger random varde pa car
                #line[i] = "#"
            elif (i == 5):
                line[i] = attributes_zip[random.randint(0, 8)] #Ger random varde pa level
                #line[i] = "#"
            else:
                line[i] *= (0.0001 * random.randint(0, 20000))
                #line[i] = 999
            count_noisepoints += 1


import re

d = { 'ARFF.html':
      data_points}


for original_filename in d.keys():
    m = re.search('^(.*)\.html$',original_filename,)
    if not m:
        print "Ignoring the file:", original_filename
        continue
    output_filename = m.group(1)+'.arff'
    with open(output_filename,"w") as fp:
        fp.write('''@relation 'generators.AgrawalGenerator '

@attribute salary numeric
@attribute commission numeric
@attribute age numeric
@attribute elevel {level0,level1,level2,level3,level4}
@attribute car {car1,car2,car3,car4,car5,car6,car7,car8,car9,car10,car11,car12,car13,car14,car15,car16,car17,car18,car19,car20}
@attribute zipcode {zipcode1,zipcode2,zipcode3,zipcode4,zipcode5,zipcode6,zipcode7,zipcode8,zipcode9}
@attribute hvalue numeric
@attribute hyears numeric
@attribute loan numeric
@attribute class {groupA,groupB}

@data

''')
        for word_and_count in d['ARFF.html']:
            print(word_and_count)
            fp.write("%f," % word_and_count[0])
            fp.write("%10.12f," % word_and_count[1])
            fp.write("%10.12f," % word_and_count[2])
            fp.write("%s," % word_and_count[3])
            fp.write("%s," % word_and_count[4])
            fp.write("%s," % word_and_count[5])
            fp.write("%10.12f," % word_and_count[6])
            fp.write("%10.12f," % word_and_count[7])
            fp.write("%10.12f," % word_and_count[8])
            fp.write("%s,\n" % word_and_count[9])


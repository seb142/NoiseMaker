import pandas as pd
from scipy.io import arff
import random
import decimal

class NoiseMaker():
    def __init__(self, number, noise):
        self.number = number
        self.noise = noise

        data = arff.loadarff('dataset/Ursprungsset/AbruptW1F1F5.arff')
        df = pd.DataFrame(data[0])
        count_noisepoints = 0
        total_points = 0
        attributes_level = ["level0","level1","level2","level3","level4"]
        attributes_car = ["car1","car2","car3","car4","car5","car6","car7","car8","car9","car10","car11","car12","car13","car14","car15","car16","car17","car18","car19","car20"]
        attributes_zip = ["zipcode1","zipcode2","zipcode3","zipcode4","zipcode5","zipcode6","zipcode7","zipcode8","zipcode9"]
        data_length = (len(df)*12)/3
        data_points = data[0]

        for line in data_points:
            for i in range(0,9):
                rand = random.uniform(0, 10)
                total_points += 1
                if(rand > (10-noise)): #kall generera brus pa 30% av datapunkterna
                    count_noisepoints += 1
                    if (i == 1):
                       # print("----------------------------------")
                        if(line[i] != 0):
                            line[i] *= (0.0001 * random.randint(0, 20000))
                        #    print(line[i], "test1")
                        else:
                            line[i] += 1
                            line[i] *= (0.0001 * random.randint(0, 20000))
                         #   print(line[i]," test2")

                    if(i==3):
                        #print("----------------------------------")
                        run = True
                        while(run):
                            tempLevel = attributes_level[random.randint(0, 4)]
                            if(line[i].decode('utf-8') != tempLevel):
                          #      print("Ej duplikat", line[i].decode('utf-8')," ", tempLevel)
                                line[i] = tempLevel#Ger random varde pa level
                                run = False
                                #line[i] = "#"


                    elif(i == 4):
                        #print("----------------------------------")
                        run = True
                        while (run):
                            tempLevel = attributes_car[random.randint(0, 19)]
                            if (line[i].decode('utf-8') != tempLevel):
                           #     print("Ej duplikat", line[i].decode('utf-8')," ", tempLevel)
                                line[i] = tempLevel  # Ger random varde pa level
                                run = False

                    elif (i == 5):
                        #print("----------------------------------")
                        run = True
                        while (run):
                            tempLevel = attributes_zip[random.randint(0, 8)]#Ger random varde pa level
                            if (line[i].decode('utf-8') != tempLevel):
                            #    print("Ej duplikat", line[i].decode('utf-8')," ", tempLevel)
                                line[i] = tempLevel  # Ger random varde pa level
                                run = False
                                #line[i] = "#"


                    else:
                        line[i] *= (0.0001 * random.randint(0, 20000))
                        #line[i] = 999
                       # print(0.0001 * random.randint(0, 20000)," ", line[i])


        import re
        d = {'AbruptW1F1F5Noise%02.1fN%d.html'%(noise,number):
              data_points}


        for original_filename in d.keys():
            m = re.search('^(.*)\.html$',original_filename,)
            if not m:
                print("Ignoring the file:", original_filename)
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
                for word_and_count in d['AbruptW1F1F5Noise%02.1fN%d.html'%(noise,number)]:
                    #print(word_and_count)
                    fp.write("%s," % word_and_count[0])
                    fp.write("%s," % word_and_count[1])
                    fp.write("%s," % word_and_count[2])
                    fp.write("%s," % word_and_count[3].decode('utf-8'))
                    fp.write("%s," % word_and_count[4].decode('utf-8'))
                    fp.write("%s," % word_and_count[5].decode('utf-8'))
                    fp.write("%s," % word_and_count[6])
                    fp.write("%s," % word_and_count[7])
                    fp.write("%s," % word_and_count[8])
                    fp.write("%s,\n" % word_and_count[9].decode('utf-8'))

                print("Noise points: ", count_noisepoints)
                print("Total points: ", total_points)
                print("Noise: ", noise)
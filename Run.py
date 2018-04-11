import NoiseMaker

noise = 1
for i in range(1,11):
    print("iteration: ", i)
    print("noise_calc: ",10-noise)
    NoiseMaker.NoiseMaker(i,noise)
    print("---------------")

noise = 1.5
for i in range(1,11):
    print("iteration: ", i)
    print("noise_calc: ",10-noise)
    NoiseMaker.NoiseMaker(i,noise)
    print("---------------")

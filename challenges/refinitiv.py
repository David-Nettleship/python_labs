#corridor of 100 lights
#run down 100 times, each time flicking the n lights on...

lights = 100
run = 1

while run < 6: 
    i = 1
    while i < lights+1:
        print(i)
        if (i%run == 0):
            print(str(i) + " light on!")
        i += 1
    print("Run: " + str(run))
    run += 1

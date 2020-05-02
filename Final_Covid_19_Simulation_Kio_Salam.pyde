# definition of variables 
x = [] 
y = []
healthy = []
time = 0
days = []
individuals = 27

def distance(x1,y1,x2,y2):
    a = y1-y2
    b = x1-x2
    c = sqrt(a*a + b*b) 
    return c 

def setup():
    size(600, 650)
    for individual in range (individuals):
        x.append(random (0, 600))
        y.append(random (0, 500))
        healthy.append("healthy")
        days.append(-1)
    healthy[0]= "sick"
    days[0]=30
def bargraph():
    global healthy, time
    fill(255)
    rect(150,620,12*individuals,22)
    rect(150,594,12*individuals,22)
    rect(150,568,12*individuals,22)
    fill (0)
    text("day {}".format(time), 5, 550)
    time=time+1
    line(0, 520, 600, 520)
    numberofinfected=0
    numberofhealthy=0
    numberofrecovered=0
    for individual in range (individuals):
        if healthy[individual] == "sick":
            numberofinfected = numberofinfected + 1
        if healthy[individual] == "healthy":
            numberofhealthy = numberofhealthy + 1
        if healthy[individual] == "recovered":
            numberofrecovered = numberofrecovered + 1
    text("number of infected {}".format(numberofinfected),5,636)
    text("number of healthy {}".format(numberofhealthy),5,610)
    text("number of recovered {}".format(numberofrecovered),5, 584)
    fill(255,0,0)
    rect(150,620,12*numberofinfected,22)
    fill(0,255,0)
    rect(150,594,12*numberofhealthy,22)
    fill(0,0,255)
    rect(150,568,12*numberofrecovered,22)
    
                        
def draw():
    global x, y, healthy
    background (255)
    strokeWeight(3)

    #create individual 
    for individual in range (individuals): 
        if healthy [individual]== "healthy":
            fill(0,255,0)
        elif healthy[individual]=="recovered":
            fill (0,0,255)
        else:
            fill(255,0,0)
        circle(x [individual], y[individual], 40)
        x[individual] = x[individual] + random(-15, 15)
        y[individual] = y[individual] + random(-15, 15)

        # boundaries conditions
        if x[individual] > 600:
            x[individual] = 600
        # add three more conditions
        if y[individual] > 500:
            y[individual] = 500
        if y[individual] < 0:
            y[individual] = 0
        if x[individual] < 0:
             x[individual] = 0
             
        if healthy[individual] == "sick":
            if days[individual]<= 0:
                healthy[individual]="recovered"
            else:
                JustinBieber= individual
                days[JustinBieber]=days[JustinBieber]-1
                for SelenaGomez in range(individuals):
                    if healthy[SelenaGomez]=="healthy" and distance(x[JustinBieber],y[JustinBieber],x[SelenaGomez],y[SelenaGomez])<40:
                        healthy[SelenaGomez] = "sick"
                        days[SelenaGomez]= random(20,40)
    bargraph()
    delay(101)

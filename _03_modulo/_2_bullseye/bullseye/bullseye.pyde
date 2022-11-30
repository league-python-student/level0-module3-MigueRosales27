def setup():
    # Set the size of your sketch

    size(400,400)
    colorMode(HSB,360,100,100)


    pass


def draw():

    besize=100

    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    background(0,0,100)

    for i in range(10):


        if( i%2==0):
            fill(0,100,100)

        else:
            fill(190,100,80);

        ellipse(200,200,besize,besize)
        besize=besize-10







    # Use an if statement and modulo to alternate the color of your rings


    pass
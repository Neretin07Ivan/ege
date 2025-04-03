from turtle import *
c = 50
tracer(0)
lt(90)
for i in range(21):
    fd(6*c)
    rt(60)
up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*c,y*c)
        dot(4 ,"red")
update()
done()
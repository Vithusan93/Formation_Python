import turtle

def escalier(taille,nb):
    
    t = turtle.Turtle()

    for i in range (0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        #taille = taille - 10
    t.forward(taille)

    turtle.done()

#escalier(60,5)

def carre(taille):
    t = turtle.Turtle()

    for i in range (0, 4):
        t.forward(taille)
        t.left(90)
    turtle.done()

carre(50)


#t.forward(100)
#t.left(90)
# t.forward(50)
#t.backward(100)
#t.right(45)
#t.forward(200)
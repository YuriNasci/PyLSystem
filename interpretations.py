'''
Created on 20/11/2014

@author: YuriNasci
'''
import math
import turtle

def interpret_turtle_2D(word, angle, d = 1, start = ''):
    turn_left = '+'
    turn_right = '-'
    forward_drawing = 'F'
    forward_no_drawing = 'f'
    push = '['
    pop = ']'

    stack = []

    turtle.hideturtle()
    turtle.tracer(0)
    if (start): turtle.setpos(start)
    turtle.setheading(90)
    # Verificar cada simbolo na palavra
    for letter in word:
        if (letter == forward_drawing):
            if (not turtle.isdown()): turtle.pendown()
            turtle.forward(d)
        elif (letter == forward_no_drawing):
            if (turtle.isdown()): turtle.penup()
            turtle.forward(d)
        elif (letter == turn_left):
            turtle.left(angle)     
        elif (letter == turn_right):
            turtle.right(angle)
        elif (letter == push):
            stack.append((turtle.heading(), turtle.pos()))
        elif (letter == pop):
            turtle.setheading(stack[-1][0])
            turtle.setpos(stack[-1][1])
            stack.pop()
    # Fim do for
    turtle.update()            
# Fim do metodo turtle_interpretation_2D

# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 10:12:42 2019

@author: student
"""
#%%
import random
import time
def pri():
    print('''
-------------------------------------------------
|           |           |           |           |
|           |           |           |           |
|   ''',dit['a'],'''     |   ''',dit['b'],'''     |   ''',dit['c'],'''     |   ''',dit['d'],'''     |
|           |           |           |           |
|           |           |           |           |
-------------------------------------------------
|           |           |           |           |
|           |           |           |           |
|   ''',dit['e'],'''     |   ''',dit['f'],'''     |   ''',dit['g'],'''     |   ''',dit['h'],'''     |
|           |           |           |           |
|           |           |           |           |
-------------------------------------------------
|           |           |           |           |
|           |           |           |           |
|   ''',dit['i'],'''     |   ''',dit['j'],'''     |   ''',dit['k'],'''     |   ''',dit['l'],'''     |
|           |           |           |           |
|           |           |           |           |
-------------------------------------------------
|           |           |           |           |
|           |           |           |           |
|   ''',dit['m'],'''     |   ''',dit['n'],'''     |   ''',dit['o'],'''     |   ''',dit['p'],'''     |
|           |           |           |           |
|           |           |           |           |
-------------------------------------------------
''')

dit={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0}

a=dit['a']
b=dit['b']
c=dit['c']
d=dit['d']
e=dit['e']
f=dit['f']
g=dit['g']
h=dit['h']
i=dit['i']
j=dit['j']
k=dit['k']
l=dit['l']
m=dit['m']
n=dit['n']
o=dit['o']
p=dit['p']



rules='''
RULES----

Use W,S,D,A to move up down right or left
W- UP
A- LEFT
S- DOWN
D- RIGHT

All the numbers move in the direction specified

Same numbers add up

The goal is to reach the number 2048

If all the squares get filled up with numbers and no moves are possible,the game ends
'''


print(rules)

time.sleep(10)

print('LETS GOOO....')

time.sleep(2)

kit=list(dit.keys())

def val():
    x=random.choice(kit)
    while dit[x]!=0:
       x=random.choice(kit)
       print(x)
    print(x)
    ra=random.choice([2,4])
    dit[x]+=ra
         
    
val()
pri()
print('HI')

while a==0 or b==0 or c==0 or d==0 or e==0 or f==0 or g==0 or h==0 or i==0 or j==0 or k==0 or l==0 or m==0 or n==0 or o==0 or p==0:
    move=str(input('ENTER A LETTER AS PER THE RULES MENTIONED ABOVE'))
    if move=='W':
        if m==a and e==0 and i==0:
            dit['a']=dit['m']+dit['a']
            dit['m']=0
            print('HI1')
        elif i==a and e==0:
            dit['a']=dit['i']+dit['a']
            dit['i']=0
            print('HI2')
        elif e==a:
            dit['a']=dit['e']+dit['a']
            dit['e']=0
            print('HI3')
        elif m==e and i==0:
            if a==0:
                dit['a']=dit['e']+dit['m']
                dit['e']=0
                dit['m']=0
                print('HI4')
            else:
                dit['e']=dit['e']+dit['m']
                dit['m']=0
                print('HI5')
        elif i==e:
            if a==0:
                dit['a']=dit['e']+dit['i']
                dit['e']=0
                dit['i']=0
                print('HI6')
            else:
                dit['e']=dit['e']+dit['i']
                dit['i']=0
                print('HI7')
        elif m==i:
            if a==0 and e==0:
                dit['a']=dit['m']+dit['i']
                dit['m']=0
                dit['i']=0
                print('HI8')
            elif a!=0 and e==0:
                dit['e']=dit['i']+dit['m']
                dit['m']=0
                dit['i']=0
                print('HI9')
            else:
                dit['e']=dit['e']+dit['i']
                dit['i']=0
                print('HI10')
                
                
                
        if n==b and f==0 and j==0:
            dit['b']=dit['n']+dit['b']
            dit['n']=0
        elif j==b and f==0:
            dit['b']=dit['j']+dit['b']
            dit['j']=0
        elif f==b:
            dit['b']=dit['f']+dit['b']
            dit['f']=0
        elif n==f and j==0:
            if dit['b']==0:
                dit['b']=dit['f']+dit['n']
                dit['f']=0
                dit['n']=0
            else:
                dit['f']=dit['f']+dit['n']
                dit['n']=0
        elif j==f:
            if b==0:
                dit['b']=dit['f']+dit['j']
                dit['f']=0
                dit['j']=0
            else:
                dit['f']=dit['f']+dit['j']
                dit['j']=0
        elif n==j:
            if b==0 and f==0:
                dit['b']=dit['n']+dit['j']
                dit['n']=0
                dit['j']=0
            elif b!=0 and f==0:
                dit['f']=dit['j']+dit['n']
                dit['n']=0
                dit['j']=0
            else:
                dit['f']=dit['f']+dit['j']
                dit['j']=0
                
                
        if o==c and g==0 and k==0:
            dit['c']=dit['o']+dit['c']
            dit['o']=0
        elif k==c and g==0:
            dit['c']=dit['k']+dit['c']
            dit['k']=0
        elif g==c:
            dit['c']=dit['g']+dit['c']
            dit['g']=0
        elif o==g and k==0:
            if c==0:
                dit['c']=dit['g']+dit['o']
                dit['g']=0
                dit['o']=0
            else:
                dit['g']=dit['g']+dit['o']
                dit['o']=0
        elif j==g:
            if c==0:
                dit['c']=dit['g']+dit['k']
                dit['g']=0
                dit['k']=0
            else:
                dit['g']=dit['g']+dit['k']
                dit['k']=0
        elif o==k:
            if c==0 and g==0:
                dit['c']=dit['o']+dit['k']
                dit['o']=0
                dit['k']=0
            elif c!=0 and g==0:
                dit['g']=dit['k']+dit['o']
                dit['o']=0
                dit['k']=0
            else:
                dit['g']=dit['g']+dit['k']
                dit['k']=0
                
                
        if p==d and h==0 and l==0:
            dit['d']=dit['p']+dit['d']
            dit['p']=0
        elif l==d and h==0:
            dit['d']=dit['l']+dit['d']
            dit['l']=0
        elif h==d:
            dit['d']=dit['h']+dit['d']
            dit['g']=0
        elif p==h and l==0:
            if d==0:
                dit['d']=dit['h']+dit['p']
                dit['h']=0
                dit['p']=0
            else:
                dit['h']=dit['h']+dit['p']
                dit['p']=0
        elif l==h:
            if d==0:
                dit['d']=dit['l']+dit['h']
                dit['h']=0
                dit['l']=0
            else:
                dit['h']=dit['h']+dit['l']
                dit['l']=0
        elif p==l:
            if d==0 and h==0:
                dit['d']=dit['p']+dit['l']
                dit['p']=0
                dit['l']=0
            elif d!=0 and h==0:
                dit['h']=dit['l']+dit['p']
                dit['p']=0
                dit['l']=0
            else:
                dit['h']=dit['h']+dit['l']
                dit['l']=0
            
            
            
            
            
        
        val()
        pri()
        print(dit)
            
            
            
            
            

#%%
from tkinter import *
from random import randint as ri
from copy import copy

import cell

WIDTH = 400


class App:
    def __init__(self, parent):

        self.root = parent

        # Array where all the cells are saved
        self.table = [`0] * 16
        # Boolean to control user inputs to avoid too many clicks
        self._canclick = True
        # Score
        self._score = 0

        # Draws all the tkinter elements
        self.main_canvas = Canvas(self.root, width=WIDTH, height=WIDTH, bg="lightblue")
        self.main_canvas.pack()
        self.second_frame = Frame(self.root)
        self.second_frame.pack()
        self._scorevar = StringVar()
        self._scorevar.set(self._score)
        self._sframesetup()

        # Draws the horizontal and vertical lines
        self._griddraw()

        # Draws the cells
        self._cellsetup(3)

    def callback(self, direction):
        """ Handles the user input

            direction: LEFT, RIGHT, DOWN, UP = 0, 1, 2, 3"""
        if self._canclick:
            self._canclick = False  # Blocks the user input

            # Makes a copy of the table to check later if something changed or not
            backup = copy(self.table)

            d = dict(enumerate([self._left, self._right, self._down, self._up]))
            d[direction]()  # Calls the right movement function

            # Check if there is space to spawn a new cell
            if not 0 in self.table:
                self._lose()
                return

            if backup != self.table:
                # Waits until the cells stop and spawns a new one
                self.root.after(301, self._spawnnew)
            else:
                self._canclick = True

    def restart(self):
        """ Restart button callback """

        # deletes lose text
        self.main_canvas.delete("d72819d9")

        # deletes all cells
        self.table = [0] * 16

        self._cellsetup(3)
        self._scorevar.set(0)

    def _sframesetup(self):
        pointframe = Frame(self.second_frame)
        pointframe.pack(side=LEFT, pady=20, padx=20)

        Label(pointframe, text="Punteggio:").pack(side=LEFT)
        Label(pointframe, textvariable=self._scorevar).pack(side=LEFT)

        restartb = Button(self.second_frame, text="Restart", command=self.restart)
        restartb.pack(side=RIGHT, pady=20, padx=20)

    def _griddraw(self):
        """ Draws the horizontal and vertical lines """

        line_color = "blue"
        cell_width = WIDTH / 4

        for n in range(1, 4):
            # Vertical lines
            self.main_canvas.create_line(n * cell_width, 0, n * cell_width, WIDTH, fill=line_color)
            # Horizontal lines
            self.main_canvas.create_line(0, n * cell_width, WIDTH, n * cell_width, fill=line_color)

    def _cellsetup(self, nstart):
        """ Spawns 'nstart' new cells and draws them """

        for _ in range(nstart):
            self._spawnnew()

    def _lose(self):
        """ Function called when the user is not able to continue the game """

        self.main_canvas.create_text(WIDTH / 2, WIDTH / 2, text="GAME OVER", font=("Helvetica", 25), tag="d72819d9")

    def _spawnnew(self):
        """ Creates a new cell and draws it in an empty space """

        while True:
            pos = ri(0, 15)  # Pick a random idx
            if self.table[pos]:
                # If the position is already taken, restart the loop
                continue

            posconv = pos % 4, int(pos / 4)  # Converts the new idx into (x, y)

            self.table[pos] = cell.Cell(self.main_canvas, self.root, posconv, WIDTH / 4, n=2 ** ri(1, 3))
            break

        # Let the user be able to click again
        self._canclick = True

    def _right(self):
        """ Moves all the cells to the right side """

        for idx in list(range(len(self.table)))[::-1]:  # Iterates the array backwards

            if self.table[idx]:  # Checks if there's a cell

                c = self.table[idx]  # Saves the cell because 'idx' will change later
                while (idx + 1) % 4:  # Keeps going till it reaches the left side

                    # 1° CASE: Two cells add up
                    if self.table[idx + 1] and self.table[idx + 1].n == self.table[idx].n:
                        self.table[idx + 1].double()  # Doubles a cell
                        self._scorevar.set(int(self._scorevar.get()) + self.table[idx + 1].n)  # Updates the score label
                        self.table[idx] = 0  # Deletes the other
                        idx += 1
                        break

                    # 2° CASE: The cell stops
                    elif self.table[idx + 1]:
                        break

                    # 3° CASE: The cell moves to the left
                    else:
                        self.table[idx + 1] = self.table[idx]
                        self.table[idx] = 0
                        idx += 1

                # Updates the canvas object of the cell and his '.pos' attribute
                newx, newy = idx % 4, int(idx / 4)
                c.move(newx - c.pos[0], newy - c.pos[1])
                c.pos = newx, newy

    def _left(self):
        """ Moves all the cells to the left side """

        for idx in range(len(self.table)):  # # Iterates the array from the beginning

            if self.table[idx]:

                c = self.table[idx]
                while idx % 4:

                    if self.table[idx - 1] and self.table[idx].n == self.table[idx - 1].n:
                        self.table[idx - 1].double()
                        self._scorevar.set(int(self._scorevar.get()) + self.table[idx - 1].n)
                        self.table[idx] = 0
                        idx -= 1
                        break

                    elif self.table[idx - 1]:
                        break

                    else:
                        self.table[idx - 1] = self.table[idx]
                        self.table[idx] = 0
                        idx -= 1

                newx, newy = idx % 4, int(idx / 4)
                c.move(newx - c.pos[0], newy - c.pos[1])
                c.pos = newx, newy

    def _down(self):
        """ Moves all the cells to the bottom """

        for idx in list(range(len(self.table)))[::-1]:

            if self.table[idx]:

                c = self.table[idx]
                while not 12 <= idx <= 15:

                    if self.table[idx + 4] and self.table[idx + 4].n == self.table[idx].n:
                        self.table[idx + 4].double()
                        self._scorevar.set(int(self._scorevar.get()) + self.table[idx + 4].n)
                        self.table[idx] = 0
                        idx += 4
                        break

                    elif self.table[idx + 4]:
                        break

                    else:
                        self.table[idx + 4] = self.table[idx]
                        self.table[idx] = 0
                        idx += 4

                newx, newy = idx % 4, int(idx / 4)
                c.move(newx - c.pos[0], newy - c.pos[1])
                c.pos = newx, newy

    def _up(self):
        """ Moves all the cells to the top """

        for idx in range(len(self.table)):

            if self.table[idx]:

                c = self.table[idx]
                while not 0 <= idx <= 3:

                    if self.table[idx - 4] and self.table[idx - 4].n == self.table[idx].n:
                        self.table[idx - 4].double()
                        self._scorevar.set(int(self._scorevar.get()) + self.table[idx - 4].n)
                        self.table[idx] = 0
                        idx -= 4
                        break

                    elif self.table[idx - 4]:
                        break

                    else:
                        self.table[idx - 4] = self.table[idx]
                        self.table[idx] = 0
                        idx -= 4

                newx, newy = idx % 4, int(idx / 4)
                c.move(newx - c.pos[0], newy - c.pos[1])
                c.pos = newx, newy


    root = Tk()

app = App(root)w

root.bind("<a>", lambda event: app.callback(0))
root.bind("<d>", lambda event: app.callback(1))
root.bind("<w>", lambda event: app.callback(3))
root.bind("<s>", lambda event: app.callback(2))

root.bind("<r>", lambda event: app.restart())

root.mainloop()
    #%%
    


import tkinter as tk # importuje biblioteke 

import random as rn

def main():
    
    dt = 220 # prędkośc węża 
    
    window = tk.Tk() 
    
    window.title("Projekt") # Nazwa okna 
    
    myCanvas = tk.Canvas(window, width = 600, height = 400) # Tworzenie okna 
    myCanvas.pack() 
    
    class Snake: # klasa 
        def __init__(self, width, height): 
            self.width = int(width) # szerokość 
            self.height = int(height) # wysokośc 
            self.msnake = [[self.width / 2, self.height / 2], [self.width / 2 + 1, self.height / 2], [self.width / 2 + 2, self.height / 2]] 
            self.move = 0
            self.tmove = [[0,1],[1,0],[0,-1],[-1,0]] # Wektor kierunku ruchu węża 
            self.size = 10
            self.gameover = False 
            self.food = [rn.randint(1, self.width - 2), rn.randint(1, self.height - 2)]
        def drawBox(self,x, y, color = 'yellow'): # Kolor obramowania i obiektu 
            myCanvas.create_rectangle([x, y, x + self.size, y + self.size], fill=color)
        def draw(self):
            myCanvas.delete("all")
            if self.gameover: # Tworzenie pętli 
                myCanvas.create_text([self.width / 2 * self.size, self.height / 2 * self.size], text = "Przegrałeś") 
            else:
                for i in range(self.width):  
                    self.drawBox(i * self.size, 2)
                    self.drawBox(i * self.size, (self.height - 1) * self.size)
                for i in range(1, self.height):
                    self.drawBox(0, i * self.size)
                    self.drawBox((self.width - 1) * self.size, i * self.size)
                for i in self.msnake:
                    self.drawBox(i[0] * self.size, i[1] * self.size)
                self.drawBox(self.food[0] * self.size, self.food[1] * self.size, color = 'red')
        def eat(self): 
            if self.msnake[0][0] == self.food[0] and self.msnake[0][1] == self.food[1]:  
                self.msnake.append([0,0]) # Dodawanie elementów do obiektu 
                self.food = [rn.randint(1, self.width - 2), rn.randint(1, self.height - 2)] # Losowe wyskakiwanie "jedzenia"
        def move_snake(self):
            for i in range(len(self.msnake) - 1,0,-1):
                self.msnake[i][0] = self.msnake[i-1][0]
                self.msnake[i][1] = self.msnake[i-1][1]
            self.msnake[0][0] += self.tmove[self.move][0]
            self.msnake[0][1] += self.tmove[self.move][1]
            self.colision()
            self.eat()
            self.draw()
        def turnLeft(self):
            self.move = (self.move + 1) % len(self.tmove)
        def turnRight(self):
            self.move = (self.move - 1) if self.move > 0 else len(self.tmove) - 1
        def colision(self):
            if self.msnake[0][0] == 0 or self.msnake[0][1] == 0 or self.msnake[0][0] == self.width - 1 or self.msnake[0][1] == self.height - 1:
                self.gameover = True
            for i in self.msnake[1:]: 
                if self.msnake[0][0] == i[0] and self.msnake[0][1] == i[1]:
                    self.gameover = True
        def reset(self):
            self.gameover = False
            self.msnake = [[self.width / 2, self.height / 2], [self.width / 2 + 1, self.height / 2], [self.width / 2 + 2, self.height / 2]] 
            self.move = 0 
            self.tmove = [[0,1],[1,0],[0,-1],[-1,0]] 
            self.size = 10
            self.gameover = False 
            self.food = [rn.randint(1, self.width - 2), rn.randint(1, self.height - 2)]
            window.after(dt, move)
    
    sn = Snake(600 / 10, 400 / 10)
    
    menubar = tk.Menu(window)
    menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Menu", menu=menu)
    menu.add_command(label="Od nowa", command = sn.reset)
    menu.add_command(label="Wyjście", command = window.quit)
    window.config(menu=menubar)
    
    sn.draw()
    def move():
        sn.move_snake()
        if not sn.gameover:
            window.after(dt, move)
   
    def turnLeft(event):
        sn.turnLeft()
    def turnRight(event):
        sn.turnRight()
    

    window.after(dt, move)
    window.bind_all("<KeyPress-Left>", turnLeft)
    window.bind_all("<KeyPress-Right>", turnRight)
    
    
    window.mainloop()
    
    return 0

if __name__ == '__main__':
    main()
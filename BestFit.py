import tkinter as tk

root=tk.Tk()
canvas2=tk.Canvas(root, width=200,height=1000)
canvas1=tk.Canvas(root, width=1000,height=1000)

# creation de la classe rectangle
class Rectangle:
    def __init__(self,w,h):
        self.w = w
        self.h = h

# creation de la classe espace
class Espace:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        


# focntion pour prendre de maximum d un tableau
def get_Max(tab):
    idMax=-1
    MaxValue=-40
    i=0
    for t in tab:
        if MaxValue < t.h*t.w:
            MaxValue = t.h*t.w
            idMax = i
        i=i+1
    return idMax


# fonction tri decroissant selon l Aire
def tri_decroissant(Rectangles):
    result=[]
    if len(Rectangles) > 1:
        idmax=get_Max(Rectangles)
        maxValue=Rectangles[idmax]
        Rectangles.pop(idmax)
        result=tri_decroissant(Rectangles)
        result.insert(0,maxValue)
    else:
        result=Rectangles
    return result


def getEspaceRestant(espace,rectangle):
    espaceLibre=[]
    # espace a droite
    if rectangle.w < espace.w:
        E=Espace(espace.x+rectangle.w,espace.y,espace.w-rectangle.w,espace.h)
        espaceLibre.append(E)
    #espace a gauche
    if rectangle.h < espace.h:
        E=Espace(espace.x,espace.y+rectangle.h,espace.w,espace.h-rectangle.h)
        espaceLibre.append(E)
    return espaceLibre
#prendre la valeur de l espace minimum
def getBestRestant(Reste):
    minAire=1000000
    espaceMin=None
    for r in Reste:
        if r.h*r.w < minAire:
            espaceMin=r
            minAire=r.h*r.w
    return espaceMin



#f
def addToNewEspace(NewSurface,E):
    surface=NewSurface
    for e in E:
        surface.append(e)
    return surface

#  fonction pour mettre a les surface libres
def EditSurfaceLibre(surface_Libre,position,rectangle):
    NewSurface=[]
    for libre in surface_Libre:
        if libre.x == position["x"] and libre.y == position["y"]:
            E=getEspaceRestant(libre,rectangle)
            NewSurface=addToNewEspace(NewSurface,E)
        else:
            NewSurface.append(libre)
    return NewSurface

def addNewRectangle(pos,rect):
    canvas1.create_rectangle(pos["x"],pos["y"],pos["x"]+rect.w,pos["y"]+rect.h,fill=None,outline="black")
    
def sumEspace(espaceRestants):
    total=0
    for e in espaceRestants:
        total=total+e.w*e.h
    return total

def BestFit(Rectangles,conteneur):
    surface_libre=[]
    surface_libre.append(conteneur)
    for rectangle in Rectangles:
        bestFit=None
        bestposition=None
        for espace in surface_libre:
            if rectangle.w <= espace.w and rectangle.h <= espace.h:
                espaceRestants=getEspaceRestant(espace,rectangle)
                waste = sum(e.w*e.h for e in espaceRestants)                
                if bestFit is None or waste < (bestFit.w*bestFit.h):
                    bestposition={"x":espace.x, "y":espace.y}
                    bestFit=getBestRestant(espaceRestants)
                    print(bestposition)
    
        if bestFit != None:
            surface_libre=EditSurfaceLibre(surface_libre,bestposition,rectangle)
            addNewRectangle(bestposition,rectangle)
        else:
            break  
    
    
#finction pour ajouter le rectangle
def addRectangle(width_entry,height_entry):
    try:
        width=int(width_entry.get())
        height=int(height_entry.get())
        Rectangles.append(Rectangle(width,height))
        Rect=tri_decroissant(Rectangles)
        canvas1.delete("all")
        initialise(Rect,Surface)
    except ValueError:
        print("Invalid")

def initialise_position(Rectangles,canvas):
    i=0
    x_pos=20
    ecart=40
    y_pos=20
    
    for rect in Rectangles:
        x1=x_pos
        x2=x_pos+rect.w
        y1=y_pos
        y2=y_pos+rect.h
        canvas.create_rectangle(x1,y1,x2,y2,fill="blue",outline="black")
        x_pos=x_pos+rect.w+ecart




def initialise(Rectangle,surface):
    root.title("Best Fit Function 2D")
    root.geometry("1200x1000")
    x_pos=surface.x
    y_pos=surface.y
    canvas1.create_rectangle(x_pos,y_pos,x_pos+surface.w,y_pos+surface.h,fill=None,outline="black")
    BestFit(Rectangle,surface)
    initialise_position(Rectangle,canvas1)
    #ajout du deuxieme canvas
    canvas2.config(bg="green")
    addButton=tk.Button(root,text="ajouter le rectangle",command=lambda:addRectangle(width_entry,height_entry))
    label_w=tk.Label(root,text="width")    
    label_h=tk.Label(root,text="height")
    width_entry=tk.Entry(root)
    height_entry= tk.Entry(root)
    
    canvas2.create_window(100,50,window=label_w)
    canvas2.create_window(100,100,window=width_entry)
    canvas2.create_window(100,150,window=label_h)
    canvas2.create_window(100,200,window=height_entry)
    
    
    canvas2.create_window(100,250,window=addButton)
    
    canvas1.grid(row=0,column=0,padx=0,pady=0)
    canvas2.grid(row=0,column=1,padx=0,pady=0)
    
    root.mainloop()





Rectangles=[]
Rectangles.append(Rectangle(100,50))
Rectangles.append(Rectangle(150,70))
Rectangles.append(Rectangle(120,120))
Rectangles.append(Rectangle(50,90))
Rectangles.append(Rectangle(110,130))

Surface=Espace(200,350,300,300)
Rectangles=tri_decroissant(Rectangles)
for r in Rectangles:
    print(r.w)
initialise(Rectangles,Surface)
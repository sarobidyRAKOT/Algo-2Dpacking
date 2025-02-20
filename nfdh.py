import tkinter as tk

root=tk.Tk()
canvas2=tk.Canvas(root, width=200,height=1000)
canvas1=tk.Canvas(root, width=1000,height=1000)

# focntion pour prendre de maximum d un tableau
def get_Max(tab):
    idMax=-1
    MaxValue=-40
    i=0
    for t in tab:
        if MaxValue < t['h']:
            MaxValue = t['h']
            idMax = i
        i=i+1
    return idMax


# fonction de tri d un tablaue
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
# focntion pour initialiser les composants
def initialise_position(Rectangles,R,canvas):
    i=0
    x_pos=20
    ecart=40
    y_pos=20
    canvas.create_rectangle(200,350,200+R["W"],350+R["H"],fill=None,outline="black")
    for rect in Rectangles:
        x1=x_pos
        x2=x_pos+rect["w"]
        y1=y_pos
        y2=y_pos+rect["h"]
        canvas.create_rectangle(x1,y1,x2,y2,fill="blue",outline="black")
        x_pos=x_pos+rect["w"]+ecart



#fonction pour placer le recantgles
def place_rectangles(Rectangles,R,canvas):
    x_pos=200
    y_pos=350
    
    current_width=0
    initial_width=x_pos
    current_height=y_pos+R["H"]
    
    niveau_height=current_height-Rectangles[0]["h"]
    # dessiner le conteneur
    canvas.create_rectangle(x_pos,y_pos,x_pos+R["W"],y_pos+R["H"],fill=None,outline="black")
    i=0
    for rect in Rectangles:
        if rect["w"]+current_width < R["W"]:
            canvas.create_rectangle(initial_width+current_width,current_height-rect["h"],initial_width+current_width+rect["w"],current_height,fill=None,outline="black")
            current_width+=rect["w"]
            
        else:
            current_width=0
            current_height=niveau_height
            niveau_height=niveau_height-rect["h"]
            canvas.create_rectangle(initial_width+current_width,current_height-rect["h"],initial_width+current_width+rect["w"],current_height,fill=None,outline="black")
            current_width+=rect["w"]        
            
            
#finction pour ajouter le rectangle
def addRectangle(width_entry,height_entry):
    try:
        width=int(width_entry.get())
        height=int(height_entry.get())
        Rectangles.append({'w':width,'h':height})
        Rect=tri_decroissant(Rectangles)
        canvas1.delete("all")
        initialise(Rect,R)
    except ValueError:
        print("Invalid")



# fonction pour creer la fenetre 
def initialise(Rectangles,R):
    print(Rectangles)
    root.title("Fit Function 2D")
    root.geometry("1200x1000")
        
# initilalisation du premier canvas
    place_rectangles(Rectangles,R,canvas1)
    initialise_position(Rectangles,R,canvas1)

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
Rectangles.append({'w':100,'h':50})
Rectangles.append({'w':150,'h':70})
Rectangles.append({'w':120,'h':120})
Rectangles.append({'w':50,'h':90})
Rectangles.append({'w':110,'h':130})


R={'W':300,'H':300}
# applen de la fonction tri
Rectangles=tri_decroissant(Rectangles)

initialise(Rectangles,R)
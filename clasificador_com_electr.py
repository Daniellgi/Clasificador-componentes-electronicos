import cv2
import numpy as np
import time 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk #Para descargar la librería que me deja subir fotos en la ventana principal
import numpy as np
import cv2
import PIL.Image, PIL.ImageTk
import serial
arduino = serial.Serial("COM4", 9600)
time.sleep(2)

classes = ["resistencia","diodo","capacitor","transistor","led","integrado","rele","potenciometro","trimer","boton","switch","cristal"]
classesNum = [0,0,0,0,0,0,0,0,0,0,0,0]

clasesDispensador=[["11","12","13","14","15","16","17","18","19","110","111","112"],
                   ["21","22","23","24","25","26","27","28","29","210","211","212"]]

##global bandera=True

root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir")

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Conectar")
borrarMenu.add_command(label="Salir")

HelpMenu=Menu(barraMenu, tearoff=0)
HelpMenu.add_command(label="Licencia")
HelpMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="Conectar", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="Ayuda", menu=HelpMenu)

onevar = BooleanVar()
onevar.set(False)

twovar = BooleanVar()
twovar.set(False)

velbanda=IntVar()
velbanda.set(0)

timetolva=IntVar()
timetolva.set(0)

iniciarVar=BooleanVar()
iniciarVar.set(False)

banderaIniciar=BooleanVar()
banderaIniciar.set(False)

miFrame = ttk.Frame(root, padding=(5,5,5,5))
miFrame.pack()

#-------------------------Control Frame---------------------------


#bandera=False
varone=0
vartwo=0
variniciar=0
##def condicionMensaje():
##    print("yo entre a la funcion")
##    if(onevar.get()==True):
##         
##        varone=1
##    if(twovar.get()==True):
##            
##        vartwo=1
##    if(onevar.get()==False):
##            
##        varone=0
##    if(twovar.get()==False):
##            
##        vartwo=0
##    if(iniciarVar.get()==True):
##        variniciar=1
##    if(iniciarVar.get()==False):
##        variniciar=0

def bandaAct():
    
    if(iniciarVar.get()==False):        

        iniciarVar.set(True)

        if(onevar.get()==True):     
        
         
            varone=1
        if(twovar.get()==True):
            
            vartwo=1
        if(onevar.get()==False):
            
            varone=0
        if(twovar.get()==False):
            
            vartwo=0
        if(iniciarVar.get()==True):
            
            variniciar=1
        if(iniciarVar.get()==False):
            variniciar=0

        print("__________________Estado de las variables_________________")
   
    #print(onevar.get(),s.get(),twovar.get(),s2.get(),s3.get())
    
        mensaje = (str(0)+"," + str(varone) + "," + str(s.get()) + "," +
                 str(vartwo) + "," + str(s2.get())+ "," + str(variniciar))

        ##Mando al arduino
        arduino.write(mensaje.encode())        

        print(mensaje)
    
##        print(0,varone,s.get(),vartwo,variniciar)

    #print("______Mensaje Arduino________________________")
              
    #arduino.write(mensaje.encode())
    #print(str(velbanda.get()+400).encode())
    
        Buttonn.configure(text="Parar")
    
    
        
    else:
        
        print("-----Apagado----")
        iniciarVar.set(False)
        Buttonn.configure(text="Iniciar")
        onevar.set(False)
        s.set(0)
        twovar.set(False)
        s2.set(0)
        s3.set(0)
        if(onevar.get()==True):     
        
         
            varone=1
        if(twovar.get()==True):
            
            vartwo=1
        if(onevar.get()==False):
            
            varone=0
        if(twovar.get()==False):
            
            vartwo=0
        if(iniciarVar.get()==True):
            #print("yo entre aqui")
            variniciar=1
        if(iniciarVar.get()==False):
            variniciar=0
        
        
##        condicionMensaje()
        mensaje = (str(0)+"," + str(varone) + "," + str(s.get()) + "," +
                  str(vartwo) + "," + str(s2.get())+ "," + str(variniciar))
        arduino.write(mensaje.encode())
                  
##        print(onevar.get(),s.get(),twovar.get(),s2.get(),s3.get())
        print(mensaje)
        
        
        
        #iniciarVar.set(True)
        
        #banderaIniciar.set(True)
        #iniciarVar.set(False)

##    if(iniciarVar.get()==True and banderaIniciar==True):

        
##    if(iniciarVar.get()==False):
##        arduino.write(str(velbanda.get()+300).encode())
##        print(onevar.get(),s.get(),twovar.get(),s2.get(),s3.get())
##        iniciarVar.set(True)
##    
    
    #if(bandera==False):
        
    #print (str(s.get()),one.get())
    #bandera=True
    #else:
    #print(s.set(0))f
    #bandera=False
        

    


Controls = ttk.Labelframe(miFrame, text='Controls')
Controls.grid(row=0, column=0, ipadx=5, ipady=5, sticky=(N, W))

#####Banda Frame#######
lfBanda = ttk.Labelframe(Controls, text='Banda')
lfBanda.grid(row=0, column=0, padx=10, pady=10, sticky=(N, W))

one = ttk.Checkbutton(lfBanda, text="Activar", variable=onevar, onvalue=True)
one.grid(column=0, row=0, sticky=W)




Labels=ttk.Label(lfBanda, text='Velocidad').grid(row=1 , column=1, sticky=W)
s = ttk.Scale(lfBanda, orient=HORIZONTAL, length=100, from_=0.0, to=99.0,variable=velbanda)
s.grid(row=1, column=0, padx=10, pady=10)

#######Tolva Frame######
lfTolva = ttk.Labelframe(Controls, text='Tolva')
lfTolva.grid(row=2, column=0, padx=10, pady=10,sticky=(N, W))

two = ttk.Checkbutton(lfTolva, text="Activar", variable=twovar, onvalue=True)
two.grid(column=0, row=0, sticky=W)

Labels2=ttk.Label(lfTolva, text='Velocidad').grid(row=1 , column=1, sticky=W)
s2 = ttk.Scale(lfTolva, orient=HORIZONTAL, length=100, from_=0.0, to=100,variable=timetolva)
s2.grid(row=1, column=0, padx=10, pady=10)

Labels3=ttk.Label(lfTolva, text='Velocidad').grid(row=2 , column=1, sticky=W)
s3 = ttk.Scale(lfTolva, orient=HORIZONTAL, length=100, from_=0.0, to=100.0)
s3.grid(row=2, column=0, padx=10, pady=10)

def add_image(tkimg,ID):
    textoComentario.insert (END, '\n')
    textoComentario.image_create(END,image=tkimg)
    textoComentario.insert (END,ID)
    textoComentario.insert (END, '\n')

def Camara_image(tkimg):
    label.config(image=tkimg)
    #label.image_create(END,image=tkimg)
def aumentar():
    classesNum[3]=classesNum[3]+1
    print(classesNum[3])
    labelc4.configure(text = str(classes[3])+": "+str(classesNum[3]))
    
    
    
#-------------------------Camara Frame---------------------------
lfCamara = ttk.Labelframe(miFrame, text='Camara')
lfCamara.grid(row=0, column=1, padx=10, pady=2, rowspan=3,sticky=(N, W))

label = ttk.Label(lfCamara)
label.grid(row=0 , column=0)

#-------------------------Console Frame---------------------------
lfConsola = ttk.Labelframe(miFrame, text='Registros')
lfConsola.grid(row=0, column=2, padx=10, pady=2,rowspan=3,sticky=(N, W))
##
##textoComentario=Text(lfConsola, width=20, height=22)
##textoComentario.grid(row=0, column=0, padx=10, pady=10)
##
##scrollVert=Scrollbar(lfConsola, command=textoComentario.yview)
##scrollVert.grid(row=0, column=1, sticky="nsew")
##
##textoComentario.config(yscrollcommand=scrollVert)

labelc1 = ttk.Label(lfConsola,text = str(classes[0])+": "+str(classesNum[0]))
labelc1.grid(row=0 , column=0,padx=5, pady=5, sticky=(N, W))

labelc2 = ttk.Label(lfConsola,text = str(classes[1])+": "+str(classesNum[1]))
labelc2.grid(row=1 , column=0,padx=5, pady=5, sticky=(N,W))

labelc3 = ttk.Label(lfConsola,text = str(classes[2])+": "+str(classesNum[2]))
labelc3.grid(row=2 , column=0,padx=5, pady=5, sticky=(N, W))

labelc4 = ttk.Label(lfConsola,text = str(classes[3])+": "+str(classesNum[3]))
labelc4.grid(row=3 , column=0,padx=5, pady=5, sticky=(N, W))

labelc5 = ttk.Label(lfConsola,text = str(classes[4])+": "+str(classesNum[4]))
labelc5.grid(row=4 , column=0,padx=5, pady=5, sticky=(N, W))

labelc6 = ttk.Label(lfConsola,text = str(classes[5])+": "+str(classesNum[5]))
labelc6.grid(row=5 , column=0,padx=5, pady=5, sticky=(N, W))

labelc7 = ttk.Label(lfConsola,text = str(classes[6])+": "+str(classesNum[6]))
labelc7.grid(row=6 , column=0,padx=5, pady=5, sticky=(N, W))

labelc8 = ttk.Label(lfConsola,text = str(classes[7])+": "+str(classesNum[7]))
labelc8.grid(row=7 , column=0,padx=5, pady=5, sticky=(N, W))

labelc9 = ttk.Label(lfConsola,text = str(classes[8])+": "+str(classesNum[8]))
labelc9.grid(row=8 , column=0,padx=5, pady=5, sticky=(N, W))

labelc10 = ttk.Label(lfConsola,text = str(classes[9])+": " +str(classesNum[9]))
labelc10.grid(row=9 , column=0,padx=5, pady=5, sticky=(N, W))

labelc11 = ttk.Label(lfConsola,text = str(classes[10])+": " +str(classesNum[10]))
labelc11.grid(row=10 , column=0,padx=5, pady=5, sticky=(N, W))

labelc12 = ttk.Label(lfConsola,text = str(classes[11])+": "+ str(classesNum[11]))
labelc12.grid(row=11 , column=0,padx=5, pady=5, sticky=(N, W))

Buttonn=ttk.Button(miFrame, text = "Iniciar", command=bandaAct)
Buttonn.grid(row=1, column=0, padx=10, pady=2,sticky=(N, S, E, W))

Buttonn2=ttk.Button(miFrame, text = "Parar")
Buttonn2.grid(row=2, column=0, padx=10, pady=10,sticky=(N, S, E, W))


def evaluate(event):
    res.configure(text = "Result: " + str(eval(entry.get())))
    
##w = tk.Tk()
##tk.Label(w, text="Your Expression:").pack()
##entry = tk.Entry(w)
##entry.bind("<Return>", evaluate)
##entry.pack()
##res = tk.Label(w)
##res.pack()
##w.mainloop()
#--------------------------Fin interfaz---------------------------------

confThreshold = 0.25
nmsThreshold = 0.40
inpWidth =160
inpHeight =160

classes = ["resistencia","diodo","capacitor","transistor","led","integrado","rele","potenciometro","trimer","boton","switch","cristal"]

#modelConf = "yolov3.cfg"
#modelWeights = "yolov3.weights"
#modelConf = "elecCards.cfg"
#modelWeights = "elecCards.weights"
modelConf = "yolo.cfg"
modelWeights = "electronics.weights"

winName = "try"

net = cv2.dnn.readNetFromDarknet(modelConf, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


def postprocess(frame, outs):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]
    classIDs = []
    confidences = []
    boxes = []
    cenx = []
    ceny = []

    for out in outs:
        for detection in out:            
            scores = detection [5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > confThreshold:
                centerX = int(detection[0] * frameWidth)
                cenx.append(centerX)
                
                centerY = int(detection[1] * frameHeight)
                ceny.append(centerY)

                width = int(detection[2]* frameWidth)
                height = int(detection[3]*frameHeight )

                left = int(centerX - width/2)
                top = int(centerY - height/2)

                classIDs.append(classID)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

##                cond=centerY>(frameHeight//2-10) and (centerY<(frameHeight//2+10))
##                #print(centerY>(frameHeight//2-10) and (centerY<(frameHeight//2+10)))
##                if(cond):
##                    framees=frame[top:top+height,left:left+width]
##                    try:
##                        framees=cv2.resize(framees,(50,50))
##                        framees = cv2.cvtColor(framees,cv2.COLOR_BGR2RGB)
##                        tkimage3 = ImageTk.PhotoImage(image = PIL.Image.fromarray(framees))
##                        salidaa.append(tkimage3)
##                        #add_image(tkimage3,classes[classID])
##                    except:
##                        pass
                


    #indices = cv2.dnn.NMSBoxes (boxes,confidences, confThreshold, nmsThreshold )
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)

    for i in indices:
        i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
##        centerrx=(width-left)//2
##        centerry=(height-top)//2
##        
##        #leftt.append(left)
##        #topp.append(top)
##        cenx.append(centerrx)
##        ceny.append(centerry)
        
        drawPred(classIDs[i], confidences[i], left, top, left + width, top + height,frame)
    return frame, classIDs,cenx, ceny

        
def drawPred(classId, conf, left, top, right, bottom,frame):
    cv2.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)

    label = '%.2f' % conf

    # Get the label for the class name and its confidence
    if classes:
        assert (classId < len(classes))
        label = '%s:%s' % (classes[classId], label)

    #A fancier display of the label from learnopencv2.com 
    # Display the label at the top of the bounding box
    #labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    #top = max(top, labelSize[1])
    #cv2.rectangle(frame, (left, top - round(1.5 * labelSize[1])), (left + round(1.5 * labelSize[0]), top + baseLine),
                 #(255, 255, 255), cv2.FILLED)
    # cv2.rectangle(frame, (left,top),(right,bottom), (255,255,255), 1 )
    #cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 1)
    cv2.putText(frame, label, (left,top), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

def getOutputsNames(net):
	layerNames = net.getLayerNames()

	return [layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()]

def exit():
	k = cv2.waitKey(1)
	if (k==27):
		return 1
	else:
		return 0

def clasificador(frames):
    salida = []
    
    for i in range(len(frames)):
        blob = cv2.dnn.blobFromImage(frames[i], 1/255, (inpWidth, inpHeight), [0,0,0], 1, crop = False)

        net.setInput(blob)

        outs = net.forward(getOutputsNames(net))
        #print(outs)
        
        

        salida.append(postprocess(frames[i], outs))
        

    return(salida)

def dispensador(pos,clase):
    
    
##    arduino.write(str(clasesDispensador[pos][clase][0]).encode())
##    print(clasesDispensador[pos][clase])
##    print("TODO EL MENSAJE")
    mensaje = (str(clasesDispensador[pos][clase])+"," + str(varone) + "," + str(s.get()) + "," +
                  str(vartwo) + "," + str(s2.get())+ "," + str(variniciar))
    arduino.write(mensaje.encode())
    print("Dispensador")
    print(mensaje)
##    print(mensaje)

    #arduino.write(b'4')
##    time.sleep(2)
    #arduino.close()
    

    
cap = cv2.VideoCapture(1)
salidaa = []

k = 0
frames=[[0],[0]]
salida=[]

bgr1 = np.zeros((288, 320, 3), dtype=np.uint8)
bgr1[:,:,:] = (0, 0, 255)

bgr2 = np.zeros((288, 320, 3), dtype=np.uint8)
bgr2[:,:,:] = (0, 255, 0)

cond1=False
cond2=False

while k == 0:
    t0=time.time()
    
    _, frame = cap.read()
    frame=cv2.resize(frame,(640,480))
    framecp=frame.copy()

    frame1 = framecp[96:384,0:320]
    frame2 = framecp[96:384,320:640]
    frames[0]=frame1
    frames[1]=frame2

    salida=clasificador(frames)
    #print(salida)
    
##    print(salida[0][2],salida[0][3])
    try:
        
        frameHeight1 = salida[0][0].shape[0]
        frameWidth1 = salida[0][0].shape[1]

        frameHeight2 = salida[1][0].shape[0]
        frameWidth2 = salida[1][0].shape[1]

        yder=salida[0][3][0]
        
    ##    print(yder)
        yizq=salida[1][3][0]
        #print(yizq,yder,frameHeight1)
            

        cond1=(yder>(frameHeight1//2-70)) and (yder<(frameHeight1//2+70)and(iniciarVar.get()==True))
    ##   print(frameHeight1//2-10)
        
        cond2=(yizq>(frameHeight2//2-70)) and (yizq<(frameHeight2//2+70)and(iniciarVar.get()==True))
    ##    print(frameHeight2//2-10)
        #print(cond2,yizq,cond1,yder,frameHeight1//2)
                  
        if(cond1):
           dispensador(0,salida[0][1][0])
           print(salida[0][1][0])
           classesNum[salida[0][1][0]]=classesNum[salida[0][1][0]]+1
           
        if(cond2):
           dispensador(1,salida[1][1][0])
           print(salida[1][1][0])
           classesNum[salida[1][1][0]]=classesNum[salida[1][1][0]]+1
    except:
        pass
##    condicionMensaje()
    #mensaje = (str(0)+"," + str(varone) + "," + str(s.get()) + "," +
    #              str(vartwo) + "," + str(s2.get())+ "," + str(variniciar))
##    print(variniciar)
    
    #print(mensaje)
##    
##       
       
    framecp[96:384,0:320]=cv2.addWeighted (salida[0][0],0.7, bgr1,0.2,0)

    framecp[96:384,320:640]=cv2.addWeighted (salida[1][0],0.7, bgr2,0.2,0)


    ancho = 500
    alto = 500
    #framecp=cv2.resize(framecp,(ancho,alto))
    framecp = cv2.cvtColor(framecp,cv2.COLOR_BGR2RGB)
    tkimage2 = ImageTk.PhotoImage(image = PIL.Image.fromarray(framecp))

    #print(left, top, width, height)
    #cv2.imshow("ROI",frame[top:top+height,left:left+width])
    
    #cv2.imshow("clasific",framecp)
    #cv2.imshow(winName, framecp)
    Camara_image(tkimage2)
    
    #time.sleep(2)
   
    t1=time.time()
    #print(t1-t0)
    root.update()

    k = exit()

import cv2 
video=cv2.VideoCapture(0)
#while True:
    #_,frame=video.read()
frame=cv2.imread('car2.png') 
frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(frame, (5, 5), 0)                     #Apply the Gaussian Blur on the Image Enhanced in order to reduce the Noise. 
tresh_img = cv2.adaptiveThreshold(blur_img, 255.0,                             #Apply the adaptive thresholding onto the Gaussian-Blurred image received.
                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                    cv2.THRESH_BINARY_INV, 19, 9)     

tresh_img_clr=cv2.cvtColor(tresh_img,cv2.COLOR_GRAY2BGR)          #crea la versione acolori della threshold per poterci disegnar ei rettangoli colorati
contours, hierarchy =cv2.findContours(tresh_img,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) #cerca sulla thresh i conturs
possible_plates=[]
for cnt in contours:                            #per ogni contur ceckiamo se l'area è > 100 
    approx= cv2.contourArea(cnt)                #e se le proporzioni di he w sono giuste
    if approx>1000:
        x,y,w,h=cv2.boundingRect(cnt)
        if w>3*h and w<5*h: 
            cv2.rectangle(tresh_img_clr, (x,y),(x+w,y+h),(0,255,0),2)       #se lo sono disegnamo i rettangoli sull'immagine
            possible_plates.append(tresh_img[y+5:y+h+1-5,x+w//10:x+w+1-(w//8)])              #e aggiungiamo la porzione di immagine alle possibili targhe
final_plate=0
final_list_of_chars=[]
for i in possible_plates:
    c_count=0
    list_of_chars=[]
    i_clr=cv2.cvtColor(i,cv2.COLOR_GRAY2BGR)                                            #per ogni possibile targa creiamo l'immagine a colori per disegnare i rettangolini
    #cv2.imshow('targa',i)
    #k=cv2.waitKey(0)
    contours, hierarchy =cv2.findContours(i,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #troviamo i rettangoli
    for cnt in contours:
        approx= cv2.contourArea(cnt)
        x,y,w,h=cv2.boundingRect(cnt)
        if h>1.5*w and h<5*w and approx>200:        #controlliamo proporzioni e area per assicurarci siano lettere
            c_count+=1                                                          #ad ogni lettere valida aggiungiamo uno al counter
            cv2.rectangle(i_clr, (x,y),(x+w,y+h),(0,255,0),2)                   #e disegnamo il rettangolo
            list_of_chars.append(i[y:y+h+1,x:x+w+1])  
    #cv2.imshow("chars",i_clr)
    #k=cv2.waitKey(0)
    if c_count>3:   #se sono state trovate più di tre lettere valide può essere la targa vera
        #cv2.imshow("chars",i_clr)
        #k=cv2.waitKey(0)
        if type(final_plate)==int:          #se ancora non è stata strovata una targa finale
            final_plate=i_clr
            final_list_of_chars=list_of_chars
        elif len(final_plate)>len(i):       #se è gia stata trovata controlliamo se quella precedente è più grande
            final_plate=i_clr               #in quel caso era probabilmente un 'rettangolo' che contine la targa che 
            final_list_of_chars=list_of_chars             #stiam considerando ora, quindi la sostituiamo
                                            #perchèè ci conviene lavorare sullo slice più accurato
cv2.imshow("FINAL PLATE",final_plate)
k=cv2.waitKey(0)
for char in final_list_of_chars:
    image = cv2.copyMakeBorder(char, 6, 6,14, 14, cv2.BORDER_CONSTANT,0) #aggiungp dei bordi neri per rendere lìimmagine simile  quella del dataset                                                                       #utilizzato per riconoscere i caratteri
    image=cv2.resize(image,(28,28))
    cv2.imshow('chars',image)
    k=cv2.waitKey(0)
#cv2.imshow("video",tresh_img_clr)
#k=cv2.waitKey(0)
#if k== ord("k"):
#    break
#i love martina 
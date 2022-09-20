import cv2 
video=cv2.VideoCapture(0)
#while True:
    #_,frame=video.read()
frame=cv2.imread('img\car9.png') 
frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(frame, (5, 5), 0)                     #Apply the Gaussian Blur on the Image Enhanced in order to reduce the Noise. 
tresh_img = cv2.adaptiveThreshold(blur_img, 255.0,                             #Apply the adaptive thresholding onto the Gaussian-Blurred image received.
                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                    cv2.THRESH_BINARY_INV, 19, 9)     

tresh_img_clr=cv2.cvtColor(tresh_img,cv2.COLOR_GRAY2BGR)          #crea la versione acolori della threshold per poterci disegnar ei rettangoli colorati
contours, hierarchy =cv2.findContours(tresh_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #cerca sulla thresh i conturs
possible_plates=[]
for cnt in contours:                            #per ogni contur ceckiamo se l'area è > 100 
    approx= cv2.contourArea(cnt)                #e se le proporzioni di he w sono giuste
    if approx>1000:
        x,y,w,h=cv2.boundingRect(cnt)
        if w>3*h and w<5*h: 
            cv2.rectangle(tresh_img_clr, (x,y),(x+w,y+h),(0,255,0),2)       #se lo sono disegnamo i rettangoli sull'immagine
            possible_plates.append(tresh_img[y:y+h+1,x:x+w+1])              #e aggiungiamo la porzione di immagine alle possibili targhe
for i in possible_plates:
    i_clr=cv2.cvtColor(i,cv2.COLOR_GRAY2BGR)                                            #per ogni possibile targa creiamo l'immagine a colori per disegnare i rettangolini
    cv2.imshow('targa',i)
    k=cv2.waitKey(0)
    contours, hierarchy =cv2.findContours(i,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #troviamo i rettangoli
    for cnt in contours:
        approx= cv2.contourArea(cnt)
        x,y,w,h=cv2.boundingRect(cnt)
        if h>1.5*w and h<5*w:                                                           #controliamo le proporzioni per assicurarci siano lettere
         cv2.rectangle(i_clr, (x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("chars",i_clr)
    k=cv2.waitKey(0)     

cv2.imshow("video",tresh_img_clr)
k=cv2.waitKey(0)
#if k== ord("k"):
#    break
#i love martina
# not as much as i love u
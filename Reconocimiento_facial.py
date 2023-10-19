# Programa simple para la deteccion de rostros en tiempo real
# Importación biblioteca 
import cv2

# Cargar el clasificador de cascada de Haar para detección de rostros
face_classifier = cv2.CascadeClassifier('C:/Users/Edwin/Desktop/haarcascade_frontalface_default.xml')

# Se inicializa la camara, el indice 0 se refiere al
# uso de la camara web incorporada en la mayoria de latops
captura = cv2.VideoCapture(0)

# Configuración de títulos y estilo de fuente
titulo = "Captura Facial"
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
font_scale = 1
font_color = (0, 0, 0)


# Bucle principal para la detección y visualización en tiempo real
while True:
    # En cada iteración del bucle, se captura un
    # cuadro de la cámara web y se almacena en la variable "img"
    ret, img = captura.read() 

    # Convertir la imagen capturada a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
        
    # El título "Captura Facial" se dibuja en la imagen en la posición (10, 25)
    # con el estilo de fuente y color especificados 
    cv2.putText(img, titulo, (10, 25), font, font_scale, font_color, 2)

    cv2.imshow('Ventana', img) 
    
    # El programa verifica si se ha presionado la tecla "Esc"
    # (código 27 en OpenCV) y, si es así, sale del bucle y cierra la ventana.
    pulso = cv2.waitKey(30)
    if pulso == 27:
        break
    
# Esta línea libera los recursos de la camara web, garantizando
# que la cámara se apague correctamente y que los recursos asociados se liberen    
captura.release() 
# Esta línea cierra todas las ventanas que se hayan creado utilizando OpenCV
cv2.destroyAllWindows()

    
    
    

# Programa simple para la deteccion de autos en videos
# Importación bibliotecas 
import cv2

# Cargar el clasificador de cascada de Haar para detección de autos
face_classifier = cv2.CascadeClassifier('C:/Users/Edwin/Desktop/cars.xml')

# Esta línea de código permite cargar un archivo de video y lo convierte en una fuente de entrada de video para el programa
captura = cv2.VideoCapture('C:/Users/Edwin/Desktop/Autos.mp4')

# Configuración de títulos y estilo de fuente
titulo = "Captura Car"
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
font_scale = 1
font_color = (0, 0, 0)

# Funcion creada para la deteccion de autos en un video 
while True:
    # Esta línea captura un cuadro del video y lo almacena en la variable "img" 
    ret, img = captura.read() 

    # Convierte la imagen a escala de grises para facilitar la detección
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
        
    # El título "Captura Car" se dibuja en la imagen en la posición (10, 25)
    # con el estilo de fuente y color especificados
    cv2.putText(img, titulo, (10, 25), font, font_scale, font_color, 2)

    cv2.imshow('Ventana', img) 
    
    # El programa verifica si se ha presionado la tecla "Esc"
    # (código 27 en OpenCV) y, si es así, sale del bucle y cierra la ventana.
    pulso = cv2.waitKey(30)
    if pulso == 27:
        break
    
# Esta línea libera los recursos de la captura de video 
captura.release() 
# Esta línea cierra todas las ventanas que se hayan creado utilizando OpenCV
cv2.destroyAllWindows()

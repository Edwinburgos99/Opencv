# Opencv

## Programa detección de rostros en tiempo real(cara frontal)

### Requisitos previos

Este es un programa simple para la detección de rostros en tiempo real utilizando OpenCV y el clasificador de cascada de Haar, para la ejecución respectiva del programa en tu PC necesitarás tener instalado el programa Python (recomendación la versión más actual de Python), en caso de no tenerlo en este enlace podrá descargar el Python más actual [Descargar_Python](https://www.python.org/).

Si tu instalacion de python no incluye la biblioteca Opencv, puedes instalarla en tu terminal con la siguiente linea de codigo `pip install opencv-python`. Una vez ya hayas instalado Python y Opencv en tu ordenador, asegurate de tener todos los archivos de la carpeta 'Opencv' en tu pc.

### Ejecucion del programa

Para ejecutar este programa lo primero que haras sera abrir tu entorno de Python, seleccionar y abrir el programa 'Reconocimiento_facial.py' en tu entorno. A continuacion localiza la linea de codigo

`face_classifier = cv2.CascadeClassifier('RUTA/DE/TU/ARCHIVO/haarcascade_frontalface_default.xml')`

Reemplaza 'RUTA/DE/TU/ARCHIVO/haarcascade_frontalface_default.xml' con la ubicación real del archivo 'haarcascade_frontalface_default.xml' en tu PC, por ultimo ejecuta el programa y funcionará sin problemas.

## Programa detección de ojos en tiempo real

### Requisitos previos

Este es un programa simple para la detección de ojos en tiempo real utilizando OpenCV y el clasificador de cascada de Haar, para la ejecución respectiva del programa en tu PC necesitarás tener instalado el programa Python (recomendación la versión más actual de Python), en caso de no tenerlo en este enlace podrá descargar el Python más actual [Descargar_Python](https://www.python.org/).

Si tu instalacion de python no incluye la biblioteca Opencv, puedes instalarla en tu terminal con la siguiente linea de codigo `pip install opencv-python`. Una vez ya hayas instalado Python y Opencv en tu ordenador, asegurate de tener todos los archivos de la carpeta 'Opencv' en tu pc.

### Ejecucion del programa

Para ejecutar este programa lo primero que haras sera abrir tu entorno de Python, seleccionar y abrir el programa 'Reconocimiento_ojos.py' en tu entorno. A continuacion localiza la linea de codigo

`face_classifier = cv2.CascadeClassifier('RUTA/DE/TU/ARCHIVO/haarcascade_eye.xml')`

Reemplaza 'RUTA/DE/TU/ARCHIVO/haarcascade_eye.xml' con la ubicación real del archivo 'haarcascade_eye.xml' en tu PC, por ultimo ejecuta el programa y funcionará sin problemas.

### Programa deteccion de objetos(autos) en video

Este programa es una aplicación simple que utiliza la biblioteca OpenCV y el clasificador de cascada de Haar, para detectar autos en un video, para la ejecución respectiva del programa en tu PC necesitarás tener instalado el programa Python (recomendación la versión más actual de Python), en caso de no tenerlo en este enlace podrá descargar el Python más actual [Descargar_Python](https://www.python.org/).

Si tu instalacion de python no incluye la biblioteca Opencv, puedes instalarla en tu terminal con la siguiente linea de codigo `pip install opencv-python`. Una vez ya hayas instalado Python y Opencv en tu ordenador, asegurate de tener todos los archivos de la carpeta 'Opencv' en tu pc.

### Ejecucion del programa

Para ejecutar este programa lo primero que haras sera abrir tu entorno de Python, seleccionar y abrir el programa 'Reconocimiento_autos.py' en tu entorno. A continuacion localiza la linea de codigo

`face_classifier = cv2.CascadeClassifier('RUTA/DE/TU/ARCHIVO/cars.xml')`

Reemplaza 'RUTA/DE/TU/ARCHIVO/cars.xml' con la ubicación real del archivo 'cars.xml' en tu PC, prosiguiendo deberas localizar la linea

`captura = cv2.VideoCapture('RUTA/DE/TU/ARCHIVO/Autos.mp4')`

La cual se encarga de cargar el archivo de video y lo convierte en una fuente de entrada de video para el programa, Reemplaza 'RUTA/DE/TU/ARCHIVO/Autos.mp4' con la ubicación real del archivo 'Autos.mp4' en tu PC.

# Opencv

## Programa detección de rostros en tiempo real(cara frontal)

### Requisitos previos

Este es un programa simple para la detección de rostros en tiempo real utilizando OpenCV y el clasificador de cascada de Haar, Para la ejecución respectiva del programa en tu PC necesitarás tener instalado el programa Python (recomendación la versión más actual de Python), en caso de no tenerlo en este enlace podrá descargar el Python más actual [Descargar_Python](https://www.python.org/).

Si tu instalacion de python no incluye la biblioteca Opencv, puedes instalarla en tu terminal con la siguiente linea de codigo `pip install opencv-python`. Una vez ya hayas instalado Python y Opencv en tu ordenador, asegurate de tener todos los archivos de la carpeta 'Opencv' en tu pc.

### Ejecucion del programa

Para ejecutar este programa lo primero que haras sera abrir tu entorno de Python, seleccionar y abrir el programa 'Reconocimiento_facial.py' en tu entorno. A continuacion localiza la linea de codigo 'face_classifier = cv2.CascadeClassifier('RUTA/DE/TU/ARCHIVO/haarcascade_frontalface_default.xml'), Reemplaza 'RUTA/DE/TU/ARCHIVO/haarcascade_frontalface_default.xml' con la ubicación real del archivo 'haarcascade_frontalface_default.xml' en tu PC, por ultimo ejecuta el programa y funcionará sin problemas.

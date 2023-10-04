import cv2
import numpy as np

import sys

print(sys.argv)
#Si no se recibe por parametro el nombre, se asume que es input.jpg
if len(sys.argv) == 2:
    nombre = sys.argv[1]
else:
    nombre = 'input.jpg'

#Cargar la imagen de entrada
input_image = cv2.imread(nombre)

#Definir los kernels
kernel1 = np.array([-1, 3, -1])
kernel2 = np.array([1/3, 1/3, 1/3])
kernel3 = np.array([-1, 0, -1])
#Calcular la convolucion de los kernels
kernel1_2= np.convolve(kernel1,kernel2)
print(kernel1_2)
kernel2_3= np.convolve(kernel2,kernel3)
print(kernel2_3)
#Aplicar kernel1_2
image_kernel1_2=cv2.filter2D(src=input_image,ddepth=-1, kernel=kernel1_2)
#Aplicar kernel2_3
image_kernel2_3=cv2.filter2D(src=input_image,ddepth=-1, kernel=kernel2_3)

#Guardar las imágenes resultantes
cv2.imwrite('image_kernel1_2.jpg', image_kernel1_2)
cv2.imwrite('image_kernel2_3.jpg', image_kernel2_3)
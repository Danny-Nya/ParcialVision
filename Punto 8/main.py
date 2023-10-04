import cv2
import numpy as np

import sys

#Codigo basado en el Ejercicio 2
#Repositorio personal: https://github.com/Danny-Nya/Taller2-VisionArtificial

print(sys.argv)
# Si no se recibe por parametro el nombre, se asume que es input.jpg
if len(sys.argv) == 2:
    nombre = sys.argv[1]
else:
    nombre = 'input.jpg'

#Cargar la imagen de entrada
input_image = cv2.imread(nombre)

#Definir las matrices
#Matriz traslacion
translation_matrix = np.float32([[1, 0], [0, 1], [-21, 15]])
#Angulo de Rotacion
rotation_angle = 60
#Factores de escala en x y
scaleX_factor = 5/7
scaleY_factor= 7/8
#Calcular la matriz compuesta
#Calcular la matriz compuesta de transformación
#Rotacion con Traslacion
combined_matrix = np.matmul(np.float32([[np.cos(np.radians(rotation_angle)), -np.sin(np.radians(rotation_angle)), 0],
                                       [np.sin(np.radians(rotation_angle)), np.cos(np.radians(rotation_angle)), 0]]),
                            translation_matrix)
#Cambinada anterior y Escala
combined_matrix = np.matmul(combined_matrix, np.float32([[scaleX_factor, 0, 0], [0,scaleY_factor, 0]]))
print(combined_matrix)
#Aplicar la matriz de transformación combinada a la imagen
transformed_image_combined = cv2.warpAffine(input_image, combined_matrix, (input_image.shape[1], input_image.shape[0]))
#Guardar las imágenes resultantes
cv2.imwrite('transformed_image_combined.jpg', transformed_image_combined)
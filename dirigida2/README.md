# DIRIGIDA 2

## Preguntas Teóricas

### ¿Qué diferencias observas en el historial del repositorio después de restaurar un commit mediante `reflog`?

El historial visible con `git log` no muestra el commit restaurado directamente.  
Sin embargo, `reflog` permite acceder a referencias pasadas, recuperando commits perdidos.

### ¿Cuáles son las ventajas y desventajas de utilizar submódulos en comparación con subtrees?

- **Submódulos:**  
  Mantienen los repositorios independientes, pero requieren gestión manual al actualizar.

- **Subtrees:**  
  Integran repositorios completos, simplificando la sincronización, pero dificultando la separación.

### ¿Cómo impacta la creación y gestión de hooks en el flujo de trabajo y la calidad del código?

Los hooks automatizan tareas como pruebas y formateo, mejorando la calidad del código.  
Pero si son mal gestionados, pueden introducir inconsistencias si no se comparten o documentan correctamente.

### ¿De qué manera el uso de `git bisect` puede acelerar la localización de un error introducido recientemente?

`git bisect` automatiza la búsqueda binaria entre commits buenos y malos para hallar el error.  
Ahorra tiempo al evitar pruebas manuales en todos los commits del historial.

### ¿Qué desafíos podrías enfrentar al administrar ramas y stashes en un proyecto con múltiples colaboradores?

Puede haber conflictos si varios trabajan sobre ramas similares o cambian stashes frecuentemente.  
La coordinación y políticas claras son clave para evitar sobrescrituras y pérdidas de trabajo.

---

## Evidencias Prácticas

### Configuramos el entorno utilizando el editor Nano
![Imagen 1](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/dirigida2/img/imagen1.png.jpg)

### Utilizamos el contenido editado en Nano para renombrar una rama.
![Imagen 2](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/dirigida2/img/imagen2.png.jpg)

### Verificamos la nueva rama renombrada
![Imagen 3](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/dirigida2/img/imagen3.jpg)

### Estamos en la nueva rama
![Imagen 4](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/dirigida2/img/imagen4.jpg)

### Renombramos una rama 
![Imagen 5](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/dirigida2/img/imagen5.jpg)

### Mostramos los cambios  
![Imagen 6](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/dirigida2/img/imagen6.jpg)

### Gestión de git diff 
![Imagen 7](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/dirigida2/img/imagen7.jpg)

### Instalación de hook correctamente: 
![Imagen 8](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/dirigida2/img/imagen8.jpg)

### Probamos el hooks permitiendo commits sin comentarios 
![Imagen 9](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/dirigida2/img/imagen9.jpg)

### Probamos el hooks permitiendo commits con comentarios 
![Imagen 10](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/dirigida2/img/imagen10.jpg)

### Merge automatizado de una rama exitoso 
![Imagen 11](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/dirigida2/img/imagen11.jpg)

### Generando reporte de estado del repositorio 
![Imagen 12](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/dirigida2/img/imagen12.jpg)

### Inspeccionamos el archivo que generamos  
![Imagen 12](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/dirigida2/img/imagen13.jpg)
![Imagen 13](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/dirigida2/img/imagen14.jpg)

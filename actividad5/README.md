# Actividad 5 - Trabajo con ramas en Git

## Primera parte

Creamos un directorio e inicializamos en el repositorio.  
![Imagen 1](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen1.jpg)

Creamos 2 ramas y 

![Imagen 2](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen2.jpg)

hacemos cambios en cada una de las 2 ramas y guardamos en commit

![Imagen 3](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen3.jpg)

Nos cambiamos al main y fusionamos las ramas.  

![Imagen 4](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen4.jpg)

Vemos el historial:  

![Imagen 5](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen5.jpg)

Creamos nueva rama1 y txt y guardamos el commit.  

![Imagen 6](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen6.jpg)

Creamos nueva rama2 y txt y guardamos el commit.  

![Imagen 7](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen7.jpg)

Fusionamos la rama 1 y forzamos la creación del commit.

![Imagen 8](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen8.jpg)

Mostramos el historial de commits:  

![Imagen 9](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen9.jpg)

---

### Pregunta

**¿Cuáles son las principales ventajas de utilizar `git merge --no-ff` en un proyecto en equipo? ¿Qué problemas podrían surgir al depender excesivamente de commits de fusión?**

**Ventajas:**
- Mantiene el historial claro.
- Sabes qué cambios provinieron de qué rama.
- Facilita el rollback.

**Desventajas:**
- El historial se llena de muchos commits de merge.
- Puede volverse difícil de leer si el equipo no lo organiza.

**Problemas de depender excesivamente de commits de fusión:**
- Puede causar varios problemas en el desarrollo de software, incluyendo dificultades de seguimiento y legibilidad.

---

## Segunda parte

Creamos nuevo directorio e inicializamos.  

![Imagen 10](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen10.jpg)


Creamos un archivo `index.html` y hacemos un commit.  
![Imagen 11](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen11.jpg)

Creamos una nueva rama y agregamos contenido al archivo, luego realizamos un commit.  
![Imagen 12](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen12.jpg)

Cambiamos de rama y agregamos un footer al `index.html`, luego hacemos un commit.  
![Imagen 13](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen13.jpg)

Fusionamos y notamos el conflicto.  
![Imagen 14](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen14.jpg)

Solucionamos el conflicto.  
![Imagen 15](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen15.jpg)

Subimos y realizamos un commit.  
![Imagen 16](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen16.jpg)

Verificamos el historial.  
![Imagen 17](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen17.jpg)

---

### Preguntas

**¿Qué pasos adicionales tuviste que tomar para resolver el conflicto?**

Para resolver el conflicto, primero Git detectó un problema al hacer `git merge --no-ff`. Abrí el archivo con conflicto (`index.html`), eliminé las marcas (`<<<<<<<`, `=======`, `>>>>>>>`), combiné los cambios manualmente, guardé el archivo, lo agregué con `git add` y completé la fusión con `git commit`.

**¿Qué estrategias podrías emplear para evitar conflictos en futuros desarrollos colaborativos?**

- Comunicarse bien con el equipo.
- Dividir las tareas claramente.
- Hacer `git pull` seguido.
- Trabajar en ramas separadas.
- Hacer commits pequeños.
- Usar revisiones de código antes de fusionar.

---

## Ejercicio adicional

Creamos un directorio e inicializamos.  
![Imagen 18](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen18.jpg)

Creamos un archivo `file.txt` que diga "línea 1" y hacemos un commit. Luego le agregamos "línea 2" y hacemos otro commit.  
![Imagen 19](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen19.jpg)
Creamos otra rama y hacemos un commit.  
![Imagen 20](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen20.jpg)

Volvemos al main y hacemos cambio.  
![Imagen 21](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen21.jpg)

Fusionamos (automerge) en main.  
![Imagen 22](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen22.jpg)

Vemos el historial de commits.  
![Imagen 23](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen23.jpg)
---

### Preguntas

**¿Cuándo usarías un comando como `git revert` para deshacer una fusión?**

Usaria `git revert` para deshacer una fusión cuando ya hiciste push o querés mantener el historial intacto, ya que crea un nuevo commit que revierte los cambios sin borrar nada.

**¿Qué tan útil es la función de fusión automática en Git?**

La fusión automática en Git es muy útil porque ahorra tiempo al combinar ramas sin conflictos. Sin embargo, si hay cambios en las mismas líneas, requiere intervención manual.

---

## Última parte

Creamos nueva rama para hacer cambios y realizamos commit.  
![Imagen 23](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen23.jpg)

Subimos (pusheamos) al repositorio.  
![Imagen 24](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen24.jpg)

---

### Preguntas

**¿Cómo cambia la estrategia de fusión cuando colaboras con otras personas en un repositorio remoto?**

La estrategia se enfoca en usar Pull Requests (PRs) para revisar y aprobar cambios antes de fusionarlos, lo cual permite detectar conflictos y evitar errores. Además, es común realizar `git pull` frecuentemente para mantenerse actualizado.

**¿Qué problemas comunes pueden surgir al integrar ramas remotas?**

- Conflictos de fusión cuando dos personas modifican las mismas líneas.
- Commits desordenados o incorrectos.
- Falta de comunicación entre colaboradores que lleva a cambios inconsistentes o incompatibles.

---

Creamos proyecto con 3 ramas.  
![Imagen 25](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen25.jpg)

Entramos en cada rama.  
![Imagen 26](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen26.jpg)
Realizamos cambios en la rama 1.  
![Imagen 27](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen27.jpg)

Realizamos cambios en la rama 1: 
![Imagen 28](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen28.jpg)

Ahora para la rama 2.  
![Imagen 29](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen29.jpg)

Cambiamos a la rama main y fusionamos.  
![Imagen 30](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen30.jpg)

Creamos un archivo `txt` que diga "cambio en feature3", lo agregamos, hacemos un commit, luego otro commit adicional.  
![Imagen 31](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen31.jpg)

Cambiamos nuevamente a la rama principal, fusionamos `feature3` con `main` y revisamos el historial de commits.  
![Imagen 32](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad5/img/Imagen32.jpg)

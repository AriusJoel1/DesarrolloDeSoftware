## ACTIVIDAD 9;

Implementamos la funcion test para que verifica si un usuario puede ser agregado correctamente al sistema. Esta prueba inicialmente fallaráw. 

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad9/img/8.png)

 la prueba fallará porque aún no hemos implementado la clase UserManager.

Creamos la clase UserManager en la carpeta src y volvemos a ejecutar pytest y vemos que la prueba pasa

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad9/img/2.png)

Modificamos el archivo user_manager.py para agregarle la clase con sus respectivas funciones (hash y verify). Despues ejecutamos la prueba pytest y pasa como vemos en la imagen

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad9/img/3.png)


Creamos las funcionalidades de shopping cart y sus funcionalidades de agregar producto, calcular total y vaciar carrrito

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad9/img/7.png)


Agregamos la funcion no se puede agregar usuario existente con el objetivo de no agregar un usuario existente 

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad9/img/4.png)


agregamos el email_service que simula que envía correos cuando agregamos a un usuario. Tambien implementamos la funcion de testeo para verificar que el servicio se llama corretamente durante el proceso

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad9/img/5.png)

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad9/img/6.png)



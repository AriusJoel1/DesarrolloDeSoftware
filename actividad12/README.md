## ACTIVIDAD 12;

Instalamos las librerias necesarias para el proyecto

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad12/img/Imagen1.png)

Creamos las tablas 

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad12/img/Imagen2.png)

Cargamos los datos del archivo account_data.json

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad12/img/Imagen3.png)

Dentro de la clase de pruebas TestAccountModel, utilizamos el método setup_class para cargar los datos de prueba antes de que se ejecuten las pruebas

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad12/img/Imagen4.png)


Ejecutamos ppytest para asegurarnos del caso de prueba se ejecuta sin errores

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad12/img/Imagen5.png)


Agregamos la función TestAccountModel parra probar la creación de exactamente una sola cuenta

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad12/img/Imagen6.png)

Testeamos y la prueba pasa 

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad12/img/Imagen7.png)


Creamos el metodo test_create_all_accounts para el caso de prueba de crear todas las cuentas

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad12/img/Imagen8.png)

Y testeamos

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad12/img/Imagen9.png)

Agregamos los métodos setup_method y teardown_method para eliminar los datos de la tabla antes de cada prueba y para eliminar la sesión después de cada prueba 

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad12/img/Imagen10.png)


Finalmente testeamos 

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad12/img/Imagen11.png)







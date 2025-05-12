## ACTIVIDAD 11;

Instalamos pytest y pytest-cov para ejecutar las pruebas y generar informes 

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad11/img/1.png)

Ejecutamos pruebas y pasan

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad11/img/2.png)

Modificamos la función test_is_empty

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad11/img/3.png)

Y agregamos la función test_pop 

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad11/img/4.png)



Ejecutamos pytest para verificar que el método is_empty() pasa

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad11/img/5.png)

Ahora modificamos la función test_peek en test_stack.py para la prueba unitaria del método peek no cambie el estado de la pila 

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad11/img/6.png)


Modificamos la función test_peek y testeamos

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad11/img/7.png)


Modificamos la función test_pop para eliminar y devolver el valor en la parte superior de la pila

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad11/img/8.png)


Modificamos la función test_pop y testeamos

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad11/img/9.png)

Modificamos la función test_push() en test_stack.py para que verifique que el método agregue elementos correctamente a la pila y que siempre queden en la cima.

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad11/img/10.png)


Modificamos la función test_push y testeamos

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad11/img/11.png)

Generamos un informe de cobertura utilizando pytest-cov

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad11/img/12.png)


Finalmente creamos el archivo setup.cfg para personalizar la ejecución de las pruebas y cómo se recopila el informe de cobertura de código.

![](https://github.com/AriusJoel1/DesarrolloDeSoftware/blob/main/actividad11/img/13.png)







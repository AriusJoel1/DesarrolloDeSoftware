# Motivaciones y Fundamentos de la Computación en la Nube

---

## Motivaciones para la Nube

### (a) ¿Qué problemas o limitaciones existían antes del surgimiento de la computación en la nube y cómo los solucionó la centralización de servidores en data centers?

Antes de la nube, las empresas debían mantener su propia infraestructura física, lo que implicaba altos costos de mantenimiento, problemas de escalabilidad, disponibilidad limitada y complejidad en la administración. La centralización en data centers permitió consolidar recursos, mejorar la eficiencia energética, facilitar el mantenimiento y garantizar alta disponibilidad mediante redundancia y gestión centralizada.

### (b) ¿Por qué se habla de “The Power Wall” y cómo influyó la aparición de procesadores multi-core en la evolución hacia la nube?

“The Power Wall” hace referencia al límite físico al que llegaron los procesadores mononúcleo en términos de consumo energético y generación de calor, impidiendo seguir aumentando su velocidad. Para superar esta barrera, se adoptaron arquitecturas multi-core, lo que permitió distribuir las tareas entre varios núcleos, facilitando la paralelización y el procesamiento en clústeres, una base clave para la computación en la nube.

---

## Clusters y Load Balancing

### (a) Explica cómo la necesidad de atender grandes volúmenes de tráfico en sitios web condujo a la adopción de clústeres y balanceadores de carga.

El aumento del tráfico en aplicaciones web exigía una infraestructura que pudiera manejar múltiples peticiones simultáneas sin degradar el rendimiento. Los clústeres de servidores permiten distribuir la carga de trabajo, mientras que los balanceadores de carga se encargan de direccionar las solicitudes entrantes al servidor más adecuado, optimizando tiempos de respuesta y asegurando la continuidad del servicio.

### (b) Describe un ejemplo práctico de cómo un desarrollador de software puede beneficiarse del uso de load balancers para una aplicación web.

Un desarrollador que despliega una aplicación web con múltiples instancias en contenedores (por ejemplo, usando Docker y Kubernetes) puede utilizar un balanceador de carga para dirigir automáticamente las solicitudes al contenedor menos cargado. Esto garantiza mejor rendimiento, reduce tiempos de espera para los usuarios y permite realizar actualizaciones sin tiempo de inactividad.

---

## Elastic Computing

### (a) Define con tus propias palabras el concepto de Elastic Computing.

Elastic Computing es la capacidad de escalar automáticamente los recursos de computación (como CPU, memoria o almacenamiento) según la demanda de la aplicación, lo que permite optimizar el uso de recursos y costos.

### (b) ¿Por qué la virtualización es una pieza clave para la elasticidad en la nube?

La virtualización permite ejecutar múltiples máquinas virtuales sobre un mismo hardware físico, lo que facilita la asignación dinámica de recursos. Esto permite que los entornos crezcan o se reduzcan sin necesidad de comprar o configurar nuevo hardware físico.

### (c) Menciona un escenario donde, desde la perspectiva de desarrollo, sería muy difícil escalar la infraestructura sin un entorno elástico.

Durante el lanzamiento de una nueva funcionalidad en una app móvil popular, el tráfico puede dispararse en cuestión de minutos. Sin elasticidad, el equipo de desarrollo tendría que predecir esa carga y provisionar hardware por adelantado, con riesgo de sobrecarga o desperdicio de recursos. Con elastic computing, el sistema escala automáticamente según la demanda.

---

## Modelos de Servicio (IaaS, PaaS, SaaS, DaaS)

### (a) Diferencia cada uno de estos modelos. ¿En qué casos un desarrollador optaría por PaaS en lugar de IaaS?

- **IaaS (Infrastructure as a Service):** Proporciona recursos como máquinas virtuales, almacenamiento y redes. El usuario gestiona el sistema operativo y las aplicaciones.
- **PaaS (Platform as a Service):** Ofrece una plataforma lista para usar donde el desarrollador solo se enfoca en el código y la lógica, sin preocuparse por el sistema operativo o el hardware.
- **SaaS (Software as a Service):** Aplicaciones listas para usar a través de internet (ej. Gmail, Google Drive).
- **DaaS (Desktop as a Service):** Proporciona escritorios virtuales accesibles desde cualquier dispositivo.

Un desarrollador optaría por **PaaS** cuando desea enfocarse exclusivamente en el desarrollo y despliegue de su aplicación sin encargarse de la infraestructura subyacente (como base de datos, red, sistema operativo).

### (b) Enumera tres ejemplos concretos de proveedores o herramientas que correspondan a cada tipo de servicio.

- **IaaS:** Amazon EC2, Google Compute Engine, Microsoft Azure Virtual Machines  
- **PaaS:** Heroku, Google App Engine, Azure App Service  
- **SaaS:** Dropbox, Salesforce, Trello  
- **DaaS:** Amazon WorkSpaces, Citrix Virtual Apps and Desktops, Windows 365

---

## Tipos de Nubes (Pública, Privada, Híbrida, Multi-Cloud)

### (a) ¿Cuáles son las ventajas de implementar una nube privada para una organización grande?

Una nube privada brinda mayor control sobre los datos, más seguridad, cumplimiento de normativas específicas y personalización total del entorno. Es ideal para organizaciones con requisitos estrictos en privacidad, como instituciones financieras o gubernamentales.

### (b) ¿Por qué una empresa podría verse afectada por el “provider lock-in”?

El “provider lock-in” ocurre cuando una empresa depende excesivamente de un único proveedor de nube, lo que dificulta cambiar a otro por costos altos, incompatibilidades técnicas o pérdida de datos. Esto limita la flexibilidad y la capacidad de negociación.

### (c) ¿Qué rol juegan los “hyperscalers” en el ecosistema de la nube?

Los “hyperscalers” (como AWS, Azure y Google Cloud) son grandes proveedores de infraestructura que ofrecen escalabilidad masiva, disponibilidad global y servicios avanzados en la nube. Son la columna vertebral del ecosistema cloud, permitiendo que tanto startups como corporaciones accedan a tecnologías de alto nivel sin una inversión inicial enorme.

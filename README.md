1. Desde VirtualBox lanzamos la maquina virtual de Odoo para obtener las direcciones necesarias.

2. Accedemos a la consola desde la direccion dada por la maquina virtual (Web Shell). Una vez dentro,
podremos acceder a Odoo con los siguientes comandos:

    - cd /opt/odoo
    - ./odoo.py

Si es la primera vez que se hace, la plataforma pedira que se cree una base de datos y se escoja el 
idioma

3. Otra vez desde la consola se instalara un modulo de prueba que se descargara y modificara desde 
NetBeans. Para instalarlo se lanzara el siguiente comando:

./odoo.py scaffold openacademy addons (ESTANDO SITUADOS EN /opt/odoo)

Este comando creara la estructura principal.

4. Desde NetBeans creamos un nuevo proyecto php desde servidor remoto, y configuramos el proyecto
con los datos de nuestra conexion y rutas concretas de donde esta situado nuestro modulo.

5. Una vez configurado el nuevo proyecto, descargamos el archivo openacademy situado en addons,
que es el modulo creado con el comando scaffold.

6. No se necesitan todos los archivos que se muestran. Los archivo controllers.py y models.py los 
quitamos de sus carpetas, y las borramos. Tambien borraremos el archivo __init__.pyc.

7. Seguiremos el tutorial de modulo oficial de Odoo,situado en la URL: 
https://www.odoo.com/documentation/9.0/howtos/backend.html

8.Desde el archivo openacademy.xml se crea el menu Courses, para poder crear y modificarlos. Se debe
añadir el archivo al apartado data del openerp.py.

9. Se añade un Search_View desde el openacademy.xml para poder buscar los cursos.

10. Se crea un nuevo menu Sesion desde models.py y se crea su form en el respectivo xml.

11. Se comienza con el uso de campos relacionales entre los dos menus anteriormente creados(Cursos y 
Sessions). Añadiendo los llamados one2many y many2one en models.py y en openacademy.xml

12. Creamos los archivos partner(xml y py). El xml se añade en el openerp y el py se importa en el init.
Estos archivos nos permitiran trabajar con herencias.


Databases

: nombre de las tablas simpre en singular

: si durante el uso de la aplicación soloa hacemos uso de datos d econtacto en una o ninguna interacción con el ususario se recomienda una relación uno a uno con la tabla usuario(id, nombre, correo, password) y una tabla contacto (usuario_id, telefono, dirección, SS) 

: nombre de las columnbas se refieres como "campo" y a las filas completas se conoceran como "registro" y sus poarte individuales se denominara "dato".

:: El unico dato que no puede ser NULL y que siempre es necesario es el "id" como PRIMARY KEY

:: Las FOREIGN KEY el el dato que usaremos para referir información en otra tabla.

:: El comando DROP en mysql permitira borrar tablas y bases de datos creadas

:: El comando ALTEr permitira modificar la estructura de las tablas existentes::


CREATE

CREATE DATABASE prueba;

ALTER TABLE Usuario ADD edad INT; 		 # agregar columna edad a tabla existente #

ALTER TABLE Usuario DROP COLUMN edad;   		 # borrar columna "edad" agregada #

ALTER TABLE Usuario MODIFY COLUMN email VARCHAR (50);		 # modificar el tipo de dato de una columna ya creada #

INSERT INTO Usuario (email, username)
VALUES ('joan@call.com', 'Joan');

DELETE FROM Usuario WHERE email = 'joan@call.com' LIMIT 1;  		# eliminar dato ingresado en registro anterior

ALTER TABLE Usuario ADD PRIMARY KEY (id); 		# agregar id como llave primario y auto incremental por defecto al PRIMARY KEY

ALTER TABLE Usuario MODIFY COLUMN id INT AUTO_INCREMENT;		# alterar columna id como dato entero(INT) y auto incremental (AUTO_INCREMENT)

SELECT * FROM Usuario;  		# seleccionar todo de la tabla Uduario

SELECT * FROM Usuario WHERE edad < 31; 			# crear solicitudes con condiciones de tipo lógico

UPDATE Usuario SET edad = 32 WHERE id = '1';

DELETE FROM Usuario WHERE id = '1';  	# eliminar al usuario que tenga el id_usuario '1'




### venv  :package:

1. create virtual environment env

~~~sh
python3 -m venv env
~~~

2. run virtual environment

~~~sh
source env/bin/activate
~~~

3. install Flask dependences

~~~sh
pip3 install Flask
~~~

4. check the virtual environment connection origin

~~~sh
> which pip3

result:
/usr/bin/pip3
PS /home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv> 
~~~



UPDATE mysql.user SET authentication_string=PASSWORD('root'), plugin='mysql_native_password' WHERE user='root' AND host='localhost';

ALTER TABLE user MODIFY COLUMN plugin 'mysql_native_password' WHERE user='root' AND host='localhost';

INSERT INTO user(email, username)
VALUES ('joan@call.com', 'Joan');   




/// Instalación y configuración de base de dados en linux ///

Guía de instalación:

INSTALACIÓN DE APACHE

sudo apt-get update
sudo apt-get install apache2
sudo systemctl start apache2

INSTALAR MYSQL

sudo apt update
sudo apt-cache search mysql-server
sudo apt install mysql-server-8.0

CREAR USUARIO (ROOT) Y CONTRASEÑA

sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'newPassword';
exit

CONFIGURACIÓN

sudo systemctl start mysql.service
sudo mysql_secure_installation
sudo systemctl is-enabled mysql.service

INSTALACIÓN DE PHPMYADMIN

sudo apt update
sudo apt-get install -y php php-tcpdf php-cgi php-pear php-mbstring libapache2-mod-php php-common php-phpseclib php-mysql
sudo apt install phpmyadmin php-mbstring php-zip php-gd php-json php-curl
sudo phpenmod mbstring
sudo systemctl restart apache2



_________________ method _________________________


~~~sh

❯ curl -X POST http://localhost:5000/post/1
El methodo solicitado no es == GET%                                                          

❯ curl -X GET http://localhost:5000/post/1
:: Successful :: El id del metodo POST es: 1%   

~~~
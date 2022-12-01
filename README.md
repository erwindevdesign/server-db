# MySQL & Python

### INSTALL MYSQL-APACHE-PHP

INSTALL APACHE

sudo apt-get update
sudo apt-get install apache2
sudo systemctl start apache2

INSTALL MYSQL

sudo apt update
sudo apt-cache search mysql-server
sudo apt install mysql-server-8.0

CREAD USER (ROOT) AND PASSWORD

sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'newPassword';
exit

CONFIG

sudo systemctl start mysql.service
sudo mysql_secure_installation
sudo systemctl is-enabled mysql.service

INSTALL PHPMYADMIN

sudo apt update
sudo apt-get install -y php php-tcpdf php-cgi php-pear php-mbstring libapache2-mod-php php-common php-phpseclib php-mysql
sudo apt install phpmyadmin php-mbstring php-zip php-gd php-json php-curl
sudo phpenmod mbstring
sudo systemctl restart apache2

### Create database 

1. create database

~~~MySQL
mysql> CREATE DATABASE prueba;
Query OK, 1 row affected (0.42 sec)
~~~

2. select database

~~~MySQL
mysql> USE prueba;
Database changed
~~~

3. create table

~~~MySQL
CREATE TABLE usuario(
    id INT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    birth_day INT NOT NULL
    );
~~~

4. show table

~~~MySQL
mysql> show tables;
+------------------+
| Tables_in_prueba |
+------------------+
| usuario          |
+------------------+
1 row in set (0.04 sec)

~~~

 5. describe content table

 ~~~MySQL

mysql> desc usuario;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| id        | int          | NO   | PRI | NULL    |       |
| full_name | varchar(255) | NO   |     | NULL    |       |
| email     | varchar(255) | NO   | UNI | NULL    |       |
| birth_day | date         | NO   |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
4 rows in set (0.18 sec)
 ~~~

 6. insert data

 ~~~MySQL

INSERT INTO usuario(id, full_name, email, birth_day) VALUES ('1', 'Thalia Hernandez', 'thali_sun@gmail.com', 23);
INSERT INTO usuario(id, full_name, email, birth_day) VALUES ('2', 'Felipe Calderon y Nojosa', 'chupito_partyn@yahoo.com', 48);


 ~~~


 6.1 ALTER TABLE

 ~~~
ALTER TABLE usuario MODIFY COLUMN birth_day INT;

ALTER TABLE usuario MODIFY COLUMN id AUTO_INCREMENT;
 
 
INSERT INTO user (email, username)
VALUES ('joan@call.com', 'Joan'); 
 
 ~~~
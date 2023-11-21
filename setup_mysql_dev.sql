-- sql script that creates a db hbnb
-- creates a user hbnb_dev
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

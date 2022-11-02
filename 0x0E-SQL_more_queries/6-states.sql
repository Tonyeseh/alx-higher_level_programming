-- creates a hbtn_0d_usa database
-- and creates a table states
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `states`
(`id` INT NOT NULL UNIQUE AUTO_INCREMENT,
`name` VARCHAR(256) NOT NULL, PRIMARY KEY(`id`));

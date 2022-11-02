-- creates user user_0d_1
-- the user should have all privileges on your server
-- scripts does not fail if user already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

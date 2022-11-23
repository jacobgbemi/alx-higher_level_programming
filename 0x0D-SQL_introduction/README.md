# 0x0D. SQL - Introduction


## Database Installation and Commands on UBUNTU 20.4
### Installatiom
- Install MySQL Server
  - $ ```sudo apt install mysql-server```
### Setup and Commands
1. Set password for the first time
	- $ ```mysqladmin -u root password NEWPASSWORD```
2. Change existing Password
	- $ ```sudo mysql ALTER USER 'root'@'localhost' IDENTIFIED BY 'PASSWORD';```
	- $ ```sudo systemctl stop mysql```
	- $ ```sudo mysqld -init-file=~/mysql-pwd```
	- $ ```sudo systemctl start mysql```
3. Import dumb table into a database
	- $ ```mysql -u root -p 'database_name' < 'filename.sql'```
4. Download file online
	- $ ```wget 'https://web_address.com'/filename```
5. Enter mysql prompt
	- $ ```mysql -u root -p```
6. Create New MySQL User
	- mysql> ```CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';```
7. Create New MySQL User with mysql_native_password
	- mysql> ```CREATE USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';```
8. Alter MySQL User with mysql_native_password
	- mysql> ```ALTER USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';```
9. Granting a User Permissions
	- mysql> ```GRANT PRIVILEGE ON database.table TO 'username'@'host';```
	- mysql> ```GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;```
10. Granting All privileges to a User
	- mysql> ```GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;```
11. Reload grant table to effect new privileges
	- mysql> ```FLUSH PRIVILEGES;```
12. Revoke a permission
	- mysql> ```REVOKE type_of_permission ON database_name.table_name FROM 'username'@'host';```
13. Review a User permissions
	- mysql> ```SHOW GRANTS FOR 'username'@'host';```
14. Delete a User
	- mysql> ```DROP USER 'username'@'localhost';```
15. Exit MySQL clint
	- mysql> ```exit```
16. New User log in
	- $ ``` mysql -u username -p```

| Usage | Command |
| ---- | -------- |
| Usage Example | $ ```cat 0-list_databases.sql \| mysql -uroot -p``` |
  
## Resources
- [What is Database & SQL?](https://alx-intranet.hbtn.io/rltoken/yyRKTEdRkYEVlRgZPbasjw)
- [A Basic MySQL Tutorial](https://alx-intranet.hbtn.io/rltoken/sV2PtK5YfQsXWW1malRZ5Q)
- [Basic SQL statements: DDL and DML](https://alx-intranet.hbtn.io/rltoken/IUKo4-UaRZSKPvXr5u9oBw)
- [Basic queries: SQL and RA](https://alx-intranet.hbtn.io/rltoken/rXKvu2u7vg1Hj6bnX7UgMg)
- [SQL technique: functions](https://alx-intranet.hbtn.io/rltoken/-Riv_dzSYsJyvy-LlaO6Mg)
- [SQL technique: subqueries](https://alx-intranet.hbtn.io/rltoken/QpIXoR--8eBIaidgSWYsBQ)
- [What makes the big difference between a backtick and an apostrophe?](https://alx-intranet.hbtn.io/rltoken/Gt0nFJPJRwW2Y0izzwbVrw)
- [MySQL Cheat Sheet](https://alx-intranet.hbtn.io/rltoken/wLQZvDtRCG9eQ69c8jvYVA)
- [MySQL 8.0 SQL Statement Syntax](https://alx-intranet.hbtn.io/rltoken/HmdmLiYBM0Q34iCYPWd9XQ)

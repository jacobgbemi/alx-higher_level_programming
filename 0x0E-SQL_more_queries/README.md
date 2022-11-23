# 0x0E. SQL - More queries
Further exercises on SQL quesries and key concept
![SQL-JOIN](https://github.com/jacobgbemi/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/sql_join.png)

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
- [How To Create a New User and Grant Permissions in MySQL](https://alx-intranet.hbtn.io/rltoken/RniBKj48bnIN8xpXhGl1yA)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://alx-intranet.hbtn.io/rltoken/FIiEIvA6IN_hSKM5TvgyxQ)
- [MySQL constraints](https://alx-intranet.hbtn.io/rltoken/LrovGa6N-OE2ID_tpWZRaQ)
- [SQL technique: subqueries](https://alx-intranet.hbtn.io/rltoken/kR71h5zjkPtx4kBoVf7q0g)
- [Basic query operation: the join](https://alx-intranet.hbtn.io/rltoken/rNMJeQ1jbNTCljbvCSjf6w)
- [SQL technique: multiple joins and the distinct keyword](https://alx-intranet.hbtn.io/rltoken/HhZ6TJ1q5S0aR4lhfpKdOQ)
- [SQL technique: join types](https://alx-intranet.hbtn.io/rltoken/T6FZUQdsMzr8hgNInBzudA)
- [SQL technique: union and minus](https://alx-intranet.hbtn.io/rltoken/Nd-sdM8QUpf0YKIlXzVv4w)
- [MySQL Cheat Sheet](https://alx-intranet.hbtn.io/rltoken/xP00kJWWi0SzvK-Lt8YdLQ)
- [The Seven Types of SQL Joins](https://alx-intranet.hbtn.io/rltoken/-plhBsra0N7BOuFoEg--zg)
- [MySQL Tutorial](https://alx-intranet.hbtn.io/rltoken/I4Lws_eQrIrNTbkZvvk-oQ)
- [SQL Style Guide](https://alx-intranet.hbtn.io/rltoken/051eAEP_rePBU7jeh879GA)
- [MySQL 8.0 SQL Statement Syntax](https://alx-intranet.hbtn.io/rltoken/YavbYiraYFr8oTukT_N6eQ)
- [Design](https://alx-intranet.hbtn.io/rltoken/EWLRPeqr5sQ9AqfoG_KXxw)
- [Normalization](https://alx-intranet.hbtn.io/rltoken/mqBhYoSYbhH5ZZrhDcY0kA)
- [ER Modeling](https://alx-intranet.hbtn.io/rltoken/R0exkJmf-2ddKjGfa8D0dA)

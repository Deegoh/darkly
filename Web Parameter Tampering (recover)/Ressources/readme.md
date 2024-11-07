# Vulnerability

The vulnerability allow you to steal data and do other attack like SQL Injection

# Identification

- Network Monitoring (FireFox)
- Manual testing

# Resolve

Go to http://10.11.249.210/index.php?page=recover
Inspect code and you will find a hidden input.
Change the value and submit

# Prevent

Implement strict input validation on both the client and server sides

# Resources

https://owasp.org/www-community/attacks/Web_Parameter_Tampering

# Vulnerability

Security misconfiguration is a common and potentially serious vulnerability that occurs when settings are improperly configured or left at insecure default values.

# Identification

Go to http://10.11.249.210/robots.txt<br>
we have 2 routes disallow. I checked '/whatever' and I got an file htpassword

# Resolve

I download the htpasword file and decode it.<br>
It's a md5 with 32 char.<br>
root:437394baff5aa33daa618be47b75cb49<br>
root:qwerty123@

# Prevent

- Employ the principle of least privilege
- Use secure default configurations

# Resources

https://md5decrypt.net/en/<br>
https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/03-Review_Webserver_Metafiles_for_Information_Leakage
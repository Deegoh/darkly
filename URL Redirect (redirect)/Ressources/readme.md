# Vulnerability

The vulnerabilities occur when an application accepts untrusted input containing a URL value and uses it to redirect users without proper validation.

# Identification

When we click on the url, we can see the rediction and the value is send to the url.\
https://www.legitimate-site.com/redirect?url=https://malicious-site.com

# Resolve

Go to http://10.11.249.210/index.php?page=redirect&site=https://malicious-site.com

# Prevent

- Validate and sanitize all user inputs used in redirection URLs
- Implement a whitelist of allowed redirect destinations
- Use absolute URLs for redirects instead of relative ones
- Validate the Host header and other headers that might influence redirects
- Use indirect references to internal pages instead of full URLs in redirects

# Resources

https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/11-Client_Side_Testing/04-Testing_for_Client_Side_URL_Redirect

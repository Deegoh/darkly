# Vulnerability

This vulnerability occurs when an attacker can inject CR and LF characters into the headers of the application response, effectively splitting it into two different HTTP messages.

# Identification

When we click on the url, we can see the rediction and the value is send to the url.
https://www.legitimate-site.com/redirect?url=https://malicious-site.com

# Resolve

Go to {URL}/index.php?page=redirect&site=https://malicious-site.com

# Prevent

- Validate and sanitize all user inputs used in redirection URLs
- Implement a whitelist of allowed redirect destinations
- Use absolute URLs for redirects instead of relative ones
- Avoid using user-supplied data in Location headers
- Implement proper output encoding to prevent response splitting
- Validate the Host header and other headers that might influence redirects
- Use indirect references to internal pages instead of full URLs in redirects

# Resources
https://owasp.org/www-community/attacks/HTTP_Response_Splitting
https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/15-Testing_for_HTTP_Splitting_Smuggling
# Vulnerability

Directory Traversal is a web security vulnerability that enables an attacker to access files on the server that are not intended to be accessible.

# Identification

Identify the part of the URL, we get page.\
The page parameter allows us to explore the file

# Resolve

http://10.11.249.210/?page=../../../../../../../etc/passwd

# Prevent

- Input Validation: Thoroughly validate and sanitize user input.
- Use of Safe APIs: Employ filesystem APIs that only allow access to specific directories.
- Canonicalize Paths: Normalize file paths before use.
- Principle of Least Privilege: Run applications with minimal necessary permissions.

# Resources

https://portswigger.net/web-security/file-path-traversal

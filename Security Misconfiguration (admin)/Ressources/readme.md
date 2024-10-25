# Vulnerability

Security misconfiguration is a common and potentially serious vulnerability that occurs when security settings are improperly configured or left at insecure default values.

# Identification

Go to ${URL}/robots.txt
we have 2 routes disallow. I checked '/whatever' and I got an file htpassword

# Resolve

I download the htpasword file and decode it.
It's a md5 with 32 char.
root:437394baff5aa33daa618be47b75cb49
root:qwerty123@

# Prevent

- Employ the principle of least privilege
- Use secure default configurations

# Resources

https://md5decrypt.net/en/

# Vulnerability

Session hijacking occurs when an attacker gains unauthorized access to a user's session by obtaining or guessing the session identifier, typically stored in a cookie.

# Identification

Inspect any pages with browser tool.<br>
Go to the Application tab.<br>
Check session storage

# Resolve

On Cookies tab, we'll get a cookie with the name I_am_admin<br>
The value is 'false' on md5 encoded '68934a3e9455fa72420237eb05902327'<br>
Now, we'll encode the value 'true' on md5 'b326b5062b2f0e69046810717534cb09'<br>
Replace the value with the new on and refresh the page.

# Prevent

- Use HTTPS for all communications involving sensitive data.
- Implement proper cookie attributes (Secure, HttpOnly, SameSite).
- Avoid including sensitive information directly in cookies.
- Regularly rotate session identifiers to limit the window of opportunity for attackers.

# Resources

https://owasp.org/www-community/attacks/Session_hijacking_attack<br>
https://www.dcode.fr/hash-md5

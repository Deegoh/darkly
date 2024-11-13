# Vulnerability

A brute force attack is an attempt to discover a password by systematically trying combinations of letters, numbers, and symbols to pass through authentication.

# Identification

When we tried, we didn't have any delay and rate limite.

# Resolve

```
python3 -m venv bruteforce
source bruteforce/bin/activate
pip install requests
```

run `brute.py`<br>
Let him cook

# Prevent

- Account Lockout: Lock accounts after a defined number of incorrect password attempts
- Progressive Delays: Increase the time between login attempts after each failure
- Require Complex Passwords: Enforce strong password policies to make guessing more difficult
- Multi-Factor Authentication: Implement additional authentication factors beyond just passwords
- CAPTCHA: Use CAPTCHA after failed login attempts to prevent automated attacks

# Resources

https://owasp.org/www-community/attacks/Brute_force_attack<br>
https://owasp.org/www-community/attacks/Password_Spraying_Attack<br>
https://www.f5.com/glossary/brute-force-attack

# Darkly
This project provides an excellent opportunity to gain hands-on experience with web application security.

## Installation
To set up and explore the Darkly project for web application security, follow these steps:
  
1. Download the Darkly_i386.iso file provided for the project.
2. Install QEMU if not already present:

   ```zsh
   brew install qemu
   ```
3. Create a virtual disk for the VM:
   ```zsh
   qemu-img create -f qcow2 darkly.qcow2 20G
   ```
4. Launch the VM using QEMU:
   ```zsh
   sudo qemu-system-x86_64 -hda darkly.qcow2 -cdrom Darkly_i386.iso -m 2G -nic vmnet-bridged,ifname=en0
   ```
Note: Sudo is used here due to network privilege restrictions on our system.

## Exploring the Vulnerable Website
Once the VM is running:

1. Access the website through the VM's web browser.
2. Analyze the website structure, focusing on:
   - URL parameters
   - Form inputs
   - Cookie values
   - HTTP headers
3. Look for common web vulnerabilities such as:
   - SQL injection
   - Cross-site scripting (XSS)
   - Insecure direct object references (IDOR)
   - Broken authentication
   - Sensitive data exposure
4. Use browser developer tools to inspect network requests, JavaScript code, and DOM elements.
5. Try manipulating input fields and URL parameters to uncover potential security flaws.
6. Document your findings and the methods used to discover vulnerabilities.

## Common Vulnerabilities to Look For

Focus on identifying and understanding these common web application vulnerabilities:

1. Cross-Site Scripting (XSS)

   - Test input fields and URL parameters for script injection.
   - Look for unsanitized user input reflected in the page.


2. SQL Injection

   - Attempt to manipulate database queries through user inputs.
   - Look for error messages that reveal database information.


3. Cross-Site Request Forgery (CSRF)

   - Check if the application uses anti-CSRF tokens.
   - Attempt to perform actions without proper authentication.


4. Insecure Direct Object References (IDOR)

   - Try accessing resources by manipulating identifiers in URLs or parameters.


5. Authentication Flaws

   - Test for weak password policies.
   - Look for vulnerabilities in login mechanisms, such as password reset functions.


6. Session Management Issues

   - Analyze how sessions are handled and if they're properly secured.


7. Security Misconfigurations

   - Check for information disclosure in error messages.
   - Look for unnecessary features or pages that shouldn't be accessible.


## Documenting Findings

For each vulnerability discovered:

1. Describe the vulnerability and its potential impact.
2. Explain how you identified it.
3. Provide steps to reproduce the issue.
4. Suggest possible fixes or mitigations.

## Reflection and Learning

After completing the analysis:

1. Reflect on the most common or severe vulnerabilities you found.
2. Consider how these issues could have been prevented during development.
3. Think about how you would approach building a more secure version of this application.

By systematically examining the vulnerable website and documenting your findings, you'll gain valuable insights into web application security and develop a mindset for identifying and mitigating security risks in future projects.
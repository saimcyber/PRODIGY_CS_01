# PRODIGY_CS_01
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Caesar Cipher Project</title>
</head>
<body>
    <h1>Caesar Cipher Project</h1>

<h2>Overview</h2>
    <p>This project implements the Caesar Cipher, a classic encryption method that shifts the letters in the plaintext by a fixed number of positions down the alphabet. This README provides a comprehensive guide on how to use the project, including instructions for running the code and understanding its functionality.</p>

<h2>Features</h2>
    <ul>
        <li><strong>Encryption</strong>: Convert plaintext into ciphertext using a specified key.</li>
        <li><strong>Decryption</strong>: Convert ciphertext back into plaintext using the same key.</li>
    </ul>

<h2>Getting Started</h2>
    <p>To get started with this project, you'll need to clone the repository and run the code. Follow the instructions below for setup and usage.</p>

<h3>Prerequisites</h3>
    <p>Ensure you have Python 3.x installed on your machine. You can download it from <a href="https://www.python.org/downloads/" target="_blank">python.org</a>.</p>

<h3>Cloning the Repository</h3>
    <pre><code>git clone https://github.com/saimcyber/PRODIGY_CS_01.git
cd caesar-cipher</code></pre>

<h3>Running the Code</h3>
    <p>You can run the code by executing the <code>caesarcipher.py</code> script. Here’s how to use the provided functions:</p>

<h4>Encrypting Plaintext</h4>
    <p>To encrypt plaintext, call the <code>encrypt</code> function. You'll need to provide the plaintext and an integer key (the number of positions to shift).</p>
    <pre><code>from cipher import encrypt

plaintext = input("Enter plaintext: ")
key = int(input("Enter encryption key: "))
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)</code></pre>

<h4>Decrypting Ciphertext</h4>
    <p>To decrypt ciphertext, call the <code>decrypt</code> function. You'll need to provide the ciphertext and the same integer key used for encryption.</p>
    <pre><code>from cipher import decrypt

ciphertext = input("Enter ciphertext: ")
key = int(input("Enter decryption key: "))
plaintext = decrypt(ciphertext, key)
print("Plaintext:", plaintext)</code></pre>

<h3>Code Structure</h3>
    <ul>
        <li><code>cipher.py</code>: Contains the implementation of the Caesar Cipher functions.
            <ul>
                <li><code>encrypt(plaintext, key)</code>: Encrypts the given plaintext with the specified key.</li>
                <li><code>decrypt(ciphertext, key)</code>: Decrypts the given ciphertext with the specified key.</li>
            </ul>
        </li>
    </ul>

<h3>Example Usage</h3>
    <p>Here is a complete example of how to use the Caesar Cipher functions:</p>
    <pre><code># Import the cipher module
from cipher import encrypt, decrypt

# Encrypt a message
plaintext = "hello"
key = 3
ciphertext = encrypt(plaintext, key)
print("Encrypted:", ciphertext)  # Output: khoor

# Decrypt the message
decrypted_message = decrypt(ciphertext, key)
print("Decrypted:", decrypted_message)  # Output: hello</code></pre>

<h3>Contributing</h3>
    <p>If you'd like to contribute to this project, please follow these steps:</p>
    <ol>
<li>Fork the repository.</li>
        <li>Create a new branch (<code>git checkout -b feature-branch</code>).</li>
        <li>Make your changes and commit them (<code>git commit -am 'Add new feature'</code>).</li>
        <li>Push to the branch (<code>git push origin feature-branch</code>).</li>
        <li>Create a new Pull Request.</li>
    </ol>

<hr>
    <p>Thank you for checking out the Caesar Cipher Project. Enjoy encrypting and decrypting your messages!</p>
</body>
</html>

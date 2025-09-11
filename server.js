const express = require('express');
const { spawn } = require('child_process');
const app = express();
const port = 3000;
const path = require('path');

app.use(express.static('public'));
app.use(express.json());

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/generate-password', (req, res) => {
    const { length, special, numbers, uppercase } = req.body;
    
    const pythonProcess = spawn('python3', ['password_generator.py', length, special, numbers, uppercase]);
    
    pythonProcess.stdout.on('data', (data) => {
        res.json({ password: data.toString().trim() });
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Error: ${data}`);
        res.status(500).send("Error generating password");
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});

// Frontend - public/index.html
const fs = require('fs');
const frontendHTML = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Generator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container mt-5">
    <h1 class="mb-4">Password Generator</h1>
    <form id="passwordForm">
        <div class="mb-3">
            <label for="length" class="form-label">Password Length:</label>
            <input type="number" id="length" class="form-control" value="12" min="4" max="50">
        </div>
        <div class="form-check">
            <input type="checkbox" id="special" class="form-check-input">
            <label for="special" class="form-check-label">Include Special Characters</label>
        </div>
        <div class="form-check">
            <input type="checkbox" id="numbers" class="form-check-input">
            <label for="numbers" class="form-check-label">Include Numbers</label>
        </div>
        <div class="form-check">
            <input type="checkbox" id="uppercase" class="form-check-input">
            <label for="uppercase" class="form-check-label">Include Uppercase Letters</label>
        </div>
        <button type="submit" class="btn btn-primary mt-3">Generate Password</button>
    </form>
    <h3 class="mt-4">Generated Password:</h3>
    <p id="passwordOutput" class="fw-bold"></p>
    <script>
        document.getElementById('passwordForm').addEventListener('submit', async function(event) {
            event.preventDefault();
            const length = document.getElementById('length').value;
            const special = document.getElementById('special').checked;
            const numbers = document.getElementById('numbers').checked;
            const uppercase = document.getElementById('uppercase').checked;

            const response = await fetch('/generate-password', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ length, special, numbers, uppercase })
            });
            
            const data = await response.json();
            document.getElementById('passwordOutput').textContent = data.password;
        });
    </script>
</body>
</html>`;
fs.mkdirSync('public', { recursive: true });
fs.writeFileSync('public/index.html', frontendHTML);

// Python Script - password_generator.py
const pythonScript = `
import sys
import random
import string

def generate_password(length, special, numbers, uppercase):
    characters = string.ascii_lowercase
    if special == 'true':
        characters += string.punctuation
    if numbers == 'true':
        characters += string.digits
    if uppercase == 'true':
        characters += string.ascii_uppercase
    
    return ''.join(random.choice(characters) for _ in range(int(length)))

if __name__ == "__main__":
    length = sys.argv[1]
    special = sys.argv[2]
    numbers = sys.argv[3]
    uppercase = sys.argv[4]
    print(generate_password(length, special, numbers, uppercase))
`;
fs.writeFileSync('password_generator.py', pythonScript);


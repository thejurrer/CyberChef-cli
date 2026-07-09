# CyberChef CLI
CyberChef CLI is a command-line interface tool based on the CyberChef web app. It allows for convenient and rapid data transformation and encoding/decoding operations straight from your terminal.

## Installation
```bash
git clone https://github.com/Julestblt/CyberChef-cli.git
cd CyberChef-cli
pip install -r requirements.txt
```

## Usage
```bash
python3 src/main.py [COMMAND] [-d --decode or --encode] [VALUE]
```

## Available Commands:
```
b64: Base64 operations
b32: Base32 operations
hex: Hexadecimal operations
url: URL operations
bin: Binary operations
r13: Rot13 operations
MD5: MD5 operations
charcode: Charcode operations
identify: Identifies md5, sha256, hex, b64, b32
Each command supports various methods, which can be selected by -d (decode), -e (encode), -H (hash) or -i (identify).
```

If no command or method is selected, the program will interactively ask for them. If no value is provided for the operation, the program will ask for it interactively as well.

## Examples:
Base64 encoding:
```bash
python3 src/main.py b64 -e "Hello, World!"
```
URL decoding:
```bash
python3 src/main.py url -d "Hello%2C%20World%21"
```
Rot13 decoding:
```bash
python3 src/main.py r13 -d "Uryyb, Jbeyq!"
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT

Note: This README assumes that your Python environment is set up correctly, you're using a Unix-like system, and that you're familiar with command-line operations.
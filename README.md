# PythOS 6.1

A lightweight, Python-based operating system designed for educational and experimental purposes. PythOS provides a Unix-like command-line interface with a focus on simplicity and extensibility.

## Features

- **Command-Line Interface**: Intuitive shell interface with command execution capabilities
- **User Management**: Basic user system with username management
- **File System**: Simple and clean file system operations and management
- **Package Support**: Built-in support for essential Python packages
- **Custom Commands**: Extensible command system for adding new functionality

## Getting Started

## Caution!!
  If you plan to run PythOS by source code, we recommend you to run in root, since the code was made specifically for Alpine minimal filesystem.
  Read instructions below 👇 

### Prerequisites (Only for users who want to run from source code)

- Python 3.11 or newer
- Required Python packages:
  - climage
  - hex
  - pyfiglet

### Installation

1. Clone the repository:
```bash
git clone https://github.com/milo1004/PythOS.git
cd PythOS
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the OS:
```bash
./activate.sh
```

## Project Structure
PythOS6.1/
│
├── main.py
│
├── PythOS/
│   ├── central.py
│   ├── currentdir.txt
│   ├── packages.txt
│   │
│   ├── bin/
│   │   ├── arguments.txt
│   │   ├── arguments2.txt
│   │   ├── command.txt
│   │   │
│   │   ├── apt/
│   │   │   └── apt.py
│   │   │
│   │   ├── bash/
│   │   │   └── bash.py
│   │   │
│   │   ├── cat/
│   │   │   └── cat.py
│   │   │
│   │   ├── cd/
│   │   │   └── cd.py
│   │   │
│   │   ├── clear/
│   │   │   └── clear.py
│   │   │
│   │   ├── cls/
│   │   │   └── cls.py
│   │   │
│   │   ├── date/
│   │   │   └── date.py
│   │   │
│   │   ├── help/
│   │   │   └── help.py
│   │   │
│   │   ├── install/
│   │   │   └── install.py
│   │   │
│   │   ├── ls/
│   │   │   └── ls.py
│   │   │
│   │   ├── ping/
│   │   │   └── ping.py
│   │   │
│   │   ├── pwd/
│   │   │   └── pwd.py
│   │   │
│   │   ├── pyver/
│   │   │   ├── MIT License.txt
│   │   │   ├── pyver.py
│   │   │   └── version.txt
│   │   │
│   │   ├── reboot/
│   │   │   ├── arguments.txt
│   │   │   ├── argumentsexplained.txt
│   │   │   ├── reboot_now.py
│   │   │   ├── reboot_refresh.py
│   │   │   └── reboot.py
│   │   │
│   │   └── time/
│   │       └── time.py
│   │
│   ├── boot/
│   │   ├── boot.py
│   │   ├── currentdir.txt
│   │   ├── install.py
│   │   ├── logon.py
│   │   ├── PythOS.png
│   │   ├── PythOSLogo.txt
│   │   ├── setup.py
│   │   ├── show_info.py
│   │   ├── Terms and Services.txt
│   │   └── timeusedtf.txt
│   │
│   ├── shs/
│   │   ├── boot.sh
│   │   ├── boot2.sh
│   │   ├── boot3.sh
│   │   ├── boot4.sh
│   │   ├── entercentral.sh
│   │   ├── logon.sh
│   │   └── rebootrefresh.sh
│   │
│   └── userdata/
│       ├── passwd.txt
│       └── username.txt



## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- **Milo** - [GitHub Profile](https:/github.com/milo1004)
- **Alex** - [GitHub Profile](https://github.com/alexlam0206)

## Acknowledgments

- Inspired by Unix-like operating systems and shell commanding systems
- Built with Python and shell command files for educational purposes

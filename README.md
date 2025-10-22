# PythOS 6.1

A lightweight, Python-based operating system designed for educational and experimental purposes. PythOS provides a Unix-like command-line interface with a focus on simplicity and extensibility.

## Features

- **Command-Line Interface**: Intuitive shell interface with command execution capabilities
- **User Management**: Basic user system with username management
- **File System**: Simple and clean file system operations and management
- **Package Support**: Built-in support for essential Python packages
- **Custom Commands**: Extensible command system for adding new functionality

## Getting Started
	To get started, you can download the ISO from this website: https://archive.org/details/pyth-os-6.1-x-86-64-beta
	Note: the ISO provided is only supported for x64 bit devices, and Live mode is currently the only boot mode. Persistent mode coming soon~
## Windows: 
1. Download Rufus from rufus.ie or the Microsoft Store
2. Launch Rufus and flash the ISO into a USB (512 MB+)
3. Reboot the PC
4. Enter boot menu (usually by pressing esc, F2, F10, F12 or del)
5. Select to boot from USB
6. Select `PythOS` in the GRUB menu and enjoy! (Rebooting or shuttng down WILL RESET ALL CHANGES MADE ON PYTHOS, does not affect Windows)
Note: The reboot and shutdown commands does not work yet. Long press the power button to shutdown or CTRL-ALT-DEL to reboot.

## Linux:
1. Open terminal and cd to the directory of the ISO

2. Plug in a USB and type `lsblk`

3. Remember the drive you want to flash listed (e.g. `/dev/sda1`)

4. Umount the drive (don't type in sudo if not installed)
			
				sudo umount /dev/sda1

5. Flash the ISO to the drive
			
				sudo dd if=path/to/iso.iso of=/dev/sda1 bs=200M status=progress

6. Reboot the PC

7. Enter boot menu (usually by pressing esc, F2, F10, F12 or del)

8. Select to boot from your USB

9. Select `PythOS` in the GRUB menu and enjoy! (Rebooting or shuttng down WILL RESET ALL CHANGES MADE ON PYTHOS, does not affect Linux)

### Caution!!
  There are some bugs in the cd commad. if change the directory by typing in /[folder] (any directory that starts with a /), it wouldn't recognize. So please first cd to / first, and then cd to the targetted directory.
  
  If you plan to run PythOS by source code, we recommend you to run in root, since the code was made specifically for Alpine minimal filesystem.
  Read instructions below 👇 

### Prerequisites (Only for users who want to run from source code)

- Python 3.10 or newer
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

3. Create a venv (Only need to do once unless you downloaded the source again):
```bash
python3 -m venv venv
```

4. Run the OS:
```bash
source venv/bin/activate
python3 main.py
```

## Project Structure
```
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
|   |   ├── live.txt
|   |   ├── inspmt.txt
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
│   │
│   └── userdata/
│       ├── passwd.txt
│       └── username.txt
```



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

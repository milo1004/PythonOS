# 🐍 PythOS 6.1

A lightweight, Python-based operating system designed for educational and experimental use. PythOS offers a Unix-like command-line interface with a focus on simplicity and extensibility.

---

## 🚀 Features

- Intuitive command-line interface
- Basic user and file system management
- Built-in Python package support
- Easily extensible with custom commands
- Lightweight and fast boot via ISO

---

## 💾 Download

Grab the latest ISO from [Archive.org](https://archive.org/details/pyth-os-6.1-x-86-64-beta).  
**Note**: Only x64 devices are supported. Live mode only (persistent mode coming soon).

---

## 🛠️ Installation

### Windows

1. Download [Rufus](https://rufus.ie) or install it from the Microsoft Store.
2. Flash the ISO to a USB drive (512MB+ recommended).
3. Reboot your PC and enter the boot menu (`Esc`, `F2`, `F10`, `F12`, or `Del`).
4. Select the USB device and boot into **PythOS** via GRUB.

> ⚠️ Changes made in PythOS are not saved after reboot.  
> Use `CTRL+ALT+DEL` to reboot or hold the power button to shut down.  
> The `reboot` and `shutdown` commands are not yet functional.

### Linux

1. Open a terminal and navigate to the ISO directory.
2. Plug in your USB and run `lsblk` to identify the device (e.g., `/dev/sda1`).
3. Unmount the drive:
   ```bash
   sudo umount /dev/sda1


1. Flash the ISO:sudo dd if=pythos.iso of=/dev/sda bs=200M status=progress

2. Reboot and boot from USB via GRUB.


---

⚙️ Run from Source (Advanced)

Recommended for developers or testing in a virtual environment.

Requirements

• Python 3.10+
• Packages: climage, hex, pyfiglet


Setup

git clone https://github.com/milo1004/PythonOS.git
cd PythonOS
pip install -r requirements.txt
python3 -m venv venv
source venv/bin/activate
python3 main.py


---

📁 Project Structure

PythonOS/
├── main.py
├── PythOS/
│   ├── central.py
│   ├── currentdir.txt
│   ├── packages.txt
│   ├── bin/
│   │   ├── [command folders: cd, ls, ping, etc.]
│   ├── boot/
│   ├── userdata/
│   └── assets/


---

🐞 Known Issues

• cd does not support absolute paths starting with /.
Workaround: run cd / first, then navigate.


---

🤝 Contributing

Pull requests are welcome! Fork the repo and submit your improvements.

---

📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

👥 Authors

• @milo1004
• @alexlam0206
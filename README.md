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

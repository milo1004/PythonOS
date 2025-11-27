import os
import subprocess
import curses

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    msg1 = "Proceed to installing on this device? (y/n)"
    msg2 = "(Press 'M' to proceed and install as an MBR disk even if you are using UEFI. Disk MUST be < 2TB if this mode is selected)"
    stdscr.addstr(h//2, w//2 - len(msg1)//2, msg1, curses.A_BOLD)
    stdscr.addstr(h//2 + 2, w//2 - len(msg2)//2, msg2, curses.A_BOLD)
    stdscr.refresh()

    key = stdscr.getch()
    if key in [ord('n'), ord('N')]:
        return
    elif key in [ord('y'), ord('Y'), ord('m'), ord('M')]:
        is_mbr = key in [ord('m'), ord('M')]
        curses.endwin()
        run_installer(is_mbr)


def run_installer(is_mbr=False):
    os.system("clear")
    print("Please DO NOT remove the boot media until you are told to do so.")
    print("Detecting boot media...")

    usb_device = find_live_usb()
    print("Detected Media:", usb_device)

    if not usb_device:
        print("No boot media found. Please insert your PythOS installer and try again.")
        exit(1)

    print("Mounting media...")
    os.makedirs("/mnt/usb", exist_ok=True)
    if os.system(f"mount {usb_device} /mnt/usb") != 0:
        print(f"Failed to mount {usb_device}")
        exit(1)

    print("Extracting archive...")
    os.makedirs("/tmp/archive", exist_ok=True)

    gzip_path = "/mnt/usb/boot/initramfs.cpio.gz"
    cpio_tmp = "/tmp/archive/initramfs.cpio"

    # Extract gzip -> cpio
    with open(cpio_tmp, "wb") as f:
        subprocess.run(["gzip", "-dc", gzip_path], stdout=f, check=True)

    # Extract cpio contents
    with open(cpio_tmp, "rb") as cpio_file:
        subprocess.run(["cpio", "-idmv"], cwd="/tmp/archive", stdin=cpio_file, check=True)

    print("Extraction complete.")

    print("Modifying files...")
    os.system("rm -f /tmp/archive/PythOS/PythOS/boot/live.txt")
    with open("/tmp/archive/PythOS/PythOS/boot/live.txt", "w") as writelive:
        writelive.write("False")

    print("Checking boot mode...")
    result = subprocess.run(
        "[ -d /sys/firmware/efi ] && echo 'UEFI' || echo 'BIOS'",
        shell=True, capture_output=True, text=True
    )
    boot_mode = result.stdout.strip()
    print(f"System Boot Mode: {boot_mode}")

    if is_mbr:
        print("Installing as MBR disk...")
        #custom BL
        os.system("grub-install --target=i386-pc /dev/sda")
    elif boot_mode == "UEFI":
        print("Installing as UEFI system...")
        os.system("grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=PythOS")
    else:
        print("Installing as BIOS system...")
        os.system("grub-install --target=i386-pc /dev/sda")

    print("Installation complete! You can now remove your installer media and reboot.")
    os.system("umount /mnt/usb")


def find_live_usb():
    os.makedirs("/mnt/tmpusb", exist_ok=True)
    os.makedirs("/mnt/tmpcd", exist_ok=True)

    for dev in os.listdir("/dev"):
        if dev.startswith("sd") and dev[-1].isdigit():
            path = f"/dev/{dev}"
            if os.system(f"mount {path} /mnt/tmpusb 2>/dev/null") == 0:
                if os.path.exists("/mnt/tmpusb/boot/initramfs.cpio.gz"):
                    os.system("umount /mnt/tmpusb")
                    os.system("rm -rf /mnt/tmpusb /mnt/tmpcd")
                    return path
                os.system("umount /mnt/tmpusb 2>/dev/null")

    # Try CD-ROM as fallback
    if os.path.exists("/dev/cdrom"):
        if os.system("mount /dev/cdrom /mnt/tmpcd 2>/dev/null") == 0:
            if os.path.exists("/mnt/tmpcd/boot/initramfs.cpio.gz"):
                os.system("umount /mnt/tmpcd")
                os.system("rm -rf /mnt/tmpusb /mnt/tmpcd")
                return "/dev/cdrom"
            os.system("umount /mnt/tmpcd 2>/dev/null")

    os.system("rm -rf /mnt/tmpusb /mnt/tmpcd")
    return None


if __name__ == "__main__":
    curses.wrapper(main)

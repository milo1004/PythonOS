#include <stdio.h>       // for printf()
#include <unistd.h>      // for sync()
#include <sys/reboot.h>  // for reboot() and constants
#define LINUX_REBOOT_CMD_POWER_OFF 0x4321fedc

int main(void) {
    // Step 1: Tell the user what’s happening
    printf("Flushing filesystem buffers...\n");
    sync(); // Flushes filesystem buffers

    // Step 2: Print next action
    printf("Requesting ACPI shutdown from kernel...\n");

    // Step 3: Ask the kernel to power off safely
    if (reboot(LINUX_REBOOT_CMD_POWER_OFF) == -1) {
        perror("Shutdown failed, please use the command \"flush\" and force long press the power button.");
        return 1;
    }

    // If it works, this line shouldn’t even run
    return 0;
}

import subprocess
import tkinter as tk
import subprocess
import os

# Set up the window
window = tk.Tk()
window.title("Virtual Machine Name")
window.geometry("300x100")

# Center the window on the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (300 / 2))
y = int((screen_height / 2) - (100 / 2))
window.geometry(f"400x200+{x}+{y}")

# Label and entry box
label = tk.Label(window, text="Enter the name of the virtual machine:")
label.pack(pady=10)
entry = tk.Entry(window)
entry.pack(pady=5)

# Launch the commands


def launch_commands():
    vm_name = entry.get()
    # Change directory to VirtualBox installation path
    os.chdir(r"C:\\Program Files\\Oracle\\VirtualBox\\")

    # Modify CPUID settings
    os.system(
        f'VBoxManage.exe modifyvm "{vm_name}" --cpuidset 00000001 000106e5 00100800 0098e3fd bfebfbff')

    # Set DMI system information
    os.system(
        f'VBoxManage setextradata "{vm_name}" "VBoxInternal/Devices/efi/0/Config/DmiSystemProduct" "iMac11,3"')
    os.system(
        f'VBoxManage setextradata "{vm_name}" "VBoxInternal/Devices/efi/0/Config/DmiSystemVersion" "1.0"')
    os.system(
        f'VBoxManage setextradata "{vm_name}" "VBoxInternal/Devices/efi/0/Config/DmiBoardProduct" "Iloveapple"')

    # Set SMC device key and enable getting key from real SMC
    os.system(
        f'VBoxManage setextradata "{vm_name}" "VBoxInternal/Devices/smc/0/Config/DeviceKey" "ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc"')
    os.system(
        f'VBoxManage setextradata "{vm_name}" "VBoxInternal/Devices/smc/0/Config/GetKeyFromRealSMC" 1')

    # Modify CPU profile
    os.system(
        f'VBoxManage modifyvm "{vm_name}" --cpu-profile "Intel Core i7-6700K"')

    print(
        "Virtual Machine "+vm_name+" modified to use cpu-profile Intel Core i7-6700K ")


pass


# Button to launch the commands
button = tk.Button(window, text="Launch Commands", command=launch_commands)
button.pack(pady=10)

# Run the window
window.mainloop()

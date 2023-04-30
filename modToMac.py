import os

# Change directory to VirtualBox installation path
os.chdir(r"C:\\Program Files\\Oracle\\VirtualBox\\")

# Prompt for VM name
vm_name = input("Enter the name of the virtual machine: ")

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

import os
import subprocess
import shutil
import urllib.request

# Clear the screen
os.system("clear")

# LEAVE CREDITS
print("""
#######################################################################################
#
#                                  Foxytoux
#
#                           Copyright (C) 2023 - 2024
#
#
#######################################################################################
""")

# Default Minecraft server script URL
server_url = "https://api.papermc.io/v2/projects/paper/versions/1.20.1/builds/196/downloads/paper-1.20.1-196.jar"

# Download the Minecraft server script
urllib.request.urlretrieve(server_url, "server.jar")

# Download openjdk-17-jdk
subprocess.run(["sudo", "apt-get", "update"])
subprocess.run(["sudo", "apt-get", "install", "openjdk-17-jdk", "-y"])

# Set default RAM amount
ram_amount = "2"  # Default to 2GB, you can change this if needed

# Modify the Java command with the default RAM amount
java_command = f"java -Xms{ram_amount}G -Xmx{ram_amount}G -jar server.jar nogui"

# Launch the Minecraft server
subprocess.run(java_command, shell=True)

# Modify the eula.txt file to set 'true'
with open("eula.txt", "w") as eula_file:
    eula_file.write("eula=true")

# Restart the Minecraft server with the new configurations
subprocess.run(java_command, shell=True)

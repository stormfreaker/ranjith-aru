import os
import socket
import paramiko
import requests
from datetime import datetime

def show_date_time():
    """Display the local date and time."""
    print("\nLocal Date and Time:")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def show_ip_address():
    """Display the local computer's IP address."""
    print("\nLocal Computer IP Address:")
    ip_address = socket.gethostbyname(socket.gethostname())
    print(ip_address)

def show_remote_home_directory():
    """Show the home directory of a remote computer."""
    print("\nRemote Home Directory Listing:")
    remote_ip = "10.30.194.63"  # Replace with your remote IP
    username = "user"            # Replace with your username
    password = "password"        # Replace with your password

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(remote_ip, username=username, password=password)
        sftp = ssh.open_sftp()
        for file in sftp.listdir("."):  # List files in the remote home directory
            print(file)
        sftp.close()
        ssh.close()
    except Exception as e:
        print(f"Error: {e}")

def backup_remote_file():
    """Back up a remote file by renaming it with a .old suffix."""
    remote_ip = "10.30.194.63"  # Replace with your remote IP
    username = "user"            # Replace with your username
    password = "password"        # Replace with your password

    file_path = input("Enter the full path of the file to back up: ")

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(remote_ip, username=username, password=password)

        sftp = ssh.open_sftp()
        backup_path = file_path + ".old"
        sftp.rename(file_path, backup_path)  # Rename file to create a backup
        print(f"File backed up as: {backup_path}")
        sftp.close()
        ssh.close()
    except Exception as e:
        print(f"Error: {e}")

def save_web_page():
    """Save the HTML content of a web page to a local file."""
    url = input("Enter the URL of the web page: ")
    file_name = input("Enter the file name to save the web page (e.g., page.html): ")

    try:
        response = requests.get(url)
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"Web page saved as: {file_name}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main menu for the program."""
    while True:
        print("\nMenu:")
        print("1 - Show date and time")
        print("2 - Show IP address")
        print("3 - Show remote home directory")
        print("4 - Backup remote file")
        print("5 - Save web page")
        print("Q - Quit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == "1":
            show_date_time()
        elif choice == "2":
            show_ip_address()
        elif choice == "3":
            show_remote_home_directory()
        elif choice == "4":
            backup_remote_file()
        elif choice == "5":
            save_web_page()
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

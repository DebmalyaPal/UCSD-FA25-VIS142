# 🐧 Linux Basics

- Raspbian OS is built on **Linux**.
- Linux is an operating system that controls hardware and runs programs.
- You interact with Linux using the **terminal** (command line).
- Commands are typed in text form, and Linux executes them.

Key concepts:
- **Directory** = folder
- **File system** = structure of files/folders
- **Command** = instruction you give to the computer


-------------------------------------------

# 🐧 Linux Basics

Raspberry Pi OS (Raspbian) is built on **Linux**.  
Linux is an operating system that manages hardware and runs programs.  
You interact with Linux using the **terminal** (command line), where you type commands and see text outputs.

---

## 🔹 Key Concepts

- **Directory** = folder
- **File system** = structure of files/folders
- **Command** = instruction you give to the computer

---

### File System Hierarchy
- Everything in Linux is treated as a *file* (even devices).
- `/` is the **root directory**.
- Common directories:
  - `/home` → user files (e.g., `/home/pi`)
  - `/bin` → basic programs (like `ls`, `cat`)
  - `/etc` → system configuration files
  - `/var` → logs and temporary data

### Users & Permissions
- Linux is multi‑user. Each user has their own home directory.
- Permissions control who can read/write/execute files.
- Example: `ls -l` shows permissions:
-rw-r--r-- 1 pi pi 1234 Nov 22 hello.txt
`-rw-r--r--` → permissions (read/write for owner, read for others)
Owner = `pi`, group = `pi`

### Processes
- Every running program is a **process**.
- `ps` shows processes, `top` shows live system usage.
- You can stop a process with `kill <PID>`.

### Package Management
- Linux uses package managers to install software.
- On Raspberry Pi OS: `apt` (Advanced Package Tool).
Example:
```bash
sudo apt update        # refresh package list
sudo apt install nano  # install nano text editor
```

---

## 🔹 Paths in Linux

- **Absolute path**: starts from root `/` and shows the full location.  
Example: `/home/pi/Documents/file.txt`

- **Relative path**: starts from your current directory.  
Example: if you are in `/home/pi`, then `Documents/file.txt` points to `/home/pi/Documents/file.txt`.  


- Special symbols:
`.` → current directory
`..` → parent directory
`~` → home directory of the current user

Example:
```
pwd               # Output: /home/pi

cd Documents
pwd              # Output: /home/pi/Documents

cd ..
pwd              # Output: /home/pi
```

---

## 🔹 Common Commands (with examples & outputs)

```
# pwd: print working directory
pwd
# Output: /home/pi

# ls: list files in current directory
ls
# Output: Desktop  Documents  Downloads

# cd: change directory
cd Documents
pwd
# Output: /home/pi/Documents

# mkdir: make new directory
mkdir test_folder
ls
# Output: test_folder

# touch: create empty file
touch hello.txt
ls
# Output: hello.txt

# cat: view contents of a file
cat hello.txt
# Output: (empty, since file has no content)

# echo: write text into a file
echo "Hello Raspberry Pi" > hello.txt
cat hello.txt
# Output: Hello Raspberry Pi

# rm: remove file
rm hello.txt
ls
# Output: (file gone)

# rmdir: remove empty directory
rmdir test_folder

# clear: clear the terminal screen
clear

# whoami: shows current user
whoami
# Output: pi

# uname -a: shows system info
uname -a
# Output: Linux raspberrypi 5.15.61-v7+ ...
```

---

## 🔹 Why Learn Linux?
- It gives **full control** over your Raspberry Pi.  
- Many servers, robots, and embedded systems run Linux.  
- Learning about Linux and its basic commands builds confidence in using computers beyond graphical interfaces.  

By practicing these commands, you’ll start feeling at home in the Linux world!

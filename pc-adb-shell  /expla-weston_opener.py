# PC CMD adb shell:
./start_weston.sh

export SNPE_TARGET_ARCH=aarch64-ubuntu-gcc7.5
# when this command is run, the env variable SNPE_TARGET_ARCH will be set to aarch64-ubuntu-gcc7.5; it will be accessible to any subsequent commands or processes executed in the same shell session. 

# export - used in Unix system Linux to create and modify environment variables, environment variables store values that can be used by programs to determine specific settings 
# SNPE_TARGET_ARCH - name environment variable created or modified, set to aarch64-ubuntu-gcc7.5.
# aarch64-ubuntu-gcc7.5 - value being assigned to env. Variable, it is target arch. specification commonly used in the context of developing software for ARM-based processors running Ubuntu Linux and compiled with GCC 7.5


export LD_LIBRARY_PATH=/data/local/tmp/snpeexample/$SNPE_TARGET_ARCH/lib
# env. Variable LD_LIBRARY_PATH will be set to /data/local/tmp/snpeexample/aarch64-ubuntu-gcc7.5/lib. This tells the operating system to search for shared libraries in the specific directory when executing programs. It is useful when custom shared libraries or dependencies must be loaded during program execution.  

# LD_LIBRARY_PATH - env variable that specifies search path for shared libraries. 
# /data/local/tmp/snpeexample/$SNPE_TARGET_ARCH/lib - value being assigned to LD_LIBRARY_PATH env variable, /data/local/tmp/snpeexample/ - path to directory snpeexample - it is project directory. 
## $SNPE_TARGET_ARCH - variable substitution means the value of SNPE_TARGET_ARCH environment variable , value of $SNPE_TARGET_ARCH will be expanded to aarch64-ubuntu-gcc7.5, resulting in the full path /data/local/tmp/snpeexample/aarch64-ubuntu-gcc7.5/lib
## lib directory typically contains these shared libraries when LD_LIBRARY_PATH environment variable is set to a directory path, the operating system searches for shared libraries in that directory when executing programs. The programs can find and link to the required shared libraries during runtime.


export PATH=$PATH:/data/local/tmp/snpeexample/$SNPE_TARGET_ARCH/bin
# path environment variable is modified to include the specified directory (/data/local/tmp/snpeexample/$SNPE_TARGET_ARCH/bin). It allows the shell to search for executable files in that directory when you enter a command. Adding a directory to the path enables the shell to find and execute programs in that directory without specifying the full path.   

# Path - the name of the env variable being created or modified. The path variable is a particular env variable that specified directories the shell could search for executable files. 
# $PATH - var substitution, it means the current value of the path environment variable. By using it, we are appending a new directory to the existing value of the PATH, 
#:/data/local/tmp/snpeexample/$SNPE_TARGET_ARCH/bin - it is the value being assigned to the PATH env variable, 
##: color is a delimiter used in the PATH variable to separate multiple directory paths.

export ADSP_LIBRARY_PATH="/data/local/tmp/snpeexample/dsp/lib;/system/lib/rfsa/adsp;/system/vendor/lib/rfsa/adsp;/dsp"
# programs or scripts can use this variable to determine the directories where ADSP libraries or related filed are located. It allows programs to locate and load the necessary ADSP libraries when executed. 

# /data/local/tmp/snpeexample/dsp/lib;/system/lib/rfsa/adsp;/system/vendor/lib/rfsa/adsp;/dsp - it is the value assigned to the  ADSP_LIBRARY_PATH environment variable. It represents a list of directory paths separated by semicolons (;). it is assuming all four directories contain ADSP (Audio Digital Signal Processor) libraries or related files. In reality the last directory contains files. 





export XDG_RUNTIME_DIR="/usr/bin/weston_socket"
# When you run this command, the XDG_RUNTIME_DIR environment variable is created or modified with the specified value (/usr/bin/weston_socket). This variable informs applications and processes that adhere to the XDG Base Directory specification about the location where runtime files and sockets should be placed.

# XDG_RUNTIME_DIR is an environment variable defined by the XDG Base Directory specification. It specifies the base directory where runtime files and sockets should be placed.
# "/usr/bin/weston_socket": This is the value being assigned to the XDG_RUNTIME_DIR environment variable. It represents the path to the directory or socket file.
## /usr/bin/weston_socket: This is the directory or socket file path being assigned to XDG_RUNTIME_DIR. It assumes that the /usr/bin/weston_socket directory or socket file is the designated location for runtime files and sockets.


mkdir -p $XDG_RUNTIME_DIR
# When you run this command, it creates the directory specified by the value of XDG_RUNTIME_DIR. If the directory already exists, the command does nothing. The -p option ensures that any necessary parent directories leading up to the target directory are created as well.

# mkdir - command to create directories or folders in file system
# -p - is option or flag used with mkdir commands, it stands for parents and ensures that all parent directories leading up to target directory are also created. If they do not exist. This option allows you to create nested directories in a single command without having to create each parent directory separately.
# $XDG_RUNTIME_DIR: This is a variable substitution. It refers to the value of the XDG_RUNTIME_DIR environment variable that was set previously. By using $XDG_RUNTIME_DIR in this command, we are referencing the directory path specified by the XDG_RUNTIME_DIR variable.


chmod 0700 $XDG_RUNTIME_DIR
# When you run this command, it changes the permissions of the directory specified by the value of XDG_RUNTIME_DIR to 0700. The owner of the directory will have read, write, and execute permissions, while the group and others will have no permissions.
## The chmod command helps manage access control to files and directories. In this case, setting the permissions to 0700 ensures that only the owner of the directory has full access, while restricting access for other users and groups. It provides a higher level of security by limiting the directory's visibility and modification rights to the owner only.

# chmod - is a command in Unix-based systems used to change the permissions of files and directories.
# 0700 -  This is the permission mode specified for the directory. In Unix-based systems, permissions are represented by a three-digit number.
## The leading 0 indicates that the number is in octal (base-8) format.
## The first digit (0) represents the special permission bits, which are irrelevant in this case.
## The second and third digits (7 and 0) represent the permission settings for the owner and group, respectively.
## The number 7 in octal translates to 111 in binary, which corresponds to read (r), write (w), and execute (x) permissions.
## The number 0 in octal translates to 000 in binary, corresponding to no permissions.

/usr/bin/weston --tty=1 --connector=29 &
# When you run this command, it starts the Weston compositor with the specified options. Weston will be launched on TTY 1, utilizing the specified connector (number 29). The & symbol at the end of the command allows the Weston process to run in the background, freeing up the shell for further commands.
## Weston provides a Wayland compositor responsible for managing and displaying graphical applications that use the Wayland display protocol. It creates the graphical environment for Wayland clients, manages windows, handles input events, and performs other compositor-related tasks.

# /usr/bin/weston: This command is executed. It refers to the executable file named "weston" located in the /usr/bin directory. Weston is a reference implementation of a Wayland compositor.
# --tty=1: This is a command-line option or flag provided to the weston command. It specifies the TTY (terminal) to be used. In this case, it sets the TTY to number 1. TTY 1 typically represents the first virtual console, which is often used for graphical user interfaces.
# --connector=29: This is another command-line option for the weston command. It specifies the connector to be used. In this case, it sets the connector to number 29. A connector represents a display output on a graphics card, such as an HDMI or DisplayPort port.
# &: This is a shell symbol known as the "ampersand" or "background operator". It is used to run the command in the background, allowing the shell to continue executing subsequent commands without waiting for the current command to complete.

# 0x12 Web stack debugging #2 

Debugging is the process of finding and fixing errors in software that prevents it from running correctly. As you become a more advanced programmer and an industry engineer, you will learn how to use debugging tools such as gdb or built-in tools that IDEs have. However, it’s important to understand the concepts and processes of debugging manually. This project covers a second part of the optimal framework and blueprint for debugging web stack (remote containers this scenario) bugs

## Challenge:

The user root is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in the root user, as if you fat finger a command and for example run rm -rf /, there is no comeback. That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the root user can do, just need to use a specific command that you need to discover.

For the containers that you are given in this project as well as the checker, everything is run under the root user, which has the ability to run anything as another user.

## Tasks 

Bash script that accepts one argument, the script should run the whoami command under the user passed as an argument, the script passes by different users
Fix a container so that Nginx is running as the nginx user.
Bash script must be 7 lines long or less from previos task

## Resources

emacs
BASH
Debian 9 stable / Ubuntu 16.04 / Ubuntu 18.04
Shellcheck

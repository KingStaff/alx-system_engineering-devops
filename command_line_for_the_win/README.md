# Command Line for the Win

This project aims to test your command line skills by completing various challenges.

## Task Completion

1. First 九 tasks: Complete the first 9 tasks on the [CMD Challenge website](https://cmdchallenge.com/). Once finished, take a screenshot of the page displaying your completed tasks. Save the screenshot with the filename "0-first_9_tasks". Remember to note the file extension (e.g., png or jpg).

2. Reach חי completed tasks: Complete the next 9 tasks on the CMD Challenge website, making a total of 18 tasks completed. Take a screenshot of the page showing your progress and save it as "1-next_9_tasks".

3. Reach the perfect cube, 27 completed tasks: Continue working on the remaining 9 tasks to reach a total of 27 completed tasks. Once done, take another screenshot of the page displaying your completion and save it as "2-next_9_tasks".

Ensure that all three screenshots are saved in the same folder on your local machine.

## Uploading Screenshots Using SFTP

1. Locate the folder where you saved the screenshots on your local machine and copy the path to the folder (e.g., `C:\Users\YourUsername\Path\To\Screenshots`).

2. Open your computer terminal (Command Prompt, PowerShell, or Terminal) and navigate to the folder path you copied using the `cd` command. For example:

   ```bash
   cd C:\Users\YourUsername\Path\To\Screenshots

1. Access the sandbox environment on your intranet and click on the SFTP option. The system will automatically provide you with SFTP credentials. Copy the credentials and paste them somewhere (e.g., a text editor) to ensure you have them correctly. The credentials should resemble the following format:

bash
sftp username@hostname
Replace username with your SFTP username and hostname with the appropriate hostname provided.

2. Return to your terminal and paste the SFTP credentials you copied earlier.

3. The system will request a password. Go back to your sandbox environment to retrieve the password associated with the provided credentials.

4. Once you have the password, enter it in the terminal. If successful, you will see a prompt similar to this:

bash
sftp>

5. Verify the current directory by using the pwd command in the terminal. Then navigate to the repository and directory you previously created using the cd command.

6. Depending on the file extension of your screenshots (png or jpg), use the appropriate extension when transferring the files to the sandbox environment. For example:

bash
put 0-first_9_tasks.png

or

bash
put 0-first_9_tasks.jpg

7. You will see progress updates and a completion message indicating the successful transfer of the screenshot.

8. To confirm if the pictures have been successfully transferred, access your working Linux environment and navigate to the appropriate directory where the repository is located.

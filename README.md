# CS321 installation instructions
Download the code through a ZIP file and unzip it. Transfer the files onto an SD card that's been formatted with the Raspberry Pi OS, either through using an ssh, WinSCP, FileZilla, etc to a desired source location.

1) WinSCP: https://winscp.net/eng/index.php  
2) FileZilla: https://filezilla-project.org/  
3) Copying through SSH: https://unix.stackexchange.com/questions/106480/how-to-copy-files-from-one-machine-to-another-using-ssh  

***Note: Using these techniques requires you to connect to the Wifi that the Raspberry Pi is connected to.***  

Regarding how to use WinSCP and FileZilla, refer to each of their documentation that are provided in the links.  

## Running the files  
To run these files, use the command ```py filename.py```  
  - **For example:** ```py driver.py```  
  
#### Things to note
There may exist some dependencies that must be downloaded to run these files.  
To check python version, run the command: 
 - ```python --version``` or ```python3 --version```  
 
To update python version, run the command: 
  - ```sudo apt upgrade``` or ```sudo apt update```  

To install a library or dependency that the files need, run the command: ```pip install library-package-name```  
  - Ex: ```pip install keyboard```
  
### Troubleshooting
1) **I can't transfer my files to the RPi. Why is that?**
  - Check the Wifi connection. You ***must*** be on the same Wifi as the RPi to be able to transfer files and communicate with it. Or, check that the SD card is fully seated into the RPi. Things happen.  
2) **I can't run the files/there's an error every time I try to run it.**
  - Check the spelling of the commands. There have been many times where our team members have mispelled something and have gotten an error in the installation process.    Also to note, you must be in the same directory as the files to be able to run it. Check that is not the case.  
3) **I need something else.**
  - Feel free to reach out to us in case something goes wrong.

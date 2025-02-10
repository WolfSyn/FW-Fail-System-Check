# FW-Fail-System-Check
- This script is used to analyze a csv file containing firmware version and failure description data.
  The script will calculate the total number of failures per firmware version and display a bar chart & pie chart.

- To run the script, provide the path to the CSV file as an argument when executing the script.

  HOW TO SET UP - 
    * First download this script & make sure you have Python 3.11 installed so you may run this prorgam.
    * Then, create a file of your choice (for e.g. C:\Test_Script ) then add the python file in in that created file.
    * all you now that you added the file in the folder you created, edit the python script and go at the bottom of the program
    * look for the "file_path" and add your designated path file on where your csv file is at
    * Now you can exit the program (since it will save on the changes) now double click on the program & it should give you a log folder giving you the outputs on the file on what is happening...

- V1 - added a logging function so when there is a failure in this script, it will give you a message indicating that fail
  also fixed the "DATE_TESTED" -> needed to add format so it may track the date & time. (needed to add hue & timestamps)

  V2 - added percentage on "Most Common Failure Descriptions per Firmware" -> so we may see its fail percentage.


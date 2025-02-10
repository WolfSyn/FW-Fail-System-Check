# FW-Fail-System-Check
- This script is used to analyze a csv file containing firmware version and failure description data.
  The script will calculate the total number of failures per firmware version and display a bar chart & pie chart.

- To run the script, provide the path to the CSV file as an argument when executing the script.
- V1 - added a logging function so when there is a failure in this script, it will give you a message indicating that fail
  also fixed the "DATE_TESTED" -> needed to add format so it may track the date & time. (needed to add hue & timestamps)

  V2 - added percentage on "Most Common Failure Descriptions per Firmware" -> so we may see its fail percentage.


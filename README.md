# fault-injection-countermeasures
This repository contains the necessary files and code for the countermeasure flow-control to the fault injection attack

To add flow control protection to your code use the automated/fc_protect.py python script.

The script recieves all legal routs to sensitive functions that need protection:
(Different routs to the same function must be entered as different -r routs)
usage: fc_protect.py <path_toc_file> -r <func1> <func2> ... <target_func1> -r <func21> <func22> ... <target_func2> 
  
![usage_image](https://user-images.githubusercontent.com/73127024/235954581-e44a8bba-c9da-4906-b9a7-82c0017691e1.jpeg)


This study is based on this emulator:
https://github.com/emsec/arm-fault-simulator

Need to add the steps to run the checks 

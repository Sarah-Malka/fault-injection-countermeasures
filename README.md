# fault-injection-countermeasures

## Flow-Control Countermeasure Automated Protection
To add flow control protection to your code use the automated/fc_protect.py python script.

The script recieves all legal routs to sensitive functions that need protection:

(Different routs to the same function must be entered as different -r routs)

usage: fc_protect.py <path_to_c_file> -r <func1> <func2> ... <target_func1> -r <func21> <func22> ... <target_func2> 
  
![usage_image](https://user-images.githubusercontent.com/73127024/235954581-e44a8bba-c9da-4906-b9a7-82c0017691e1.jpeg)

## ARMORY emulator case studies
As part of this resaerch project we used ARMORY emulator:
  
https://github.com/emsec/arm-fault-simulator
  
The testcases we ran with the emulator and the results can be found in ARMORY_tests folder.
  
It includes the code used to beautify the emulator results and simplify the usage of it.
  
To use test your code with the ARMORY emulator more easily follow the next steps:
  1. Create a folder for your original source code
    It should contain the follwing:
      a. c file
      b. linker.ld 
      c. start_emulation.py 
    Both the linker.ld and the start_emulation.py files can be found the ARMORY emulator repository
    The start_emulation's HALT_SYMBOLS variable should contain the target functions that needs protection
    The start symbol should be the entry point of the c program.
  


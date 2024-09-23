This fork adds python 2 compatibility and a new close() method. test.py is modified to print sensor values for easy testing.

[Datasheet](https://www.akm.com/content/dam/documents/products/electronic-compass/ak09915c/ak09915-data-sheet.zip)

**CompassData Interface Structure:**
+ \_\_init\_\_(rawdata) - raw values are extracted from rawdata, and then real values are calculated

**AK09915 Interface Structure:**
+ \_\_init\_\_(bus=1) - open port at some bus, reset, read WHOAMI registers
+ reset() - write reset bit to control register CNTL3, and sleep
+ measure() - write single measurement mode bit to CNTL2 and wait for staus flag, run read_data(), then return CompassData object
+ read(register, length=1) - read a number of bytes from the select register and successive registers
+ write(register_address, data) - write data to select register
+ close() - close AK port

If only the Magnetic North direction is needed then units can be ignored, but according to the library file they should be in gauss.

Raw data is multiplied by sensitivity which is 0.15uT/LSB, and the uT to Gauss conversion factor 0.01. 0.15*0.01 = 0.0015

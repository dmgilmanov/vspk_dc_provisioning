<<<<<<< HEAD
=======
# Python script to automate Nuage DC Fabric provisioning

# 1. Why is this script   #

When deploying a DCS solution, it is necessary to configure a number of L2 overlay networks to enable CBIS installation.
That is a cumbersome operation if done manually.
Sometimes inputs from CBIS people change and this operation becomes even more cumbersome because it has to be repeated.
To ease that, the script aims to automate the L2 overlay creation and adjusting process.


# 2. What is this script  #

The script is a set of functions in the functions.py file.
Each function reperesents a step of l2 overlay creation and adjusting.
Calling funcions in a proper order provides with a flexible way of achieving desired L2 overlays state. 
Check (4) for examples.


# 3. Where to use it      #

The script might be executed from any endpoint having:
* Connectivity to VSD API
* Python VSPK installed 


# 4. How to use it        #

Lets assumes that Nuage and the WBX fabric have been deployed and its time to provision overlays networks

To accomodate it:
* Fill in the **vsd_data.py** and **port_layout.py** files to make it inline with your enironment
* Comment or uncoment needed provisioning functions and **run_dc_provisioning.py** file:

`python3 run_dc_provisioning.py` 


>>>>>>> 48afa744bf1df1ac622a910fa529fb4fa6076577

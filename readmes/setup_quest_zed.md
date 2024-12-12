Setup for Quest: 
1. follow env installing instructions of repo itself
2. got into isaacgym/python and just do pip install -e . (file:///home/habibmaraqten/Code/TeleVisionProj/TeleVision/teleop/isaacgym/docs/install.html)

-> or install env from tv.yaml

3. Setup quest (follow local streaming issue of teleVision Repo)
 - plug in quest
 - lsusb to see on what ports the quest is plugegd in
 - see usb port details and speeds with lsusb -t  
 - go to ~/plaform-tools folder and do adb kill-server, adb start-server, adb devices -> should list the quest
 - if access denied:  sudo nano /etc/udev/rules.d/51-android.rules
 - select correct ports: SUBSYSTEM=="usb", ATTR{idVendor}=="2833", ATTR{idProduct}=="0186", MODE="0666", GROUP="plugdev"
 - redo the adb stuff from above
 - if adb start-server and then adb devices shows device: adb reverse tcp:8012 tcp:8012  (check for correct port again in code) 
 - go to quest browser and enter http://localhost:8012


For ZED camera:
download correct SDK from: https://www.stereolabs.com/en-de/developers/release#82af3640d775

make sure correct cuda version is supplied in conda env, -> can install locally ...

cd ~/Downloads
chmod +x ZED_SDK_Ubuntu20_cuda12.1_v4.2.2.zstd.run
./ZED_SDK_Ubuntu20_cuda12.1_v4.2.2.zstd.run


check if cam works on ~/usr/local/zed/tools   and then Diagnostics or Explorer

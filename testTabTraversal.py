# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import os, sys
import subprocess

sys.path.append('<your_paths>') # paths you want them to be included in the python class path
import time
#from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

class TestTabTraversal:

    CONST_MONKEY_COMMAND = 'D:/android/SDK/adt-bundle-windows-x86-20140702/adt-bundle-windows-x86-20140702/sdk/tools/monkeyrunner.bat'
    APK_PATH = '<your_apk_path>'
    apkPath = ""
    packageName = ""
    launcherActivityName = ""
    device = None

    def __init__(self, pApkPath, pPackageName, pLauncherActivityName, pDevice):
        self.apkPath = pApkPath
        self.packageName = pPackageName
        self.launcherActivityName = pLauncherActivityName
        self.device = pDevice

    def run(self):

        print 'Starting tab traversal test script...'

        if self.device == None: # here is important. if device instance has lost somehow, you need to re-create it
            # Connects to the current device, returning a MonkeyDevice object
            self.device = MonkeyRunner.waitForConnection(3)

        # wake up the device anyways
        self.device.wake()

        # Installs the Android package. Notice that this method returns a boolean, so you can test
        # to see if the installation worked.
        installed = self.device.installPackage(self.apkPath)

        # print installed info
        print installed

        # sets the name of the component to start
        runComponent = self.packageName + '/' + self.launcherActivityName

        # Runs the component
        self.device.startActivity(component=runComponent)

        # open login activity from WelcomePage
        self.openLoginActivity()

        # enter username and password
        self.enterUsernameAndPassword()

        # wait for 3 seconds
        MonkeyRunner.sleep(3)

        # press login and wait for 10 secs to take snapshot
        self.pressLoginButton()
        MonkeyRunner.sleep(10)

        # take the snapshot
        self.captureResultPng()

        # open tabs
        self.openMessagesTab()
        self.openContactsTab()
        self.openCallLogTab()
        self.openDialpadTab()
        self.openSettingsTab()

        # wait for 3 seconds
        MonkeyRunner.sleep(3)
        self.device.removePackage(self.packageName)

        print 'Ending tab traversal test script...'

    def openLoginActivity(self):

        # wait for 5 seconds
        MonkeyRunner.sleep(5)

        self.device.touch(545, 1580, MonkeyDevice.DOWN_AND_UP)

    def enterUsernameAndPassword(self):

        # wait for 5 seconds

        MonkeyRunner.sleep(5)

        self.device.touch(444, 338, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        self.device.type('')
        self.device.type('arglcli009')

        # wait for 3 seconds
        MonkeyRunner.sleep(2)

        self.device.touch(501, 513, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        self.device.type('')
        MonkeyRunner.sleep(1)
        self.device.type('123456')

    def pressLoginButton(self):

        # wait for 5 seconds
        MonkeyRunner.sleep(5)

        self.device.touch(963, 171, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)

    def captureResultPng(self):

        # Takes a screenshot
        result = self.device.takeSnapshot()

        # Writes the screenshot to a file
        result.writeToFile('<capture_file_path>','png')

    def openContactsTab(self):
        MonkeyRunner.sleep(3)
        print 'Openning Contacts tab...'
        starttime = int(round(time.time() * 1000))
        self.device.touch(83, 327, MonkeyDevice.DOWN_AND_UP)
        endtime = int(round(time.time() * 1000))

        print 'tab open time: %d ' % (endtime-starttime)


    def openMessagesTab(self):
        MonkeyRunner.sleep(3)
        print 'Openning Messages tab...'
        starttime = int(round(time.time() * 1000))
        self.device.touch(333, 372, MonkeyDevice.DOWN_AND_UP)
        endtime = int(round(time.time() * 1000))

        print 'tab open time: %d ' % (endtime-starttime)

    def openDialpadTab(self):
        MonkeyRunner.sleep(3)
        print 'Openning Dialpad tab...'
        starttime = int(round(time.time() * 1000))
        self.device.touch(545, 416, MonkeyDevice.DOWN_AND_UP)
        endtime = int(round(time.time() * 1000))

        print 'tab open time: %d ' % (endtime-starttime)

    def openCallLogTab(self):
        MonkeyRunner.sleep(3)
        print 'Openning Call log tab...'
        starttime = int(round(time.time() * 1000))
        self.device.touch(333, 372, MonkeyDevice.DOWN_AND_UP)
        endtime = int(round(time.time() * 1000))

        print 'tab open time: %d ' % (endtime-starttime)

    def openSettingsTab(self):
        MonkeyRunner.sleep(3)
        print 'Openning Settings tab...'
        starttime = int(round(time.time() * 1000))
        self.device.touch(764, 359, MonkeyDevice.DOWN_AND_UP)
        endtime = int(round(time.time() * 1000))

        print 'tab open time: %d ' % (endtime-starttime)

    def start(self):
        self.run()
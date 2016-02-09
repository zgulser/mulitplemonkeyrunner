# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import os, sys
import subprocess

sys.path.append('<your_path>') # not the file itself. the folder path including your files
import testTabTraversal

#from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

class TestLogin:

    CONST_MONKEY_COMMAND = 'D:/android/SDK/adt-bundle-windows-x86-20140702/adt-bundle-windows-x86-20140702/sdk/tools/monkeyrunner.bat' # your monkeyrunner.bat path
    APK_PATH = '<your_apk_path>'
    packageName = ""
    launcherActivityName = ""
    device = None

    def __init__(self, pApkPath, pPackageName, pLauncherActivityName):
        self.apkPath = pApkPath
        self.packageName = pPackageName
        self.launcherActivityName = pLauncherActivityName

    def run(self):

        print 'Starting login test script...'

        # Connects to the current device, returning a MonkeyDevice object
        self.device = MonkeyRunner.waitForConnection()

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

        print 'Ending login test script...'

        self.device.removePackage(self.packageName)
        MonkeyRunner.sleep(10)
        self.executeTabTraversalTest()

    def captureResultPng(self):

        # Takes a screenshot
        result = self.device.takeSnapshot()

        # Writes the screenshot to a file
        result.writeToFile('<capture_file_path>','png')

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

    def executeTabTraversalTest(self):
        # wait for 5 seconds
        MonkeyRunner.sleep(5)

        testTab = testTabTraversal.TestTabTraversal(self.APK_PATH,
                      '<your_package_name>',
                      '<your_launcher_activity>', # same name existing in the manifest
                      self.device) # trick is at here! pass the already-created device to the second test file 

        testTab.start()


testLogin = TestLogin(TestLogin.APK_PATH,
                      '<your_package_name>',
                      '<your_launcher_activity>' # same name existing in the manifest)

testLogin.run()
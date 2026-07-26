[app]

# (str) Title of your application
title = Twistmena Secure Vault

# (str) Package name
package.name = twistmenasecurevault

# (str) Package domain (needed for android packaging)
package.domain = org.mma

# (str) Source code where the main.py live
source.dir = .

# (str) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,requests,urllib3,certifi,idna,charset-normalizer,openssl

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be full screen or not
fullscreen = 0

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Accept SDK license
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1

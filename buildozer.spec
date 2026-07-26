[app]

# (str) Title of your application
title = Twistmena Secure Vault

# (str) Package name
package.name = twistmenasecurevault

# (str) Package domain (needed for android packaging)
package.domain = org.mma

# (str) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json
source.include_dir = 

# (list) Application requirements
requirements = python3,kivy,requests,urllib3,certifi,idna,charset-normalizer,openssl

# (list) Permissions - تم تفعيل أذونات الشبكة هنا لحل مشكلة الاتصال
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be full screen or not
fullscreen = 0

# (string) Presets
android.api = 33
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1

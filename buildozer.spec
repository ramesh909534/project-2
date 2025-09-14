[app]
# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain (unique)
package.domain = org.test

# (str) Source code where main.py lives
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# (str) Application entry point
main.py = main.py

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (list) Requirements
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,plyer

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# ✅ Version
version = 1.0

# ✅ Android settings
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 23b
android.ndk_api = 21

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2
warn_on_root = 1

[app]
# App details
title = MyApp
package.name = myapp
package.domain = org.test

# Main Python file (entry point)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Main file
main.py = main.py

# Icon / Presplash (optional)
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

# Supported orientations: landscape, portrait or all
orientation = portrait

# Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Requirements (உங்க libraries இங்கே list பண்ணணும்)
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,plyer

# Minimum API / SDK
android.api = 31
android.minapi = 21
android.ndk = 23b
android.sdk = 31
android.ndk_path = 

# Output APK name
package.version = 1.0
package.version.code = 1

# Logcat filter
log_level = 2

# Fullscreen option
fullscreen = 0


[buildozer]
log_level = 2
warn_on_root = 1

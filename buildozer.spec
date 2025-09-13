[app]
# App details
title = MyApp
package.name = myapp
package.domain = org.test

# Source files
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
main.py = main.py

# Icon / splash (optional)
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

# Orientation
orientation = portrait

# Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Requirements
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,plyer

# ✅ Version (fixed)
version = 1.0

# Android settings
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b

# Package version codes
package.version = 1.0
package.version.code = 1

# Fullscreen
fullscreen = 0


[buildozer]
log_level = 2
warn_on_root = 1

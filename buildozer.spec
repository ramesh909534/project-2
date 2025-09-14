[app]
title = MyApp
package.name = myapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,plyer
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

# Android settings
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 23b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a

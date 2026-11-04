[app]
title = IV Drip Calculator
package.name = ivdripcalc
package.domain = com.almnsob.ivdrip

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json,txt
icon.filename = %(source.dir)s/icon.png
version = 1.0

requirements = python3==3.10.12, hostpython3==3.10.12, kivy==2.3.0, kivymd==1.2.0, pillow, cython==0.29.34

android.permissions = INTERNET
android.accept_sdk_license = True

android.api = 34
android.minapi = 24
android.ndk = 25b

android.archs = arm64-v8a
android.orientation = portrait

android.private_storage = True
android.allow_backup = False

[buildozer]
warn_on_root = 0
log_level = 2

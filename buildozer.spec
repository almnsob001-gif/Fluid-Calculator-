[app]

# ===== اسم التطبيق =====
title = IV Drip Calculator
package.name = ivdripcalc
package.domain = com.almnsob.ivdrip

# ===== المصدر =====
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json,txt

# ===== الأيقونة (احذف السطر إذا لم تكن موجودة) =====
icon.filename = %(source.dir)s/icon.png

# ===== الإصدار =====
version = 1.0

# ===== المكتبات المطلوبة =====
requirements = python3==3.10.12, hostpython3==3.10.12, kivy==2.3.0, kivymd==1.2.0, pillow, cython==0.29.34

# ===== الأذونات =====
android.permissions = INTERNET
android.accept_sdk_license = True

# ===== إعدادات Android =====
android.api = 34
android.minapi = 24
android.ndk = 25b

# ===== المعمارية =====
android.archs = arm64-v8a

# ===== الاتجاه (الحل الأول) =====
android.orientation = portrait, portrait-reverse

# ===== التخزين =====
android.private_storage = True
android.allow_backup = False

# ===== Buildozer =====
[buildozer]
warn_on_root = 0
log_level = 2

[app]
title = CUgold 18 AUTO
package.name = cugold18auto
package.domain = com.rathure.cugold
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.1
requirements = python3,kivy==2.3.0,requests
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 0

[app:android]
p4a.branch = master
p4a.bootstrap = sdl2
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a, armeabi-v7a

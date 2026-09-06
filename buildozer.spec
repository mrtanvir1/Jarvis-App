[app]
title = Jarvis Assistant
package.name = jarvisapp
package.domain = org.assistant
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests,urllib3,chardet,idna
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1

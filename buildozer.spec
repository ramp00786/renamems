[app]

# (str) Title of your application
title = FileRenameApp

# (str) Package name
package.name = filerenameapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,pillow

# (str) Custom source folders for requirements
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Icon of the application
icon.filename = icon.png

# (str) Supported orientation (portrait, landscape or all)
orientation = portrait

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Pypi timeout
#timeout = 60

# (str) Android NDK version to use
android.ndk = 21b

# (str) Android SDK version to use
android.sdk = 28

# (int) Android API version to use
android.api = 27

# (int) Android minimum API version to use
android.minapi = 21

# (int) Android architecture to build for, can be one of armeabi-v7a, arm64-v8a, x86 or all
android.arch = armeabi-v7a,arm64-v8a

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
android.apptheme = "@android:style/Theme.NoTitleBar.Fullscreen"

# (list) Pattern to whitelist for the whole project
whitelist = */fonts/*.ttf,*/fonts/*.otf,*/images/*.png,*/images/*.jpg,*/sounds/*.wav,*/sounds/*.mp3

# (str) Path to a custom whitelist file
#whitelist_src = whitelist.txt

# (str) Path to a custom blacklist file
#blacklist_src = blacklist.txt

# (list) List of Java .jar files to add to the libs so that pyjnius can access
android.add_jars = foo.jar,bar.jar

# (list) List of Java files to add to the android project (can be java or a directory containing the files)
#android.add_src = foo.java,dir/bar.java

# (list) Android AAR archives to add (currently works only with sdl2_gradle
# and python-for-android projects)
#android.add_aars = foo.aar,bar.aar

# (list) Gradle dependencies to add (currently works only with sdl2_gradle
# and python-for-android projects)
#android.gradle_dependencies = com.android.support:support-core-ui:28.0.0

# (list) Packaging options to add (currently works only with sdl2_gradle
# and python-for-android projects)
#android.packaging_options = ...

# (str) Android add build dependencies (gradle dependencies)
#android.gradle_dependencies = com.android.support:support-core-utils:27.+

adb locat -c
adb logcat | $NDK_ROOT/ndk-stack -sym ./$1proj.android/obj/local/armeabi

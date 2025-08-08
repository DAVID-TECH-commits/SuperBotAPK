@echo off
cd /d "C:\Users\David Adeola\Desktop\DavidAPKBuild"
echo Building APK...
buildozer -v android debug
echo.
echo Build finished. Press any key to close.
pause

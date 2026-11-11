@echo off
rem Runs the live typing test against the running amiKey; output to Z:\amiKey\Windows\Tests\livetest.out
C:\vk\build\App\amikey_livetest.exe C:\vk\src\Windows\Tests\cases.tsv > Z:\amiKey\Windows\Tests\livetest.out 2>&1
echo EXIT %ERRORLEVEL% >> Z:\amiKey\Windows\Tests\livetest.out

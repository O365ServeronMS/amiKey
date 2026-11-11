// Crash reports, the Windows side of App/Model/CrashReporter.swift.
// At crash time a small text report (exception, module+offset of the fault and of each stack frame, amiKey and Windows
// versions, thread id) is written to %LOCALAPPDATA%\amiKey\Crashes\amiKey-YYYY-MM-DD-HHMMSS.txt. No typed text, no
// clipboard, no window titles, no minidump. amiKey has no crash server: reports stay on disk. Only when the hidden
// "crashEndpoint" pref names a server does the next launch ask whether to send it (or send it when the user chose
// "always"). The profile folder (C:\Users\<name>) is reduced to "~" before sending.
#pragma once
#include <windows.h>
namespace amikey { namespace crash {
void install();               // as early as possible: unhandled exceptions, std::terminate, abort, pure call, invalid parameter
void selfTestIfAsked();       // hidden: "--crash-self-test" crashes with an access violation, "--crash-self-test=terminate" via std::terminate
void checkAtLaunch();         // after the tray is up: one question (on its own thread) for the newest unhandled report
}}

// Updates from the newest GitHub release of O365ServeronMS/amiKey: its amiKey-update-<arch>.txt names the version,
// the installer and an Ed25519 signature (made by the CI with the AMIKEY_UPDATE_KEY secret) over the version and file.
// Checks daily when "Tự động cập nhật" is on, downloads and verifies the installer, and installs it
// when amiKey quits (or at the next launch). "Kiểm tra cập nhật…" checks now and asks.
#pragma once
#include <windows.h>
namespace amikey { namespace updater {
const UINT WM_UPDATER = WM_APP + 4;   // posted to the owner: wParam = Event
enum Event { EvUpToDate = 1, EvFailed, EvAvailable, EvDownloaded };
void start(HWND owner);               // first check after a short delay, then daily
void checkNow(HWND owner);            // manual check; the result is shown to the user
void onEvent(WPARAM ev);              // the owner's handler for WM_UPDATER
bool installPendingAndQuit();         // at quit: runs a downloaded, verified installer; true if it did
bool installPendingAtLaunch();        // at launch: a verified newer installer waits → run it and exit
}}

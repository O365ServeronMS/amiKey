; amiKey for Windows installer (Inno Setup 6). Per-user, no admin prompt, so the app can update itself.
;   iscc /DVersion=1.0.14 /DArch=x64 /DSrc=..\build\App amiKey.iss
#ifndef Version
  #define Version "0.0.0"
#endif
#ifndef Arch
  #define Arch "x64"
#endif
#ifndef Src
  #define Src "..\build\App"
#endif

[Setup]
AppId={{3F6C2A9E-5B1D-4E87-A2C4-7D9E0B1F6A35}
AppName=amiKey
AppVersion={#Version}
AppVerName=amiKey {#Version}
AppPublisher=ami
AppPublisherURL=https://github.com/O365ServeronMS/amiKey
AppSupportURL=https://github.com/O365ServeronMS/amiKey#readme
AppUpdatesURL=https://github.com/O365ServeronMS/amiKey/releases
VersionInfoVersion={#Version}
DefaultDirName={localappdata}\Programs\amiKey
DisableDirPage=yes
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
OutputDir=.\out
OutputBaseFilename=amiKey-{#Version}-{#Arch}-Setup
SetupIconFile=..\App\amiKey.ico
UninstallDisplayIcon={app}\amiKey.exe
UninstallDisplayName=amiKey
Compression=lzma2/max
SolidCompression=yes
WizardStyle=modern
CloseApplications=yes
CloseApplicationsFilter=amiKey.exe
RestartApplications=no
#if Arch == "arm64"
ArchitecturesAllowed=arm64
ArchitecturesInstallIn64BitMode=arm64
#else
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
#endif

[Languages]
Name: "en"; MessagesFile: "compiler:Default.isl"

[Messages]
; the few screens people see, in Vietnamese like the app
WelcomeLabel1=Cài đặt amiKey
WelcomeLabel2=amiKey {#Version} sẽ được cài cho tài khoản của bạn, không cần quyền quản trị.%n%nBấm Next để tiếp tục.
FinishedHeadingLabel=Đã cài xong amiKey
FinishedLabel=amiKey nằm ở khay hệ thống (góc dưới bên phải). Bấm Alt+Z để chuyển Anh/Việt.
ConfirmUninstall=Gỡ amiKey khỏi máy?

[Files]
Source: "{#Src}\amiKey.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\amiKey"; Filename: "{app}\amiKey.exe"

[Registry]
; the app's own "Mở amiKey khi đăng nhập" entry goes away with the app
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueName: "amiKey"; Flags: uninsdeletevalue dontcreatekey

[Run]
Filename: "{app}\amiKey.exe"; Description: "Mở amiKey"; Flags: nowait postinstall skipifsilent
; a self-update (amiKey runs the installer silently with /RELAUNCH=1) brings the app back
Filename: "{app}\amiKey.exe"; Flags: nowait; Check: ShouldRelaunch

[UninstallRun]
Filename: "{sys}\taskkill.exe"; Parameters: "/IM amiKey.exe /F"; Flags: runhidden; RunOnceId: "KillamiKey"

[Code]
function ShouldRelaunch: Boolean;
begin
  Result := ExpandConstant('{param:RELAUNCH|0}') = '1';
end;

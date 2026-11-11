# amiKey

Vietnamese typing for Windows that switches between Vietnamese and English for you.

Type Telex as usual. When you type an English word in Vietnamese mode, or a Vietnamese word in English mode, amiKey
fixes the word and switches the language. No more pressing the switch key every few words.

Made by ami. Free and open source under GPL-3.0.

## Download

Get the installer from [Releases](https://github.com/O365ServeronMS/amiKey/releases/latest):

- `amiKey-<version>-x64-Setup.exe` for most PCs (Intel/AMD), `amiKey-<version>-arm64-Setup.exe` for Windows on ARM.
- `amiKey-<version>-<arch>-portable.zip` runs without installing.

The installer is per-user: no administrator prompt. amiKey sits in the system tray (V = Vietnamese, E = English) and
updates itself from this repository's releases. Until the builds are code-signed, Windows SmartScreen asks first:
click **More info**, then **Run anyway**.

## Features

- **Telex** with modern or classic tone placement (hoà / hòa), spell checking, and keeping your keys as typed when a word isn't Vietnamese.
- **Auto switch:**
  - `more` → stays English;
  - `treen` → `trên`;
  - `truowfng`, `truongwf`, `truwownfg` → `trường`;
  - `this makes sense` comes out right in Vietnamese mode, because ambiguous words are fixed once the context is clear.
- **Programming-aware:** `var`, `const`, `git push`, `obj.dir` and `my_var` are left alone.
- **Undo:** press Backspace right after an automatic fix to undo it.
- **Remembers the language** for each app, and for each website in Chrome, Edge, Brave, Vivaldi, Opera and Firefox.
- **Switch hotkey:** Alt+Z by default; a key with modifiers, or modifiers alone, with an optional sound.
- **Emoji picker** with Vietnamese and Telex search.
- **Works with other layouts:** amiKey steps aside for other input languages (Japanese, Chinese…). Password fields get your keys untouched.

## Build

Requires Visual Studio 2022 (C++ desktop workload), CMake 3.21+ and Ninja. From a Developer PowerShell:

```powershell
cmake -S Windows -B Windows/build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build Windows/build --target amikey
```

The app is `Windows/build/App/amiKey.exe`. The version comes from `project.yml`.

## Tests

Every typing rule is locked down by tests: rule-tagged cases, golden snapshots of typing a mixed Vietnamese/English
corpus, every Vietnamese syllable, driver/simulator parity and a performance budget.

```powershell
pwsh Windows/check.ps1
```

`Windows/Tests/` has a live test that types through the running app. See [DECISIONS.md](DECISIONS.md) for every rule
and why it exists.

## Releasing

1. Set `MARKETING_VERSION` (and `CURRENT_PROJECT_VERSION`) in `project.yml`, commit, push.
2. Push the tag `v<version>`. [`.github/workflows/windows.yml`](.github/workflows/windows.yml) builds x64 and ARM64,
   signs, packages (Inno Setup), writes the signed update manifests and publishes the GitHub release.

Secrets: `CERTUM_EMAIL` / `CERTUM_OTP` (code signing) and `AMIKEY_UPDATE_KEY` (update signing). Without the Certum
secrets the release stops; to publish unsigned installers anyway, run the workflow by hand with `allow_unsigned`.

## Contributing

Pull requests are welcome, AI-written code included. Show the problem with a screenshot or video, describe the
before and after, and add test cases. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License and credits

amiKey is distributed under the GNU General Public License v3.0, see [LICENSE](LICENSE). It is a modified version of
[Vikey](https://github.com/tonyminibot/Vikey) by Tony Dinh, which is based on [OpenKey](https://github.com/tuyenvm/OpenKey)
by Tuyen Mai. Data and other code it uses: [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md).

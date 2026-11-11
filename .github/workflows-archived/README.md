# Archived workflows

GitHub only runs workflows in .github/workflows, so these do not run. amiKey ships Windows only;
Windows/check.ps1 (in windows.yml) runs the same engine lock as engine-rules.yml.
To bring one back: git mv .github/workflows-archived/<name>.yml .github/workflows/

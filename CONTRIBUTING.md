# Contributing to amiKey

Thanks for helping. Bug fixes and new features are welcome.

## AI-written code is welcome

Use Claude, Copilot, Cursor or anything else. You don't need to say which parts an AI wrote. You do need to
understand the change and have tested it yourself, the same as code you typed by hand.

## What a pull request needs

1. **Show it.** A new feature or a change of behaviour must include a screenshot or a short demo video of the new
   behaviour; pull requests without one are not merged. For a bug fix, show the bug.
2. **Before and after.** In the description, write what happened before your change and what happens after it.
   Short sentences are fine. Example: "Before: typing `os` in Vietnamese gave `os` and switched to English.
   After: it gives `ó`."
3. **Tests.** Add test cases for the behavior you changed (see below). A fix with a test that fails before it and
   passes after it gets merged fastest.
4. **One change per pull request.** Smaller pull requests are easier to review.

## Where tests go

| Area | Add cases to | Run |
|---|---|---|
| Typing rules (Telex, auto switch, spelling) | `Tools/autoswitch/rules/rules.tsv`, and a decision in `DECISIONS.md` for a new rule | `pwsh Windows/check.ps1` |
| Windows app | `Windows/Tests/cases.tsv` (live test) | `Windows/Tests/run_livetest.cmd` with amiKey running |

`check.ps1` locks the engine's behavior with golden snapshots. If your change is meant to change typing results,
review the diffs it prints, then run `pwsh Windows/check.ps1 update` and say in the pull request which results
changed and why.

## Before you open the pull request

- The tests for the parts you touched pass on your machine (CI runs them too).
- No secrets, keys or personal data in the code or the screenshots.
- amiKey is GPL-3.0. By contributing, you agree your code is released under the same license.

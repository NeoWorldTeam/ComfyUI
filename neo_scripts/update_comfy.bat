@echo off
setlocal

echo Checking for merge conflicts and resetting them...
git fetch --all

:: Reset any conflicted files
for /f "tokens=*" %%i in ('git diff --name-only --diff-filter=U') do (
    git checkout --theirs "%%i"
    git add "%%i"
)

echo Updating main repository...
git pull --rebase

echo Updating submodules...
git submodule foreach --recursive "git fetch --all"
git submodule foreach --recursive "git merge --no-commit --no-ff -s recursive -X theirs"

echo Update complete.
endlocal

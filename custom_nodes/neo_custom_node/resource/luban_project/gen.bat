set WORKSPACE=..
set LUBAN_DLL=%WORKSPACE%\Tools\Luban\Luban.dll
set CONF_ROOT=.

dotnet %LUBAN_DLL% ^
    -t all ^
    -c python-json ^
    -d json ^
    --conf %CONF_ROOT%\luban.conf ^
    -x outputCodeDir=python_schema ^
    -x outputDataDir=json_data

dotnet %LUBAN_DLL% ^
    -t client ^
    -d json ^
    --conf %CONF_ROOT%\luban.conf ^
    -x outputDataDir=json_data_client

pause

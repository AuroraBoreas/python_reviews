@REM Ref: https://stackoverflow.com/questions/25554254/batch-command-to-delete-all-subfolders-with-a-specific-name
@REM @ZL, 20210903

@echo off
goto :main

:main
	set pycache=__pycache__
	set cppcache1=bin
	set cppcache2=obj
	
	echo.
	echo remove operation started..
	
	@REM remove python caches
	FOR /d /r . %%d IN (%pycache%) DO @IF EXIST "%%d" rd /s /q "%%d"
	FOR /r . %%f in (*.db) do @if exist "%%f" del /s /q "%%f"
	
	@REM remove c++ caches
	FOR /d /r . %%d IN (%cppcache1%) DO @IF EXIST "%%d" rd /s /q "%%d"
	FOR /d /r . %%d IN (%cppcache2%) DO @IF EXIST "%%d" rd /s /q "%%d"
	
	echo.
	echo remove operation finished
	pause
goto :eof
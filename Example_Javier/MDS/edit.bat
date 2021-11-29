@echo off


REM Change the value of this variable if you have your BoUML installed in a different location:
set BOUML_LOCATION=C:\Program Files (x86)\Bouml

REM Change this variable so that it has the location of the version of eclipse you are using:
set ECLIPSE_LOCATION=C:\eclipse


REM Invocation of the UML editting tool and the eclipse IDE tool:

start /D "%BOUML_LOCATION%" "%BOUML_LOCATION%\bouml.exe" ".\mdsUML\mdsUML.prj"

start "Opening eclipse to edit/run the MDS application" /D "%ECLIPSE_LOCATION%" "%ECLIPSE_LOCATION%\eclipse.exe" -data "%~dp0ws"


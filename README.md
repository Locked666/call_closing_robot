*Call Closing Robot


execute build pro prod: 
```pyinstaller --onefile --noconsole --i ico.ico --add-data "ico.ico;." --name CallClosingRobot   main.py ```


for developed: 
```pyinstaller --onefile --i ico.ico --add-data "ico.ico;." --name CallClosingRobot   main.py```
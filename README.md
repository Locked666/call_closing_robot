# Call Closing Robot

execute build pro prod:

```bash
pyinstaller --onefile --noconsole --i ico.ico --add-data "ico.ico;." --add-data "utils;utils" --name CallClosingRobot   main.py
```

for developed:

```bash
pyinstaller --onefile --i ico.ico --add-data "ico.ico;." --add-data "utils;utils" --name CallClosingRobot   main.py
```

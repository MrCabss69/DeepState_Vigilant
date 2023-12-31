![screenshot_1703947452 9943547](https://github.com/MrCabss69/DeepState_Vigilant/assets/48258972/3b357e61-2c51-496f-b22a-45c926705d7f)# DeepState_Vigilant

DeepState_Vigilant is a Python script designed to monitor the ongoing war situation in Ukraine. It has been tested and verified on Linux, Fedora 38.

The script utilizes data from Deep State Map, a live map that provides real-time updates on the conflict.

Data Source: https://deepstatemap.live

##  What it does?

DeepState_Vigilant is designed to periodically scrape the Deep State Map and save a screenshot of the current state of the map in a designated 'images' folder. Each screenshot is timestamped for easy reference. By default, the script captures and saves a screenshot every 12 hours.

The script employs the Selenium WebDriver for Firefox (GeckoDriver) to automate the browser interactions required for the scraping process. It is designed to run in headless mode, meaning it operates without opening a physical browser window. However, it can also be run in a non-headless mode for debugging purposes.


#### July, 28 - 2023
![screenshot_1690520361 4813125](https://github.com/MrCabss69/DeepState_Vigilant/assets/48258972/f32f5004-6bd4-4776-b41c-942e0fc9c370)

#### October, 30 - 2023
![screenshot_1698618378 7576723](https://github.com/MrCabss69/DeepState_Vigilant/assets/48258972/44f35b36-44f7-4d35-b7c3-13bee6209b66)

#### December, 30 - 2023
![screenshot_1703947452 9943547](https://github.com/MrCabss69/DeepState_Vigilant/assets/48258972/e71a77a3-386b-46d3-9a01-6dd7d4954b91)


## Suggestion
To ensure that the script runs continuously without the need for manual intervention, consider implementing it as an operating system service. This will allow the script to automatically restart with your computer.

For Linux users, you can use the systemctl services to achieve this.

## Improvements and debugging
Pending to add filters to monitor recent attacks on the web scrapping.

For debugging replace:

        web_navigator = DeepstateNavigator()

with:


        web_navigator = DeepstateNavigator(False)

This will exec the script on main thread, and you will see the actions live on your browser


We are currently working on adding filters to monitor recent attacks and it's types and damages during the web scraping process. Any contributions or suggestions for improvements are welcome.


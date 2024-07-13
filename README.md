# PyStreamList  

Creates a playlist with the url for your favorite internet radio stations 
that can be used with your streaming software. This will keep you station 
urls updated as they change over time.  

## Installation  

```
# instal prerequisites
pip install pyradios
pip install pyyaml
pip install python-dotenv

# create your own copy of the stations file,
# then edit to add you favorite stations from radio-browser.info
cp stations-example.yml stations.yml

# create your own copy of the .env file,
# and change the default values as needed
cp .env.example .env

```

## Usage  

After installation, you can run the main script to generate the playlist files 
in your output folder.  

Run this command:  

```
python3 main.py
```  

## Editing the stations.yml file  

The idea of this file is to track your favorite radio station by a unique
id that doesn't change instead of a url that might change. You should also
add a friendly name to each id so that you can easily find stations and update
them.  

The file is a list of items, each having 2 properties:  

1. `uuid` - this is the unique station id from radio-browser.info
2. `friendly_name` - this is any arbitrary name for you to uniquely identify this entry  


# Translater

This is a simple project to automate translating new data for the 
OpenSupports project.

# Usage

In OpenSupports, there is [a folder with files for every language](https://github.com/opensupports/opensupports/tree/master/client/src/data/languages) 
we support. Since it is tiring to add new translations to all the files 
whenever someone wants to add a new phrase for translation, this script
automates it.

The idea is to only add the translation for the english language, and then
run this script, that will automatically translate the value of the new
phrase and complete all the languages translations.

# Demo

Here there is a picture of how it works:

![demo](https://github.com/mredigonda/opensupports-translater/blob/master/demo.png)

# How to use it

Simply copy main.py to the data/languages folder and run it, you will need to
update your version of googletrans according to [this commit](https://github.com/ssut/py-googletrans/pull/78/files).



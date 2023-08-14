# Uni checker usage and dev notes.

## Head developer: J.E.V.A.

[Universities API](http://universities.hipolabs.com/search?country=)


**important bug notes**
problem where the api is called twice, for example: serbia has 13 universities, but the app will show 26 as of version 1.1.0. it will also print the names twice when trying to call the names.

**important vscode changes**
VSCode has a base max number of cmd output lines, some countries like the United States have more universities than the max number of lines, to view all of them by name (`uni_names()`) you will have to change some setting in VSCode.
1. cmd + , or cntrl + , to open up the settings page. 
2. look up scrollback. 
3. modifyboth numbers to the new value you want.

**Whats new**
version 1.1.0: added a graph funtion (`uni_graph`) for visual representation of data.

**Usage**
This code tries to tackle a very simple question. Does the number of universities influence a countries GDP? As of version 1.0.0 and 1.1.0 the code only shows the number of universitie per country using a public API, in future version the implemantation of population size and GDP API's will help reach a conclusion to the original question. Uni_checker version 1.1.0 has three differente functions, to check the names of the universities in a country searching for it by name (`uni_names()`), to check the number of univesrisities in a specified country (`num_unis()`) and to compare the number of universities in two different countries (`diff_num_unis()`). Usage of Uni_checker is free, public and open source, this is a personal projet for future research, id also hope for Uni_Chekcer to be of use for others.

**API info**
as of version 1.1.0 "Univerisites API" does not need a key, if a future API does require one notice will be here with the respective link needed and tutorial to get the key.

**future development**:
Hotfixes and performance upgrades will be handeled in versions 1.x.1 - 1.x.x, in versions 1.2.0 and 1.3.0 id like to implement population size and GDP (gross domestic prodcut) API's acordingly. Id also like to implement a friendlier user interface, the next update will be a hotfix update to fix the previously stated bug.

**Personal note from dev**
Uni_checker is a personal project. A simple to use code that would display data about a countries GDP, population size and universites, hopefully this project can be used for future research.
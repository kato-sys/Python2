# Uni checker usage and dev notes.

## Head developer: J.E.V.A.

[Universities API](http://universities.hipolabs.com/search?country=)


**Note for professor**
Sorry for the language switch, from spanish in the program to english in the .md, i just felt like writing the documentation in english.

**important vscode changes**:
VSCode has a base max number of cmd output lines, some countries like the United States have more universities than the max number of lines, to view all of them by name (`uni_names()`) you will have to change some setting in VSCode.
1. cmd + , or cntrl + , to open up the settings page. 
2. look up scrollback. 
3. modifyboth numbers to the new value you want.

**Usage**
This code tries to tackle a very simple question. Does the number of universities influence a countries GDP? As of version 1.0.0 the code only shows the number of universitie pero country using a public API, in future version the implemantation of population size and GDP API's will help reach a conclusion to the original question.
Uni_checker version 1.0.0 has three differente functions, to check the names of the universities in a country searching for it by name (`uni_names()`), to check the number of univesrisities in a specified country (`num_unis()`) and to compare the number of universities in two different countries (`diff_num_unis()`). Usage of Uni_checker is free, public and open source, this is a personal projet for future research, id also hope for Uni_Chekcer to be of use for others.

**API info**
as of version 1.0.0 "Univerisites API" does not need a key, if a future API does require one notice will be here with the respective link needed and tutorial to get the key.

**future development**:
In version 1.1.0 of Uni_checker id like to expand out of the CMD and into a more graphical interface by using libraries like pandas, numpy and matplotlib. Hotfixes and performance upgrades will be handeled in versions 1.x.1 - 1.x.x, in versions 1.2.0 and 1.3.0 id like to implement population size and GDP (gross domestic prodcut) API's acordingly. Id also like to implement a better user interface and more languages as well as ways to choose the type of graph the data will be displayed on. observe the relationship between all three factors.

**Personal note from dev**
Uni_checker started out, and as of version 1.0.0 and 1.1.0 still is, as a homework assignment for an online programming course from a national universitiy, but as my professor said, its a project we should enjoy, and i decided to make it my first python project, a simple to use code that would display data i found relevant, in this case, GDP, population size and universites, hopefully this can grow more than just a homework asignment and actually find its way into the hands of people that can use the information for research, still if it doesnt, im still proud of my first ever python baby (project). 

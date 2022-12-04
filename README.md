# CS50X
 
# **Look-a-Location**
Video Demo:

##     Description:
This was created specifically as a final project for [CS50’s Introduction to Computer Science](https://cs50.harvard.edu/x/2022/). 

This project consists in a multi-purpose bot 


A real world simulation would be, for example:

You are walking by, let's say, Berlin, and you want to get a place to stay for the night. You can use this program to tailor your preferences and get the top results.


So you want the best 5 lodging places in Berlin, in a 20 km radius, sorted by number of reviews, or you aren't sure what you want to see, so you want to see what you can choose from?

Perfect! You open up this program, where you're prompted with simple questions like:

- Desired Location
- Desired Radius of search
- Desired Type of Attraction

If you don't know what exactly you are looking for, there is always the option to leave the line blank or type the word `attractions` to see a table of available options. As a bonus, if you're feeling extra indecisive, you can just input `random` and a random option will be chosen.

The program will output the number of found results and prompt for how many you want to see.

Then it will prompt for a sorting filter. You can choose between `Name` , `Rating` and `Number of Reviews` . In the case that you don't want to choose a specific filter, the default is  `Number of Reviews`.

Finally, the program asks you if you want to do another search, where you can choose between `yes` or `no`. If choosing `yes/y`, the program restarts, whilst `no/n` exits the program.


This program has 6 functions.

- `main` focuses on executing everything.

- `place_get` focuses on asking the user for the desired location, and with the help of Google's Places API, fetches the coordinates of the specified input.

- `attraction_select` asks for the radius and for a type of allowed attraction.

- `get_attraction` returns a a list tailored to the user input.

- `final_result` returns the actual desired statements of the locations, filtered to the users needs.

- `search_again` just asks if the user want to basically, restart the program or exit.

The `test_project.py` contains tests for each function of the main project file.


With this final project I was able to implement almost everything from the CS50P course.
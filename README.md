# CS50X
 
# **Look-a-Location**
Video Demo:

##     Description:
This was created specifically as a final project for [CS50’s Introduction to Computer Science](https://cs50.harvard.edu/x/2022/). 

This project consists in a multi-purpose bot that uses a voice recognition API and other useful libraries like FFMPEG.

A practical use would be, for example:

You are texting with someone or they have some news you need to hear but you're at a loud place and can't hear anything


This program has 6 functions.

- `main` focuses on executing everything.

- `place_get` focuses on asking the user for the desired location, and with the help of Google's Places API, fetches the coordinates of the specified input.

- `attraction_select` asks for the radius and for a type of allowed attraction.

- `get_attraction` returns a a list tailored to the user input.

- `final_result` returns the actual desired statements of the locations, filtered to the users needs.

- `search_again` just asks if the user want to basically, restart the program or exit.

The `test_project.py` contains tests for each function of the main project file.


With this final project I was able to implement almost everything from the CS50P course.
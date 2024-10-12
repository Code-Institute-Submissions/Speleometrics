# Speleometrics | a Cave Collaborative Database

![Speleometrics](docs/documentation/speleometrics.png)

[Visit my Python command line interface (CLI) application here](https://speleometrics-586df55c9a57.herokuapp.com/)

Return back to the [README.md](README.md) file.

## Testing - Table of Contents  
  
- [Testing](#TESTING.md)
  - [Testing Contents](#testing---table-of-contents)
  - [Validation](#61-validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [CSS Validation](#css-validation)
    - [Lighthouse Scores](#lighthouse-scores)
    - [Wave Accessibility Evaluation](#wave-accessibility-evaluation)
  - [Manual Testing](#manual-testing)
    - [User Input/Form Validation](#user-inputform-validation)
    - [Browser Compatibility](#browser-compatibility)
    - [Testing User Stories](#testing-user-stories)
    - [Dev Tools/Real World Device Testing](#dev-toolsreal-world-device-testing)
  - [Bugs](#bugs)
    - [Known Bugs](#known-bugs)



### **6.1. Validation**

#### **Html Validation**

html validation was conducted through [HTML W3C Validator](https://validator.w3.org). 
The following images are validation screenshots taken from the service with the website Heroku live link. 
 - The validator could not test the pages that required superuser credentials (Reports Section).
 - All the pages were valid, with no errors or warnings except one:
    - Cave Page: The validator point out that there was a stray div tag on the page (this will be further discussed on Bugs).

<details>
<summary>Cave Page</summary>

![Cave Page](documentation/testing/w3_html/cave_page.png)
</details>

| Page         | Status                 | Screenshot                                                |
|--------------|------------------------|-----------------------------------------------------------|
| About        | No errors or warnings   | <details><summary>Show Screenshot</summary> ![About](documentation/testing/w3_html/about.png) </details> |
| Add Cave     | No errors or warnings   | <details><summary>Show Screenshot</summary> ![Add Cave](documentation/testing/w3_html/add_cave.png) </details> |
| Cave Map     | No errors or warnings   | <details><summary>Show Screenshot</summary> ![Cave Map](documentation/testing/w3_html/cave_map.png) </details> |
| Cave Table   | No errors or warnings   | <details><summary>Show Screenshot</summary> ![Cave Table](documentation/testing/w3_html/cave_table.png) </details> |
| Index        | No errors or warnings   | <details><summary>Show Screenshot</summary> ![Index](documentation/testing/w3_html/index.png) </details> |
| Profile Page | No errors or warnings   | <details><summary>Show Screenshot</summary> ![Profile Page](documentation/testing/w3_html/profile_page.png) </details> |
| User Caves   | No errors or warnings   | <details><summary>Show Screenshot</summary> ![User Caves](documentation/testing/w3_html/user_caves.png) </details> |


#### **Performance Lighthouse**

In general, Lighthouse evaluated a good performance on all the website pages. The following image shows the score in the performance register by Google's Chrome validator. The cave map page, which relies on Leaflet API, comprised of a basemap and approximately 600 caves, got a score of 79 and 77, desktop and mobile, respectively. It is important to point out that similar webGIS pages have subpar lighthouse scores; as an example, I tested the IDE Sisema page with no vectorial features selected, just the basemap. The result for the desktop was 59. Thus, the scores obtained are reasonable, considering the page's content.

<details>
<summary>Lighthouse Validator Cave Map Mobile</summary>

![Lighthouse Validator Cave Map Mobile](documentation/testing/lighthouse/lighthouse_cave_map_mobile.png)
</details>

<details>
<summary>Lighthouse Validator Cave Map Mobile</summary>

![Lighthouse Validator Cave Map Desktop](documentation/testing/lighthouse/lighthouse_cave_map_desktop.png)
</details>

<details>
<summary>Lighthouse Validator Cave Map Mobile</summary>

![Lighthouse Validator IDE Sisema](documentation/testing/lighthouse/lighthouse_ide_sisema.png)
</details>



| Page               | Score | Screenshot                                                                                                                 |
|--------------------|-------|-----------------------------------------------------------------------------------------------------------------------------|
| About              | 99    | <details><summary>Show Screenshot</summary> ![About](documentation/testing/lighthouse/lighthouse_about_desktop.png) </details> |
| Add Cave           | 100    | <details><summary>Show Screenshot</summary> ![Add Cave](documentation/testing/lighthouse/lighthouse_add_cave_desktop.png) </details> |
| Cave Map           | 79    | <details><summary>Show Screenshot</summary> ![Cave Map](documentation/testing/lighthouse/lighthouse_cave_map_desktop.png) </details> |
| Cave Page          | 99    | <details><summary>Show Screenshot</summary> ![Cave Page](documentation/testing/lighthouse/lighthouse_cave_page_desktop.png) </details> |
| Cave Table         | 97    | <details><summary>Show Screenshot</summary> ![Cave Table](documentation/testing/lighthouse/lighthouse_cave_table_desktop.png) </details> |
| Index              | 97    | <details><summary>Show Screenshot</summary> ![Index](documentation/testing/lighthouse/lighthouse_index_desktop.png) </details> |
| Profile Page       | 99    | <details><summary>Show Screenshot</summary> ![Profile Page](documentation/testing/lighthouse/lighthouse_user_area_desktop.png) </details> |
| User Edit          | 95    | <details><summary>Show Screenshot</summary> ![User Edit](documentation/testing/lighthouse/lighthouse_user_caves_desktop.png) </details> |
| User Caves         | 99    | <details><summary>Show Screenshot</summary> ![User Caves](documentation/testing/lighthouse/lighthouse_user_caves_desktop.png) </details> |
| Report Dashboard   | 100    | <details><summary>Show Screenshot</summary> ![Report Dashboard](documentation/testing/lighthouse/lighthouse_report_desktop.png) </details> |
| Report Description | 95    | <details><summary>Show Screenshot</summary> ![Report Description](documentation/testing/lighthouse/lighthouse_report_page_desktop.png) </details> |


| Page               | Score | Screenshot                                                                                                                |
|--------------------|-------|----------------------------------------------------------------------------------------------------------------------------|
| About              | 92    | <details><summary>Show Screenshot</summary> ![About](documentation/testing/lighthouse/lighthouse_about_mobile.png) </details> |
| Add Cave           | 93   | <details><summary>Show Screenshot</summary> ![Add Cave](documentation/testing/lighthouse/lighthouse_add_cave_mobile.png) </details> |
| Cave Map           | 77    | <details><summary>Show Screenshot</summary> ![Cave Map](documentation/testing/lighthouse/lighthouse_cave_map_mobile.png) </details> |
| Cave Page           | 93    | <details><summary>Show Screenshot</summary> ![Cave Map](documentation/testing/lighthouse/lighthouse_cave_page_mobile.png) </details> |
| Cave Table         | 94    | <details><summary>Show Screenshot</summary> ![Cave Table](documentation/testing/lighthouse/lighthouse_cave_table_mobile.png) </details> |
| Index              | 83    | <details><summary>Show Screenshot</summary> ![Index](documentation/testing/lighthouse/lighthouse_index_mobile.png) </details> |
| Profile Page       | 99    | <details><summary>Show Screenshot</summary> ![Profile Page](documentation/testing/lighthouse/lighthouse_user_area_mobile.png) </details> |
| User Edit         | 95    | <details><summary>Show Screenshot</summary> ![User Caves](documentation/testing/lighthouse/lighthouse_user_edit_mobile.png) </details> |
| User Caves          | 92   | <details><summary>Show Screenshot</summary> ![User Edit](documentation/testing/lighthouse/lighthouse_user_caves_mobile.png) </details> |
| Report Dashboard   | 95   | <details><summary>Show Screenshot</summary> ![Report Dashboard](documentation/testing/lighthouse/lighthouse_report_mobile.png) </details> |
| Report Description | 95    | <details><summary>Show Screenshot</summary> ![Report Description](documentation/testing/lighthouse/lighthouse_report_page_mobile.png) </details> |


##### **Code Institute Python PEP 8 Linter**
No major error was detected, aside from indentation and whitespaces. After some refactoring the Python Linter didn't encoutered any erros. 

<details>
<summary>Python Linter</summary>

![Python Linter](docs/documentation/python_linter_final.png)

</details>

### **6.4. Manual Testing**
According to the functions written in the code, these are the input possibilities for satisfying error handling and RegEx requirements. 

| Input Field                    | Example         | Possible Values                                                                                 | Type of input                                                                                |
|--------------------------------|-----------------|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Basin Name                     | b_river_suir_02 | Any string in the format 'b_xxxx_'                                                    	     | String ReGex format limited to 25 characteres                                                              |
| Latitude                       | -20.102852      | Any valid latitude in decimal format                                                            | String ReGex starting with -+ != 0                                                                     |
| Longitude                      | -43.453612      | Any valid longitude in decimal format                                                           | String ReGex starting with -+ != 0                                                                    |
| Area                           | 002.708         | Any positive decimal number                                                                     | String ReGex with 6 digits separated by a dot != 0                                                                          |
| Perimeter                      | 007.289         | Any positive decimal number                                                                     | String ReGex with 6 digits separated by a dot != 0                                                                       |
| Main Course Length             | 001.612         | Any positive decimal number                                                                     | String ReGex with 6 digits separated by a dot != 0                                                                     |
| Basin Length                   | 001.761         | Any positive decimal number                                                                     | String ReGex with 6 digits separated by a dot != 0                                                                           |
| Elevation Outlet               | 0961            | Any positive integer                                                                            | String ReGex with 4 digits separated != 0                                                                 |
| Elevation Spring               | 1378            | Any positive integer                                                                            | String ReGex with 4 digits separated != 0                                                    |
| Elevation Highest              | 1413            | Any positive integer                                                                            | String ReGex with 4 digits separated != 0                                                    |
| Urbanization Level             | 0.64            | Any decimal number between  0 and 1                                                              | Any decimal number between != 0 to 1                                                                            |
| Basin index			 | 2		   | Any string in the format 'b_river_suir_XX'                                                      | Any digit from 2 to 983 (Google Sheets limit)                                                                    |                                                                                   |
| General Information Print Option | b_river_suir_02 | Any string in the format 'b_river_suir_XX'                                                      | Basin name to print general information                                                       |
| Exit Option                    | 'exit'            | 'exit'                                                                                         | exit lowercase                                                                  |
| Confirmation (Yes/No)          | 'y', 'n'           | 'y', 'n'                                                                                       |String y or n lowercase


It should be noted that throughout the development and testing process we tried to insert a series of different values that would be either accepted or rejected. In addition, I tested the dimensional data validation functions and explored the choice loops in order to check for a break. Therefore, with a reasonable number of tests, I did not identify an error in the data entry. 

### **6.3. Bugs & Fixes** 

##### **Bug 01**

Bug: The get_data(dictionary RE_PATTERNS) function gets the Regex expression and returns the first identical value. 
This was an issue because the same Regex patterns were shared with different variables, i.e. Latitude and Longitude.
So even when the Longitude variable was called, the print strings of lat would show up because it was the first identical value in the dictionary.

<details>
<summary>Bug 01</summary>

![Bug 01](docs/documentation/bug_01.png)

</details>

Solution: Refactor the code with two dictionaries so the Regex values and variables intro texts are passed correctly.

##### **Bug 02**

Bug: Although the data entries were valid according to Regex string validation, the inputted data could be inconsistent with real-world data.
Thus, I tried to implement safeguards, such as not allowing the 0 entries, which would make the morphometric indeces invalid. 
Most of them are structured by multiplication and division operations, and allowing 0 as an entry would result in indices resulting in 0.

<details>
<summary>Bug 02</summary>

![Bug 02](docs/documentation/bug_02.png)

</details>

Solution: In this case, I added negative lookahead assertions along with the positive ones (validate the entry type). The first prevents the use of 0 as an entry.
I used Regex Tutorial as a consult material regarding negative and positive lookahead assertions. 
Regex negative and positive lookahead assertions: https://www.regextutorial.org/positive-and-negative-lookahead-assertions.php

##### **Bug 03**

Bug: The structure of get_data(variable_input) was set to append values to the basin dictionary after the input.
Because of the append action would add a value to the existent value of the parameter key, creating a list.
Thus, the validation check functions wouldn't evaluate a True after a False due to the incorrect values in the list.
In addition, adding values and creating a list would render the basin dictionary useless as a primary agroupment of temporary data.

<details>
<summary>Bug 03</summary>

![Bug 03](docs/documentation/bug_03.png)

</details>

Solution: The solution revolved around changing the way data is collected so that the old value would be replaced by a new one.
The possibility to replace data made it possible to run the application correctly, and this was done by updating the input rather than appending the value.
Hence, changing the last part of the snippet where inputs were passed to the basin dict fixed the bug.

<details>
<summary>Bug 03</summary>

![Bug 03](docs/documentation/bug_03_solution.png)

</details>


##### **Bug 04**

bug: After re-entering invalid data more than twice, activating the loop between check_elevation and re_enter_data, even if the entries were validated between themselves
the re-enter variables loop would continue popping the re-enter elevation decision.

<details>
<summary>Bug 04</summary>

![Bug 04](docs/documentation/bug_04_solution.png)

</details>

Solution: The bug was solved closing the outer loop of the re_enter_data function. This Stack Overflow's link help me with the solution.
https://stackoverflow.com/questions/65747924/break-doesnt-break-while-loop-why

##### **Bug 05**

Bug: The check_dimensional_data function wasn't returning properly True if inputs would numerically return true. 

<details>
<summary>Bug 05</summary>

![Bug 05](docs/documentation/bug_05_01.png)


![Bug 05](docs/documentation/bug_05_02.png)


</details>

Solution: By debugging and separating all the conditions, I noticed the bug was connected to the data type.
The data used in the function was a string. When this string was multiplied, it returned a new string instead of a number, leading to the incorrect output. 
So, I added the proper data type to the local variables (float or int).

<details>
<summary>Bug 05</summary>

![Bug 05](docs/documentation/bug_05_solution.png)

</details>

##### **Bug 06**

Bug: When deploying the app to heroku it returned with the critical error: 
Traceback (most recent call last):   File "/app/run.py", line 10, in <module> from terminaltables import AsciiTable, DoubleTable, SingleTable ModuleNotFoundError: No module named 'terminaltables'.

Solution: I indetify the issues was connected to terminaltables and searched online using the terminal message.
I got a answer in https://github.com/LionSec/xerosploit/issues/102, and re-instal terminaltables and a couple other extensions, changing the python version to current.
I pushed my code and re-deployed the app in heroku and those measures solved my bug. 

##### **Bug 07**

Bug: To validate the basin index (Google Sheets index column of the data entered by the user) that connects steps 1 - Data Entry and 2 - Calculate Morphometric Indices, I chose to validate that input is an integer. However, high numbers (> 983) return the error "gspread.exceptions.APIError: APIError: [400]: Range (v_data!A999) exceeds grid limits. Max rows: 983, max columns: 26" and the regex check on column 1 basin_name returned the error TypeError: expected string or bytes-like object, got 'NoneType'

Solution: Thus, I created an if instance that only made valid values less than the Google Sheets limit of 983 rows. In addition, the entry 'NoneType' in the empty cell in column 1 was passed by the string method, which made it possible to check the data via regex.


### **6.4. Unsolved Bugs** 

Maybe it's not a bug, but depending on the size of the strings fetched in the print_morpho_text() function, they can break the justified look of the text. I've tried adjusting the spacing a few times, but the limitations of indentation and 79 characters have made this a difficult task. Apart from that, no other bug was detected during my testing. 
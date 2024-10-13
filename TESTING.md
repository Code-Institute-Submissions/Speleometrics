# Speleometrics | a Collaborative Cave Database

![Speleometrics](documentation/speleometrics.png)

[Visit my website here](https://speleometrics-586df55c9a57.herokuapp.com/)

Return back to the [README.md](README.md) file.

## Testing - Table of Contents  
  
6. [Testing](#testing)
   6.1. [Validation](#61-validation)
      6.1.1. [Html Validation](#html-validation)
      6.1.2. [Performance Lighthouse](#performance-lighthouse)
         6.1.2.1. [Lighthouse Validator Desktop Pages](#lighthouse-validator-desktop-pages)
         6.1.2.2. [Lighthouse Validator Mobile Pages](#lighthouse-validator-mobile-pages)
      6.1.3. [Python PEP 8 Validation](#python-pep-8-validation)
         6.1.3.1. [Python PEP 8 Validator](#python-pep-8-validator)
      6.1.4. [CSS Validation](#css-validation)
   6.2. [Manual Testing](#62-manual-testing)
   6.3. [Bugs & Fixes](#63-bugs--fixes)
      6.3.1. [Bug 01](#bug-01)
      6.3.2. [Bug 02](#bug-02)
      6.3.3. [Bug 03](#bug-03)
      6.3.4. [Bug 04](#bug-04)
      6.3.5. [Bug 06](#bug-06)
      6.3.6. [Bug 07](#bug-07)
   6.4. [Unsolved Bugs](#64-unsolved-bugs)

### **6.1. Validation**

#### **Html Validation**

html validation was conducted through [HTML W3C Validator](https://validator.w3.org). 
The following images are validation screenshots taken from the service with the website Heroku live link. 
 - The validator could not test the pages that required logged in user (profile User Section) superuser credentials (Reports Section) and error pages (500, 403 and 404).
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


##### Lighthouse Validator Desktop Pages
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


##### Lighthouse Validator Mobile Pages
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


#### **Python PEP 8 Validation**
[Code Institute Python PEP 8 Linter](https://pep8ci.herokuapp.com/#) was used, no major error was detected, aside from indentation and whitespaces. After some refactoring the Python Linter didn't encoutered any errors. 

##### Python PEP 8 Validator

| Feature           | admin.py                                                                                                               | forms.py                                                                                                               | models.py                                                                                                               | urls.py                                                                                                                | views.py                                                                                                               |
|-------------------|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Spelometrics      | X                                                                                                                       | X                                                                                                                      | X                                                                                                                      | <details><summary>Show Screenshot</summary> ![Spelometrics urls](documentation/testing/pep8/ci_python_linter_speleometrics_urls.png) </details> | X                                                                                                                      |
| SpeleoStatistics  | X                                                                                                                       | X                                                                                                                      | X                                                                                                                      | <details><summary>Show Screenshot</summary> ![SpeleoStatistics urls](documentation/testing/pep8/speleostatistics/ci_python_linter_speleostatistics_urls.png) </details> | <details><summary>Show Screenshot</summary> ![SpeleoStatistics views](documentation/testing/pep8/speleostatistics/ci_python_linter_speleostatistics_views.png) </details> |
| Profiles          | <details><summary>Show Screenshot</summary> ![Profiles admin](documentation/testing/pep8/profiles/ci_python_linter_profiles_admin.png) </details> | <details><summary>Show Screenshot</summary> ![Profiles forms](documentation/testing/pep8/profiles/ci_python_linter_profiles_forms.png) </details> | <details><summary>Show Screenshot</summary> ![Profiles models](documentation/testing/pep8/profiles/ci_python_linter_profiles_models.png) </details> | <details><summary>Show Screenshot</summary> ![Profiles urls](documentation/testing/pep8/profiles/ci_python_linter_profiles_urls.png) </details> | <details><summary>Show Screenshot</summary> ![Profiles views](documentation/testing/pep8/profiles/ci_python_linter_profiles_views.png) </details> |
| Caves             | <details><summary>Show Screenshot</summary> ![Caves admin](documentation/testing/pep8/caves/ci_python_linter_profiles_caves.png) </details> | <details><summary>Show Screenshot</summary> ![Caves forms](documentation/testing/pep8/caves/ci_python_linter_profiles_forms.png) </details> | <details><summary>Show Screenshot</summary> ![Caves models](documentation/testing/pep8/caves/ci_python_linter_profiles_models.png) </details> | <details><summary>Show Screenshot</summary> ![Caves urls](documentation/testing/pep8/caves/ci_python_linter_profiles_urls.png) </details> | <details><summary>Show Screenshot</summary> ![Caves views](documentation/testing/pep8/caves/ci_python_linter_profiles_views.png) </details> |

#### **CSS Validation** 

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate custom CSS file. No errors or warnings were detected.

<details>
<summary>CSS Validation</summary>

![CSS Validation](documentation/testing/w3c_css_validation_speleometrics.png)
</details>

### **6.2. Manual Testing**


| Feature                                          | Tested? | User Input Required                               | User Feedback Provided                                                                                                                                               | Pass/Fail | Fix |
|--------------------------------------------------|---------|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----|
| Search Caves                                     | Yes     | Search query                                      | Users can search for caves by name, user or dimensions. Results display relevant caves or "No caves found", if no match.                                               | Pass      | -   |
| Cave Page                                        | Yes     | Inconsistency details (optional)                  | Logged-in users can report inconsistencies. Success message shown upon successful report submission, the function is disabled if not logged in . Addiontionally, forbidden page is shown if the user is able to bypass verification.                              | Pass      | -   |
| Add Cave                                         | Yes     | Various fields including image                     | Users receive prompt for required fields. Field validation is done by Regex. Success message displayed upon successful addition of a cave.                                                              | Pass      | -   |
| Edit Cave                                        | Yes     | Various fields including image                     | Users owners or superuses can edit cave information. Success message shown upon successful edit.                                                                                       | Pass      | -   |
| Delete Cave                                      | Yes     | Confirmation button                                | Users owners or superusers can confirm deletion or return to the main page. Success message displayed upon deletion.                                                                          | Pass      | -   |
| User Search Caves                                | Yes     | Search query                                      | Users can search for caves belonging to a specific user. Results display relevant caves or "No caves found" if no match.                                          | Pass      | -   |
| View Profile                                     | Yes     | None                                              | Displays user profile information. If contact email is empty, redirects to edit profile.                                                                             | Pass      | -   |
| Edit Profile                                     | Yes     | Various fields including profile image             | Users receive prompt for email, which is the only required field. Success message displayed upon successful edit.                                                                            | Pass      | -   |
| Map View                                         | Yes     | None                                              | Displays all caves on a map.                                                                                                                                       | Pass      | -   |
| Custom 403 Page                                  | -     | None                                              | Displays a custom 403 error page when access is forbidden.                                                                                                         | -      | -   |
| Custom 404 Page                                  | Yes     | None                                              | Displays a custom 404 error page when a page is not found.                                                                                                         | Pass      | -   |
 

### **6.3. Bugs & Fixes** 

##### **Bug 01**

Description: The edit_profile function returned a NameError "name for form is not defined". This must have happened due to a reference to an undefined variable pointed out to the form in the context. Through some code investigation, I detected that the function was not correctly accessing the instance of the Profile model associated with the logged-in user.

<details>
<summary>Bug 01</summary>

![Bug 01](documentation/testing/bugs/bug_1.png)

</details>

Solution: The solution involved verifying if the function utilized the appropriate instance of the user's profile. This was achieved by modifying the edit_profile function to correctly reference the logged-in user's profile through the correct query set, allowing for the data to be retrieved.

##### **Bug 02**

Description: The browser encountered a NoReverseMatch error when attempting to use the reverse function for the profile URL in Django. This error must have happened because the URL pattern did not match the parameters being passed to the reverse function. 

<details>
<summary>Bug 02</summary>

![Bug 02](ddocumentation/testing/bugs/bug_2.png)

</details>

Resolution: I investigated some former students' git hub repos, and I came to the conclusion that this error was somehow connected to the problem of the user being created by Django All Auth and not being connected later to the Profile database. So, based on Amy Richards's repo, I implemented signals in profile models to ensure that the created users and the future users would have the profile created simultaneously as the user was created. Here is the snippet that I used:

```python
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates a profile for a new user.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Creates a profile for a user created before profile app.
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()

```

##### **Bug 03**

Description: A layout related bug. For unknown reasons, at that time, I could not apply paddings to profile form labels. 

<details>
<summary>Bug 03</summary>

![Bug 03](docs/documentation/bug_03.png)

</details>

Description: A layout related bug. For unknown reasons, at that time, I could not apply paddings to profile form labels.
Solution: I found a thread in stack overflow indicating a solution to the matter. This bug happens because a label is an inline element, and so is not affected by the top and bottom padding. The solution was to transform the labels into block-level elements, thus allowing the padding to have an effect.


##### **Bug 04**

Description: During the customization of the signup form, due to the necessity of making it necessary for the user to provide a valid e-mail address for contact in the profile page, the custom html would return a None placeholder text in the user name's input area. 

<details>
<summary>Bug 04</summary>

![Bug 04](documentation/testing/bugs/bug_4.png)

</details>

Solution: I thought it was a placeholder mistake, but the placeholder name was an indication username. During a call with my mentor, he pointed out that none was returned from value={{ form.username.value }}. This template variable was not important to the signup page, so I ended up removing it.

<details>
<summary>Bug 04 - Solution</summary>

![Bug 04](documentation/testing/bugs/bug_4_solution.png)

</details>

##### **Bug 05**

Description:  I added a modal to confirm deletion actions, but in the mobile versions of website the modal would not appear with the fading effect occupying the entire screen and/or the buttons would not work. 

<details>
<summary>Bug 05</summary>

![Bug 05](documentation/testing/bugs/bug_5.png)

</details>

Solution: Through some code investigation, I concluded that the bug happened in mobile versions because it was connected to the card representation on small screens, which would override the tables on bigger screens. This function consists of a for loop that returns template variables to populate the cave information shown on the screen. The lock of the screen or the freezing fading effect and absence of the modal box happens because the modal if statement was inserted inside the indentation for the loop card. I adjusted the indentation, and the page and modals worked as expected.

##### **Bug 06**

Description: When editing a registered cave it would ask for the user to provide a user, which is an occult field, because this field should not be altered or even filled during cave add; the filling of the field is automatic. I tried to set the user field to not required, and the cave record would return without a user/author. This was unexpected because the edit_caver function would save the user during the editing process (cave.user = user.username), but this did not prevent the empty user outcome. The following screenshot was taken during the debugging section, and the user field was made visible. 

<details>
<summary>Bug 06</summary>

![Bug 06](documentation/testing/bugs/bug_6.png)

</details>

Solution: I refactored the edit_cave function to maintain the user as not required, capture the cave user from the cave model, and pass it through a variable user, which was attributed to the cave.user after the validation of the form. This adjustment corrected the issue.

##### **Bug 07**

Description: The notification modal was displaying empty when refresh or redirect requests were made.

<details>
<summary>Bug 07</summary>

![Bug 07](documentation/testing/bugs/bug_7.png)

</details>

Solution: I detected this bug during testing, and corrected it by inserting a none to the style attribute of the modal. I implemented this by an If statement, if there was no messages mode display is none.



### **6.4. Unsolved Bugs** 

Through my testing, I have not detected critical bugs, but there are three minor issues left unsolved.
They are not bugs per se because they would not hinder the usage of the website.
Two of them are more layout inconsistencies, and the last one is an error message trailing div from the w3c validator.

Unresolved Bug 01 - layout inconsistency on the button to upload button of the cav_map. My system is in pot-br, so the default is displayed in Portuguese, but this will change according to the system's main language. The problem is that the box doesn't follow the theme design of the website. To fix this inconsistency, I would have to customise all the add_cave forms, but all my validation done in the model would have to be inserted again, demanding more time, which I was short. So, I opted not to solve this issue.

<details>
<summary>Bug 01</summary>

![Bug 01](documentation/testing/bugs/unresolved_bug_1.png)

</details>

The second layout inconsistency has to do with the whitespaces displayed in front of the bio text during the editing of a profile.
I looked at it, but I could not find a quick fix. To reach MVP and implement other features, I judged this would not be fixed at this time.


<details>
<summary>Bug 02</summary>

![Bug 02](documentation/testing/bugs/unresolved_bug_1.png)

</details>


The validator w3c html validator pointed out that there was a stray div tag on the page.
I double-checked my code, and there was no indentation problem; there was no layout change as I intended and no loss to the navigability. I suppose this issue concerns the Django's rendering of the page.

<details>
<summary>Bug 03</summary>

![Cave Page](documentation/testing/w3_html/cave_page.png)
</details>

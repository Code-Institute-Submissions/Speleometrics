# Speleometrics | a Collaborative Cave Database

![Speleometrics](documentation/speleometrics.png)

[Visit my website here](https://speleometrics-586df55c9a57.herokuapp.com/)

## Readme - Table of Contents

1. [Introduction](#1-introduction)

2. [UX Design](#2-ux-design)

    2.1. [Strategy](#21-strategy)

    2.2. [User Stories](#22-user-stories)
    
    2.3. [Flow Chart](#23-flow-chart)

    2.4. [Data Model](#24-data-model)

    2.5. [Design](#25-design)

3. [Features](#3-features)

    3.1. [Existing Features](#31-existing-features)

    3.2. [Future Features](#32-future-features)

4. [Technologies Used](#4-technologies-used)

    4.1. [Languages Used](#41-languages-used)

    4.2. [Frameworks, Libraries & Programs Used](#42---frameworks-libraries-technologies--programs-used)

5. [Testing](#5-testing)

6. [Deployment](#6-deployment)

    6.2. [Forking the Github Repository](#61-deploying-via-heroku)

    6.1. [Github Pages](#62-github-pages)

    6.3. [Making a Local Clone](#63-making-a-local-clone)

7. [Credits](#7-credits)


## **1. Introduction**

Aiming to reconcile my academic background in Geography (bachelor's degree) and newly acquired coding skills, I propose a collaborative platform to house speleological data from the Quadrilátero Ferrífero region, where I worked as an environmental consultant for 12 years.

This platform has statistical, database search, and webGIS features that are engaging and collaborative. The site aims for precision and reliability in recording speleological information, confers transparency and promotes the free flow of information. 

The first issue in designing the website, after deciding on the problem statement, in my creative process is the name of the web application. The site’s name comes from a linguistic accident in my poor or literal translation of what I know in Portuguese as 'espeleometria,' a widely used term, into English, resulting in 'speleometric,' which is actually more commonly known in English as 'cave metrics.' I added an 's' at the end because I thought the name sounded better. During the deployment process on Heroku, I was happy to discover that my fortunate accident is an unregistered name on the platform.

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

## **2. UX Design**

### **2.1. Strategy/Scope and Structural Plane**

My choice for this project is guided, above all, by access to information. In recent years, I have worked on speleological studies in which the metrics of caves can, by a small statistical margin, preserve them or allow them to be suppressed. In a scenario in which economic interest conflicts with the preservation of speleological heritage, given that the genetic process of caves is the same as the concentration of high iron content, forming iron ore deposits, every decision must be grounded (pun intended) by the most complete and high-quality cave data.

In recent years, environmental agencies have tried to generate and maintain a reliable database of caves in the state of Minas Gerais. However, this database only contains spatial data on the caves and does not provide metric data. 

In addition, different environmental studies list different and non-centralized data. This may be due to developers' (mining companies) unwillingness to share information, given the possibility of changes in cutting metrics and losing more deposits. Finally, one could point to a market reserve of specialized consulting companies, which creates a market reserve in possession of a comprehensive database. 

In order to break away from the practices listed in the previous paragraphs and ensure the constitutional right to request and obtain information from government bodies as granted by the Freedom of Information Act, I conceived of this web application. Integrating a database will make the process more transparent and accessible to all stakeholders, contributing to the proper management of speleological heritage.

Speleometrics aims to create a centralized, transparent platform for gathering and sharing cave metrics specific to the Quadrilátero Ferrífero region. This platform will serve various stakeholders—speleologists, conservationists, environmental consultancy companies, public agencies, academics, and cave enthusiasts—by providing accessible and accurate data on caves. The user-friendly dashboard will offer insights into key cave attributes (such as length, depth, area, volume and others), helping in decision-making for environmental licensing, conservation, and research.

In sum the website aims for:
- Allowing input, update, display, and storage of cave metrics data.
- The data should be accessible by all listed stakeholders.
- To provide a user-friendly dashboard to the users, displaying cave metrics specific to the Quadrilátero Ferrífero region.

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

### **2.2. User Stories**

1. User Story (main ideia of the app):
As an admin, I want to create a platform that would provide basic cave metrics to speleologists, conservationists, environmental consultancy companies, public agencies, academics, and cave enthusiasts so that I can centralize and make public and transparent the acquisition of cave metrics data in the Quadrilátero Ferrífero region.
Acceptance Criteria:
- The platform allows input, update, display, and storage of cave metrics data.
- Cave metrics should be accessible by all listed stakeholders.
- To provide a user-friendly dashboard to the users, displaying cave metrics specific to the Quadrilátero Ferrífero region.

2. User Story:
As a user, I want to consult the database, so that I can check on the mean relevance metrics of the Quadrilátero Ferrífero Speleological unit and its Geomorphological Units.
Acceptance Criteria:
- Provide a user-friendly dashboard on the index page to the users.
- Display in feature manner cave metrics specific to the Quadrilátero Ferrífero region (All Data) and the Geomorphological Unit that make up the aforementioned speleological unit (filter by a field)
- Clear representation of metrics through charts, tables, etc.
Specific parameters can filter data (e.g., cave name, size).

3. User Story:
As a user, I want to consult data and general info of a cave, so that I can quickly collect relevant cave information for conservation/environmental licensing purposes.
Acceptance Criteria:
- Users can search for caves by name, location, or other identifiers.
- Users can access a specific info page, “/cavename,” displaying all the collected data available about said cave.
- The cave info page provides relevant data: location/coordinates, physical dimensions, and other textual data.
- Downloadable cave maps (PDF) and images (jpg, png, etc) are available.

4. User Story:
As a user, I want to consult the listing of all caves in the database using filters, so that I can access data according to my own needs, given that it has several different criteria.
- A summary page listing the database caves for quick consultation.
- Allow user to request data through filters such as dimension criteria, author, Geomorphological Unit

5. User Story:
As a user, I want to know in which class of percentile my (or a particular) cave is classified according to percentiles of cave metrics, so that I can have some pointers on the cave’s relevance according to its metrics.
Acceptance Criteria:
- The info page will display a score for cave metrics regarding the speleological and geomorphological units.
- The percentiles must be up to date with the last insertion/deletion of registered caves.

6. User Story:
As a user, I want to verify caves near a target area through a map interface, so that I can spatially assess existing caves quickly and easily.
Acceptance Criteria:
- A map interface must be implemented where users can search for caves by navigating the map frame.
- The map should provide clickable cave icons that would display summarised cave data.
- Display the Geomorphological and Speleological Units.

7. User Story:
As a user, I want to, through the map, open the cave info page, so that I can quickly gather info from the clicked feature.
Acceptance Criteria:
- Clicking on a cave marker in the map interface opens the specific cave info page.
- The info page should not stop the navigation in the map interface.

8. User Story:
As a user, I want to register caves that I have surveyed, so that I can add to the overall metrics and contribute to the speleological knowledge of the region.
Acceptance Criteria:
Users can submit new cave entries through a form that includes required fields, as stablished by the database model.
- Admin reviews and approves user-submitted cave data before it is added to the public database.
- The users are notified upon successful submission and approval.
- Users can upload cave maps (PDF) and images during registration.

9. User Story:
As a user, I want to check the data input on my registered caves, so that I can ensure the entered data is correct and up to date.
Acceptance Criteria:
- Users have access to a personal dashboard listing the caves they have registered.
- Users can review and edit data on their registered caves.
- Any edits or updates to registered caves must be approved by an admin before incorporation of data to the database.

10. User Story:
As a user, I want to report inconsistent data (typos) or suggest updates on the data of caves not registered by me, so that I can contribute to the overall quality of the database.
Acceptance Criteria:
- Users can flag inconsistent data or suggest updates on any cave information.
- A notification is sent to admins for review and approval of suggestions.
- Users receive confirmation regarding the status of their reports.
- A comment area and submit button should be available on each cave info page for submitting such reports.

11. User Story:
As a user, I want to get in touch with other users, so that I can message them directly and ask for further material or information about a cave.
Acceptance Criteria:
- The platform provides user profile pages.
- The platform offers private messaging or contact functionality between users.
- Users must share contact details for further communication.

12. User Story:
As an admin, I want to follow up via external notification (email) with report inconsistency requests by users, so that I can guarantee the current update and maintain a consistent database.
Acceptance Criteria:
- Admins receive notifications of flagged or reported data inconsistencies via email.

13. User Story:
As an admin, I want to manage user accounts, especially disabling user profiles due to misuse of the website functionalities, so that I can maintain control over the information provided by the website.
Acceptance Criteria:
- Admin can view and manage user profiles from the admin panel.
- Admins can disable, delete, or temporarily suspend user accounts based on misuse.
- The admin can restore disabled accounts and track account management history.

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

### **2.3. Skeleton & Surface Planes**

#### Wireframes

The wireframes were created using Balsamiq. At this stage, along with the user stories, it was possible to identify the functionalities, pages, and data to be presented in later phases. 

Although the design is simple, comparing the final result with the wireframes shows that the production phase successfully implemented what was proposed at the outset.

<details>
<summary>Home Desktop</summary>

![Home Desktop](documentation/wireframes/index.png)

</details>

<details>
<summary>Home Mobile</summary>

![Home Mobile](documentation/wireframes/index_mobile.png)

</details>


<details>
<summary>Profile Desktop</summary>

![Profile Desktop](documentation/wireframes/user_profile.png)

</details>

<details>
<summary>Profile Mobile</summary>

![Profile Mobile](documentation/wireframes/profile_mobile.png)

</details>


<details>
<summary>About Desktop</summary>

![About Desktop](documentation/wireframes/about.png)

</details>

<details>
<summary>About Mobile</summary>

![About Mobile](documentation/wireframes/about_mobile.png)

</details>

<details>
<summary>Map Search Desktop</summary>

![Map Search  Desktop](documentation/wireframes/map_search.png)

</details>

<details>
<summary>Map Search Mobile</summary>

![Map Search Mobile](documentation/wireframes/cave_map_mobile.png)

</details>

<details>
<summary>Table Search Desktop</summary>

![Table Search  Desktop](documentation/wireframes/cave_search.png)

</details>

<details>
<summary>Table Search Mobile</summary>

![Table Search Mobile](documentation/wireframes/cave_search_mobile.png)

</details>


<details>
<summary>Add cave Desktop</summary>

![Add cave  Desktop](documentation/wireframes/add_cave.png)

</details>

<details>
<summary>Add cave Mobile</summary>

![Add cave Mobile](documentation/wireframes/add_cave_mobile.png)

</details>

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

#### Datbase Schema

The cave registration system was structured using a relational database schema which the models are: User, Profile, Cave, and Report. The models are connected by relationships defined through foreign key associations. User is structured by Django AllAuth, a set of applications that automate tasks related to addressing authentication, registration, and account management.

The Cave, which stores the main data collected by the website, is linked to the User model via a foreign key, establishing that each cave entry is created and managed by a specific user, ensuring ownership of cave records. The Cave model includes fields like cave_name, latitude, longitude, elevation, length, depth, area, and volume, each with specific validation constraints to ensure consistency in data entry.

The Profile model, in turn, is associated with the User model through a one-to-one relationship established by the user. This allows each user to have a detailed profile while maintaining the core authentication provided by Django All Auth. Additionally, the Profile model handles user information, allowing them to edit their profile and access the website's main functions, like adding a cave, provided the user provides an email_for_contact, bio, and display name, which are not mandatory fields. This relationship ensures the integrity of user data, connecting it back to cave entries and reports through consistent foreign key relationships across the models.

Finally, The Report model captures the relationship between users and cave entries in terms of data inconsistencies. A report gathers info about the reporting user, the cave being reported, the cave owner, and the inconsistency. This is managed through foreign keys that ensure each report correctly maps out the cave and the users involved. 

![Speleometrics - Data Schema](documentation/speleometrics_data_model.png)

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

### **2.4. Design** 

For the page design, I drew inspiration from the interface I used most often while preparing environmental impact reports, which in this case was Microsoft Word. The blank page in the centre with grey borders would bring comfort to the centred content and familiarity to users, most of whom share a similar professional background to mine.

As for the logo, it went through several versions and colours. After testing a few possibilities, one of which was my user profile photo, I decided on something more elemental and simple. The capital greek letter omega is commonly used as a cartographic symbol to designate a cave, and this was present in several versions of the logo. Regarding the colour, I chose orange, as it resembles the soil developed from the rocks of the Quadrilátero Ferrífero.

<details>
<summary>Orange Soil</summary>

![Orange Soil](documentation/orange.png)

</details>

<details>
<summary>Word Blank Page</summary>

![Word Blank Page](documentation/word_blank_page.png)

</details>

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

#### Colour Scheme

I chose a palette that would ornate with orange, white, and grey for the colour scheme that inspired the site's design. Since much of the content will be presented through text and tables, to maintain a clean appearance, I decided to choose a dark tone for the text. To that end, I checked the accessibility of a dark blue shade and a white tone. I opted out of shades of grey or black for this purpose, as I found the dark blue tone more elegant.


![Colour Palette](documentation/color_palette.png)

<details>
<summary>Colour Text</summary>

![Colour Text](documentation/color_text_contrast.png)

</details>

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

#### Font

I chose Josefin Sans for the items in the nav-bar and Inter Sans for the rest of the text.

### **2.4. Agile and Project Managing** 

I tried to implement Agile Methodology during the planning of my full stack framework project. The planning was conducted with [GitHub Project](https://github.com/users/hpesciotti/projects/3). I chose to limit my entries to Tasks, User Stories, linking them through GitHub interface. 

I had initially around 30 days to execute the project, as suggest by the CI Scheduler. I would like to point out that was a very short time frame to develop a full-stack application and taking into account my learning curve with Django and Boostrap, I think the endproduct can achive the MVP status. 

Here is a draft of my initial planning divided um four sprints, tackling the various content involved on Speleometrics.

| Sprint | Start       | Finish      | Content                                    |
|--------|-------------|-------------|--------------------------------------------|
| 1      | 15/09/2024  | 21/09/2024  | Design, Wireframes, Sign-In (Django AllAuth) |
| 2      | 22/09/2024  | 28/09/2024  | Defining the models, Profiles and Caves    |
| 3      | 29/09/2024  | 05/10/2024  | Statistics, Reports, Maps and Frontend Development |
| 4      | 06/10/2024  | 13/10/2024  | Styling/Testing/Documentation               |

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

### **3. Features**

#### **3.1. User view**

To ensure an engaging interface and data protection, it was necessary to establish some permissions for the website users.
Moreover, the classification of users reflects upon the user's access to some pages. 
The following charts show the accessibility of the features per user type.

| Feature / User Type       | Unlogged User | Logged User | Superuser |
|---------------------------|---------------|-------------|-----------|
| **Home**                  | Visible       | Visible     | Visible   |
| **About**                 | Visible       | Visible     | Visible   |
| **Caves**                 |               |             |           |
| - Map Search              | Visible       | Visible     | Visible   |
| - Table Search            | Visible       | Visible     | Visible   |
| - Cave Page               | Visible       | Visible     | Visible   |
| - Report Cave             | Not Visible    | Visible     | Visible   |
| **User Area**             |               |             |           |
| - Register a Cave         | Not Visible    | Visible     | Visible   |
| - My Caves                | Not Visible    | Visible     | Visible   |
| - Edit Cave               | Not Visible    | Visible     | Visible   |
| - Edit Profile            | Not Visible    | Visible     | Visible   |
| **Reports**               |               |             |           |
| - Report List             | Not Visible    | Not Visible  | Visible   |
| - Report Page             | Not Visible    | Not Visible  | Visible   |

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

#### **3.2. CRUD Functionality**

The Create, Read, Update, Delete (CRUD) functionalities are planned for Speleometrics. Through the Database Model, it is clear that full CRUD functionality is available for the Cave database, meaning that any user who has registered a cave and a superuser has access to Create, Read, Update, and Delete operations. Regarding user profiles, the only operation currently unavailable is the ability to delete them. Since cave records are crucial to the web application's purpose, deleting profiles could result in data loss (cascade effect). Therefore, the option to delete a profile was not initially planned. Additionally, as transparency is a guiding principle of the project, most functionalities are available in Read mode, even for users who are not logged in. The following chart displays the CRUD functions per page per user.

| Feature / User Type       | Unlogged User | Logged User           | Superuser         |
|---------------------------|---------------|-----------------------|--------------------|
| **Home**                  | R             | R                     | R                  |
| **About**                 | R             | R                     | R                  |
| **Cave**                  |               |                       |                    |
| - Table Search            | R             | R                     | R                  |
| - Cave Page               | R             | All = R - If owner = U, D | R, U, D          |
| - Report Cave             | R             | C                     | C                  |
| **User Area**             |               |                       |                    |
| - Register a Cave         | R             | C                     | C                  |
| - My Caves                | R             | U, D                  | R, U, D            |
| - Edit Cave               | R             | If owner = U else -  | U                  |
| - Edit Profile            | R             | All = R / If owner = U | All = R / If owner = U |
| **Reports**               |               |                       |                    |
| - Report List             | -             | -                     | R, D               |
| - Report Page             | -             | -                     | R, D               |

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

### **4.1. Features Showcase**

#### Header

The header features two versions tailored for both mobile and desktop views. Both versions include the site's logo, which has hover and focus functions aligned with the adopted colour scheme. The logo follows current trends by maintaining a minimalist design.

In the desktop version, links are presented as nav-pills, responsive to hover, focus, and active states. The purpose of the nav-pills is to effectively indicate the section or area of the site being accessed. It is important to note that the "add cave" section, which depends on user validation and is accessed through the user area, sits between the cave and user area tabs.

The navbar is also responsive to user type. When the user is not logged in, the user area is visible but appears as disabled, prompting the user to log in or sign up. Additionally, only superusers can access the reports tab, which remains invisible to other users.

The mobile version includes the logo and stack bars for the drop-down menu. This version lists the sublinks under the Caves section directly without requiring additional clicks. Similar to the desktop version, the responsiveness to the user's status is also applied.


![Nav Bar](documentation/showcase/nav_bar.png)

<details>
<summary>Nav Bar Effects</summary>

![Nav Bar Effects](documentation/showcase/nav_bar_effects.png)

</details>

<details>
<summary>Nav Bar Privileges - Desktop</summary>

![Nav Bar Privileges - Desktop](documentation/showcase/nav_bar_privliges.png)

</details>

<details>
<summary>Nav Bar Privileges - Mobile</summary>

![Nav Bar Privileges - Mobile](documentation/showcase/nav_bar_privliges_mobile.png)

</details>

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

#### Footer

I decided not to insert relevant website information in the footer.
Instead, I inserted Font Awesome links to GitHub and LinkedIn.
The footer is very minimalistic, almost imperceptible, as intended.

![Footer](documentation/showcase/footer.png)

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

#### Home / Index page

The home/index page is comprised of three distinct elements: the hero image, the call-to-action banner linked to a sign-in button (which switches to user area if the user is logged in), and the Cave Metrics section.

The hero image is represented by a panoramic photograph of the Serra do Curral, one of the geomorphological units included in the registry. This range features the Quadrilátero Ferrífero's quartzite and ironstone-supported ridges, with most of the region's cavities attributed to the latter. The hero image serves to create visual appeal. In the mobile version, this image is responsive and centers on one of the mountain peaks.

The call-to-action banner aims to inform users about the purpose of the site and intuitively encourage them to register via the button. The text succinctly explains the website's main goals.

![Hero Image and Banner](documentation/showcase/hero_image.png)

![Hero Image and Banner](documentation/showcase/hero_image_mobile.png)

Finally, the Cave Metrics section provides statistical data on cavity records, both for the entire Quadrilátero Ferrífero region and the geomorphological units it comprises. This section serves as a valuable reference point for a preliminary assessment of significance. Magnitude ratios are essential for project planning that may affect the speleological heritage. Additionally, these metrics can be integrated into environmental studies without the time-consuming process of consolidating and calculating data, as they are easily accessible through the web application. In the backend, those statistics are run every time there's a request to update the page. I opted not to create a database for this function because this information is dynamic, and there was no need for early optimization as the page's loading time was fast.

![Cave Metrics](documentation/showcase/qf_statistics.png)

The section also includes the total number of caves and those recorded in each geomorphological unit. To ensure greater readability and minimize confusion among the tables, the units are embedded within an accordion. In the mobile version, tables have the overflow-x: scroll attribute for screens smaller than 300px, facilitating the reading of presented values.

![Cave Metrics](documentation/showcase/accordion_geomorphological_units.png)

![Cave Metrics](documentation/showcase/qf_accordion_geomorphological_units_mobile.png)

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

#### Cave Map Search

The page offers a GIS interface through the Leaflet tool, where users can view the location of caves marked with a custom icon. Clicking on the icon triggers a pop-up displaying general information about the cave, with the cave and user names hyperlinked to their respective individual pages. The page also features a composite altimetry basemap with varying scales, using data from SRTM and even IBGE.

Cave locations are displayed by a function that iterates through all records and returns the geographical coordinates of each cave for the map. In the credits section, links are provided to resources that guided the integration of Django elements into JavaScript functions.

Additional filters can be implemented on this page to optimize the loading speed, but to reach the MVP, such functionalities have been postponed as future features. Nevertheless, the main acceptance criteria for this feature were achieved. To fulfil the requirements of User Story [#6](https://github.com/hpesciotti/Speleometrics/issues/6), a new tool needed to be used, probably ArcGIS web, which would take a long time to implement. I guess the original scope was too convoluted. 

![Map Search Mobile](documentation/showcase/map_search_desktop.png)

![Map Search Mobile](documentation/showcase/map_search_mobile.png)

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

#### Table Search

The Cave Search allows users to search by exact term, name, or author, or to list caves in ascending and descending order based on metric parameters. This functionality was challenging to implement, and I based it on the work of Joy Zadan (PP5). 

This page offers two distinct versions for cave listing. The search results are displayed in a table on larger screens, while on smaller resolutions, the caves are presented as cards. This approach ensures that search results are easily interpretable on mobile devices. 

As shown on the map page, users can access the specific cave and user pages via hyperlinks. Clicking the links opens the desired page in a new browser tab, allowing users to continue their search seamlessly. Lastly, this page offers options to edit and delete data if accessed by a superuser.

![Cave Search Desktop](documentation/showcase/table_search_user_desktop.png)

<details>
<summary>Cave Search Desktop Privileges - Mobile</summary>

![Cave Search Desktop Privileges - Mobile](documentation/showcase/table_search_admin.png)

</details>

![Cave Search Mobile](documentation/showcase/table_search_mobile.png)

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

#### About

The About page is the most straightforward page on the site, consisting solely of text and static images. 
Its purpose is to provide general information about the studied area, caves, and environmental licensing, especially regarding the relevance and speleological metrics. At the bottom of the page are external links with the `noopener` attribute to official sources on the topic.

![About Desktop](documentation/showcase/about_desktop.png)

![About Mobile](documentation/showcase/about_mobile.png)

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

#### Profile

The Profile page includes several checks to ensure the user has filled in their contact email. The contact email is essential for user interaction when requesting information, as described in user stories #10 and #11. On first access, the user is redirected to the profile edit page. After filling it in, users can access the pages to add caves, check their registered caves, or edit their user profile.

![Profile Page - Image](documentation/showcase/profile_page_custom_image.png)

<details>
<summary>Profile Page - No Image</summary>

![Profile Page - No Image](documentation/showcase/profile_page_no_picture.png)

</details>

<details>
<summary>Profile Page - Not logged in</summary>

![Profile Page - Not logged in](documentation/showcase/cave_page_not_logged_in.png)

</details>

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

#### My Caves

Through the profile, users can access "My Caves," which returns their registered caves. The interface is similar to the table search, offering users the option to open individual cave pages, edit the caves, and delete the records. In mobile mode, the table view switches to cards for better presentation.


![Profile Page - Not populated](documentation/showcase/profile_page_my_caves_populated.png)

<details>
<summary>Profile Page - Not populated</summary>

![Profile Page - Not populated](documentation/showcase/profile_page_my_caves.png)

</details>

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

#### Add Cave / Cave Edit

The "Add Cave" feature is authorized for users whose profiles have a contact email. The function that renders this page checks if the user is logged in (`@login_required`) and if they are the owner of the cave (`profile_user = get_object_or_404(User, username=username)` and `profile = get_object_or_404(Profile, user=profile_user)`). 

The form responsible for adding a cave includes required fields such as `cave_name`, `latitude`, `longitude`, `elevation`, `length`, `depth`, `area`, and `volume`, all of which undergo validation, including Regex checks, to ensure consistent data. If the user fills out a field incorrectly, the form returns a custom alert message indicating where the error occurred. It's worth mentioning that despite the option to upload a cave map, no maps have been added to the current cave records (although one appears in the screenshots). This is because materials such as cave sketches and photos are often provided to mining companies under non-disclosure agreements, which unfortunately prevents me from attaching such data at this time. Lastly, the same form used in `cave_add` is also utilized for editing cave data (`cave_edit`), but the function that renders it retrieves the cave data and populates each field accordingly.

Through the profile, users can access "My Caves," which returns their registered caves. The interface is similar to the table search, offering users the option to open individual cave pages, edit the caves, and delete the records. In mobile mode, the table view switches to cards for better presentation.


![Register Cave](documentation/showcase/register_cave.png)

<details>
<summary>Register Cave - No Filled</summary>

![Register Cave - No Filled](documentation/showcase/register_cave_wont_proceed.png)

</details>

<details>
<summary>Register Cave - Error</summary>

![Register Cave - Error](documentation/showcase/register_cave_error_notifications.png)

</details>


[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)


#### Cave Page

The cave page consists of a simple layout where the data is presented individually in a textual format. On this page, the owner of the cave has the option to delete it. Conversely, any user can submit a report for inconsistencies. This report is submitted through a modal equipped with a text box where the reporting user only needs to fill in the specific inconsistency found in the data. The other data points, such as `cave`, `reported_by`, `cave_owner`, and `reported_created_date`, are automatically collected.

![Cave Page](documentation/showcase/cave_page_not_logged_in.png)

<details>
<summary>Cave Page - Notification</summary>

![Cave Page - Notification](documentation/showcase/cave_page_notitification.png)

</details>

<details>
<summary>Cave Page - Delete Modal</summary>

![Cave Page - Delete Modal](documentation/showcase/delete_cave_modal.png)

</details>

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

#### Report

The report page is restricted to superusers. Its purpose is to list records with inconsistent data. This page includes filtering options to allow site administrators to organize review requests and provide the necessary follow-up. Each item can be viewed separately using the "Detail" button. 

At the end of the review process, the admin can delete the review request. At this stage of the website, there is no automated way for the user to track if their report request has been addressed, except through email communication from the administrator.


![Report](documentation/showcase/report.png)


![Report Page](documentation/showcase/report_page.png)


[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)


#### Sign In Page

The sign In page is supported by Django AllAuth model. 
I added some personalisation to return erro messages.

![SignIn Validation 1](documentation/showcase/sign_in_validation.png)


![SignIn Validation 2](documentation/showcase/sign_in_validation_2.png)


[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)


## **4. Technologies Used**

### **4.1. Languages Used**

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

- [Python](https://www.python.org/about/)

- [JavaScript](https://www.javascript.com/)

[Back to top](//github.com/hpesciotti/Speleometrics/blob/main/README.md)

### **4.2 - Frameworks, Libraries, Technologies & Programs Used**  

- [Gitpod](https://www.gitpod.io): used form coding

- [GitHub](https://github.com/): to save and store all files for this web application 

- [Git](https://git-scm.com/): used for version control

- [Django](https://www.djangoproject.com/): for building the web application

- [Regex](https://www.w3schools.com/python/python_regex.asp): for checking for pattern in strings.

- [Google Fonts](https://fonts.google.com/): font was imported from here 

- [Font Awesome](https://fontawesome.com/): icons and their associated kit were downloaded from here  

- [Leaflet](https://leafletjs.com/examples.html): an open-source JavaScript library for mobile-friendly interactive maps, especially the tutorials section on how to how to add a marker and set custom style for the marker.

- [Numpy](https://numpy.org/): for running the statistics

- [Cloudinary](https://cloudinary.com/): for storing images (cave-maps and profile pictures)

- [Microsoft Power Point](https://www.lucidchart.com/pages/?): used to create data chart and logo

- [ChatGPT](https://chat.openai.com/): for improving and making text content more engaging.

- [ArcGIS](https://www.arcgis.com/index.html): to build the QF geomorphological units map.

- [Grammarly](https://app.grammarly.com): for spelling or grammatical inaccuracies in the text

- [Google Chrome Lighthouse](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk): for auditing the performance of the web application

- [Code Institute Linter](https://pep8ci.herokuapp.com/#): for validating Python code according PEP 8

- [MS Paint](https://www.microsoft.com/en-us/windows/paint): for editing the captured screenshots

- [Heroku](https://dashboard.heroku.com/): for deploying the terminal application.

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

## **5. Testing**

- An additional file for Testing can be found here: [Testing](https://github.com/hpesciotti/Speleometrics/blob/main/TESTING.md)

## **6. Deployment**

The website was developed using Gitpod code editor, committed to Git as a local repository, and then pushed to GitHub for storage.

## **6.1 Code Institute PostgreSQL Database *

- Navigate to [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net/)
- Enter your student email address in the input field provided.
- Wait for database to be created and review the email sent to your student email inbox.

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)

### **6.2. Connecting to GitHub**

To begin this project from scratch, you must first create a new GitHub repository using the [Code Institute's Template](https://github.com/Code-Institute-Org/ci-full-template). This template provides the relevant tools to get you started. To use this template:

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above CI Full Template.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In Gitpod locate your repository and create a new workspace.

[Back to top](//github.com/hpesciotti/Speleometrics/blob/main/README.md)

### **6.3. Django Project Setup**

- Install Django and all supporting libraries for Speleometrics: 

```
pip install asgiref==3.8.1
pip install cloudinary==1.36.0
pip install dj-database-url==0.5.0
pip install dj3-cloudinary-storage==0.0.6
pip install Django==4.2.16
pip install django-allauth==0.57.2
pip install django-resized==1.0.2
pip install django-summernote==0.8.20.0
pip install gunicorn==20.1.0
pip install numpy==2.1.2
pip install oauthlib==3.2.2
pip install pillow==10.4.0
pip install psycopg2==2.9.9
pip install PyJWT==2.9.0
pip install python3-openid==3.2.0
pip install requests-oauthlib==2.0.0
pip install sqlparse==0.5.1
pip install urllib3==1.26.20
pip install whitenoise==5.3.0
```
  
- After the insatalation process run ```pip3 freeze --local > requirements.txt``` in the terminal.  
- Create a new Django project in the terminal ```django-admin startproject speleometrics .```
- Create a new app eg. ```python3 mangage.py startapp caves```
- Register caves in **INSTALLED_APPS** in **settings.py** as 'caves',
- Run ```python3 manage.py createsuperuser``` and enter credentials to create a superuser, allowing Admin access.
- Run migrations with commands: ```python3 manage.py makemigrations``` and ```python3 manage.py migrate```
- Create an **env.py** to store all confidential data such as the **DATABASE_URL** and **SECRET_KEY**. 

```import os
os.environ["DATABASE_URL"]="<CI's data base>"
os.environ.setdefault("CLOUDINARY_URL")
```

- Add envy.py to must be added to your **gitignore**, so it will not be upload to GitHub.
- Reference the file in your project's **settings.py**: 
For adding to **settings.py**:

```
import os
import dj_database_url
if os.path.exists("env.py"):
import env
```

- Replace **DATABASES** with:

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
```

- Set up the templates directory in **settings.py**:
    Under ``BASE_DIR`` enter ``TEMPLATES_DIR = os.path.join(BASE_DIR, ‘templates’)``
    Update ``TEMPLATES = 'DIRS': [TEMPLATES_DIR]`` with:

```
os.path.join(BASE_DIR, 'templates'),
os.path.join(BASE_DIR, 'templates', 'allauth')
```

- Create the media, static and templates directories in top level of project file in IDE workspace.

-  Create a Procfile in the project repository for Heroku deployment, containing the following line:
web: gunicorn speleometrics.wsgi

-  Run migrations again to ensure all database changes are applied.

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)


### **6.4. Cloudinary API**

Cloudinary offers a cloud-based solution for media storage. All images uploaded by users in the Speleometrics project are hosted on this platform.

To get started, create a new account at Cloudinary and add your Cloudinary API environment variable to your env.py file and Heroku Config Vars. In your project workspace:
  - Include the Cloudinary libraries in the INSTALLED_APPS section of your settings.py file, in the following order:
```
   'cloudinary_storage',  
   'django.contrib.staticfiles',  
   'cloudinary',
```
- Add to **env.py** and link up with **settings.py**: ```os.environ["CLOUDINARY_URL"]="cloudinary://...."``` 
- Configure Cloudinary as the storage for media and static files in settings.py with the following settings:

```
STATIC_URL = '/static/
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'  
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]  
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')‌  
MEDIA_URL = '/media/'  
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```
[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)


### **6.5.  Heroku Deployment**

To start the deployment process , please follow the below steps:

- Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
- Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
- Enter an app name and choose your region. Click '**Create App**'. 
-  In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. The KEY:VALUE pairs that you will need are your: 
   
   - Set CLOUDINARY_URL** 
   - Set DATABASE_URL**
   - Set DISABLE_COLLECTSTATIC to 1
  
- Add the Heroku host name into **ALLOWED_HOSTS** in your projects **settings.py file** -> ```['herokuappname', ‘localhost’, ‘8000 port url’].```
- Once you are sure that you have set up the required files including your requirements.txt and Procfile, you have ensured that **DEBUG=False**, save your project, add the files, commit for initial deployment and push the data to GitHub.
- Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
- Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
-  Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Manual' deployment method. Click '**Deploy Branch**'.
- Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site. If you receive any errors, Heroku will display a reason in the app build log for you to investigate. *

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)


### **6.5.  Clone Project**

A local clone of this repository can be made on GitHub. Please follow the below steps:

- Navigate to GitHub and log in.
- The [Speleometrics](https://github.com/hpesciotti/Speleometrics/) can be found at this location.
- Above the repository file section, locate the '**Code**' button.
- Click on this button and choose your clone method from HTTPS, SSH or GitHub CLI, copy the URL to your clipboard by clicking the '**Copy**' button.
- Open your Git Bash Terminal.
- Change the current working directory to the location you want the cloned directory to be made.
- Type `git clone` and paste in the copied URL from step 4.
- Press '**Enter**' for the local clone to be created.
- Using the ``pip3 install -r requirements.txt`` command, the dependencies and libraries needed for FreeFido will be installed.
- Set up your **env.py** file and from the above steps for Cloudinary and ElephantSQL, gather the Cloudinary API key and the Elephant SQL url for additon to your code.
- Ensure that your **env.py** file is placed in your **.gitignore** file and follow the remaining steps in the above Django Project Setup section before pushing your code to GitHub.

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)


### **6.6.  Clone Project**

A copy of the original repository can be made through GitHub. Please follow the below steps to fork this repository:  

- Navigate to GitHub and log in.  
- Once logged in, navigate to this repository using this link [Speleometrics](https://github.com/hpesciotti/Speleometrics/).
- Above the repository file section and to the top, right of the page is the '**Fork**' button, click on this to make a fork of this repository.
- You should now have access to a forked copy of this repository in your Github account.
- Follow the above Django Project Steps if you wish to work on the project.

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)


## **7. Credits**

### **7.1. Content**

- Code Institute - I think there for I Blog project: Django walkthrough project.

- [RegexTutorial](https://www.regextutorial.org/positive-and-negative-lookahead-assertions.php): reading material on negative and positive lookahead assertions

- [W3Schools](https://www.w3schools.com/python/python_regex.asp): for Regex reading material.

- [Regex Calculator](https://regex101.com/): for testing and implementing Regex

- [Django Docs](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.readonly_fields): For general info on Django functionalites

- [Leaflet](https://leafletjs.com/examples.html): an open-source JavaScript library for mobile-friendly interactive maps, especially the tutorials section on how to how to add a marker and set custom style for the marker.

- [D3noob GitHub page](https://gist.github.com/d3noob/9150014): how to add multiple points to leaflet div's map.

- [Leaflet Basemap Previw](https://leaflet-extras.github.io/leaflet-providers/preview/): To pick a basemap for cave_maps page.

- [Geographic Information Systems](https://gis.stackexchange.com/questions/184125/alternative-basemaps-for-leaflet): for info on alternative basemaps for Leaflet.

- [appsbd](https://appsbd.com/how-to-create-map-using-leaflet-js-best-way-to-figure/): On how to add pop-ups to Leaflet.

- [Stack Overflow](https://stackoverflow.com/questions/63962443/create-a-post-save-signal-that-creates-a-profile-object-for-me): Creating post signals.

- [Stack Overflow](https://stackoverflow.com/questions/14820952/change-bootstrap-input-focus-blue-glow): Changing glow default glow effects on bootstrap.

- [Stack Overflow](https://stackoverflow.com/questions/7168658/why-is-the-padding-not-working-on-my-label-elements): Setting padding to input fields.

- [Stack Overflow](https://stackoverflow.com/questions/8806673/html-how-to-retain-formatting-in-textarea): on how to retain formatting o text area.

- [Boostrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/): Implementing nav bar, accordion, focus, hover effects, grid structure and more.

- [Amy Richardson](https://github.com/amylour/FreeFido_v2): for post signals and general django structure.

- [Joy Zadan](https://github.com/JoyZadan/shop-kbeauty): Implementing search bar and filters.

- [StaticsGlobe](https://www.youtube.com/watch?v=VZAmgg_khO0): How to calculate percentiles with num.py

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)


### **7.2. Media**

- [Font Awesome](https://fontawesome.com/): for the icons used in the footer of the application.

- [Unplash](https://unsplash.com/pt-br/s/fotografias/Serra-do-Curral): for index hero image

- All remaining photographs are my own.

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)


### **7.3. Acknowlegements**

- My informal mentor and great friend, [Bruno Dias](https://github.com/brunoald/), for helping me to structure the project.

- My mentor, Darío Carrasquel, for his support and constructive feedback.

- My partner, Joana, for all the emotional support.

[Back to top](https://github.com/hpesciotti/Speleometrics/blob/main/README.md)


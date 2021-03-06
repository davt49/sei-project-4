# Feeling Radiohead  

## Brief

Create an application using React with a Python backend

## Timeframe & Team

7 days, personal project

Project is live here https://feeling-radiohead.herokuapp.com/songs (Quick Access)

![](readmepics/feelingradiohead.png)


## Technologies
- React
- Python
- Flask
- Marshmallow
- SQLAlchemy
- Bulma
- Git
- Heroku

## Theme

Radiohead is an all-time favourite band for me and it was a lot of fun working on this project.

I wanted to create a index/show board that gives each song the detail it deserves: The lyric snippet gives an insight into the meaning/thought process behind the song, the review and music video are additional links that will open in a new tab and wouldn't stop the music, which plays immediately.

I seperated the songs into categories that better describe their style and mood. I explained more of this on the About page.

I picked background images that are relevant to the song. Such as older pictures of the band for their early albums and abstract paintings for their more erratic experimental outputs.

## Controls

##### Register and Log In to the App.

![](readmepics/login.png)

##### Filter songs.

![](readmepics/filter.png)

##### Click on a song to go into the show page, where music will play and can be paused. various info for the song.

![](readmepics/songinfo.png)

# Stack Overview/Process

## Flask.py

The models and controllers are seperated into: base, categories, songs, users and forumtopics. With varying usages of the RESTful routes, since forumtopics would require all the routes while songs slightly less. Currently website forum not configured on frontend, as I didn't feel it necessary for the idea of the app, however it's good to keep it as reference for future.

##### Base Model handles the datetime entries for user log in, posts and comments.

![](readmepics/basemodel.png)

##### User model and Auth controller handles the logging in. Using bcrypt to hash and validate the password input. Manages the tokens when logging in and validations.

![](readmepics/usermodel.png)

##### POST requests for login and register.

![](readmepics/postroutes.png)

##### Router keeps all the routes of the Backend in one place and so easier to manage.

![](readmepics/router.png)

##### Secure Route checks that the Authorization token is present, manages the JSON Web Token and assigns the correct error message according to error response.

![](readmepics/secureroute.png)

##### The Seeds file contains all the creative content from user profiles, songs to categories that makes up the core content of the site. The database is dropped and re-created on every seed run.

![](readmepics/seed.png)

## React.js

Connecting RESTful path from the backend to the components, which manages the functions and requests on the page.

##### The filter Songs option is done almost entirely on React, using the category data from seeds, the Songs are filtered to show only the categories selected.

![](readmepics/filtercode.png)

##### Changes state when clicked.

![](readmepics/filterrender.png)

##### The Song component gets referenced directly into Songs and acts as a specific function outside of the component, where the design and references to the seeds file is managed.

![](readmepics/song.png)

##### In the Song Show component the data is laid out for presentation.

![](readmepics/songshow.png)

##### Auth handles the log in and authentication for the user. Giving a token that expires after a set time when the user log in. Removes the token while logging out.

![](readmepics/auth.png)

##### App contains the BrowserRouter which easily manages the switching of different routes.

![](readmepics/browserrouter.png)

## Wins

The data from the seeds file is nicely presented onto the render on the frontend. This creates a nice concentration of data that is easily managed and to make changes and additions to.

## Challenges and Main Takeaways

Flask has a simpler style compared to Node.js and while the file structure and syntax is less demanding the knowledge needed to manipulate the backend, I feel is higher. We studied it for two days and went ahead to build our project, so more practice would be needed for me to be more comfortable with it. Although I do prefer the syntax compared to Node.js.

The filter function needed the addition of .some() to make it work with multiple categories as opposed to just one definite category.

![](readmepics/filtersome.png)

The songs are used for educational purposes as I'm well aware of copyright issues. However it was not intended to be used for profit but fan appreciation.

## Future Improvements

The addition of a user forum and Radiohead news section (if possible to link to an API) would be great, as well as information for tour dates and tickets. They will compliment the site well as a one stop shop for Radiohead.

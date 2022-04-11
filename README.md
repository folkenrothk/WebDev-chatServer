# `CMPSC 302` Web Development, Week 6: Front- vs. Back-end

* Assigned: 11 April 2022, 1:30 PM
* Due: 24 April 2022, 11:59 PM

## Having a chat

![o hai lets have uh chat](https://www.bestcat.com/files/variants/wqpfaohu4nwi1ycfi6pvs3rqx7h7/95276c0da81b822f513711c81fff742daadd87617d24212e679e52fc18befcd2/Tea_Party.jpg)

This project results in a basic chat server, i.e. an app that allows anyone to join and chat with anyone else present on the app's web page.
Much of this relies on concepts we've been learning over the last three or four weeks, and introduces a new way to use Javascript: via `nodejs`.
While this may seem new -- and, to some extent is -- it's not a new language, just a _server-side_ ("back-end") implentation of Javascript.

### Front- vs. Back-end

The section header appears to set up an oppositional relationship between these two "layers" of a web app. However, they're really the two
complementary layers of anything that calls itself an "app." Developers refer to the various configurations of layers that make up an 
application as that app's "stack."

For this project, you'll build _both_.

#### Supreme clientele

We think of "front-end," we're really thinking about everything that's _client_-side, that is HTML, CSS, and proper Javascript. Each of these
pieces are rendered (i.e. cobbled together) by the browser. The user accessing the site is referred to as a "client" in this case and all
of this work is, essentially, their responsibility. Thankfully, modern browers take care of this.

#### Behind your back

Any functionality that's rendered by a third-party _server_ is often referred to as "back-end." User browsers aren't responsible for this and
generally this layer is described (in part) as a "listener," waiting for a specific "front-end" client to ask to connect and retrieve information 
or (in our case) _stay connected_ to coordinate events like sending messages to everyone in a chat room.

### Requirements

#### Design

* A two-row grid which features a chat input box and scrolling input window which changes based on screen width, per the wireframes below
* A login "modal" (i.e. pop-over window) that requires users to set a user name before entering the chat
* `HTML` form elements to accomplish user inputs for user names and chat messages

#### Functionality

* User name as a requirement to "unlock" the message form
* Ability to send a message by pressing only `Enter` key in message entry
* Connection to your Heroku `nodejs` server to transmit messages
  * such that multiple parties can send and receieve messages in the main window
* Ability to "persist" connections by sending "ping" messages on a regular basis
  * "Regular basis" means once per second until a user quits the server
  * "quits the server" just means "closes the window"
* One additional feature that _you develop_ to implement
  * if you're looking for ideas, the professor has many _tailored to you_!

Using the above basic functionality, a testing script should be able to send and receive `20` messages over a span of 4 minutes. This is _important_:

* To pass this test, each your message must have the `.chat_msg` selector -- this can be done with any element, but _must be the right selector_
  * If you're not passing the `[CHAT]` test, it's _likely_ that the above is the reason


#### Writing

This assignment requires a bit of writing -- namely via a short description of your intended additional functionality [see above](#Functionality).
To complete the writing, finish the `TODO` in the `writing/` directory of the main folder of the repository. Use the `feature.md` file to:

* describe the intended functionality in a paragraph no more than 150 words
* describe _how_ you intend to implement it
* in the code block provided in the file, paste the particular code you used to implement it
  * wondering what a "code block" is? You'll know it when you see it.

##### Wireframes

###### Desktop

![On yr main](https://chat.cmpsc302.chompe.rs/media/wireframe-desktop.png)

###### Mobile

![On the Go](https://chat.cmpsc302.chompe.rs/media/wireframe-mobile.png)

#### Functionality

## Making a GitHub Pages page

This assignment also requires you to make your work available via GitHub Pages. For a primer on where to find it
and how to do it:

- [ ] locate and click the `Settings` tab at the top of the screen
- [ ] from the menu at the left, select `Pages`
- [ ] locate the "Source" heading; set the "Branch" as `main`, and change the second drop-down to `/docs`
- [ ] click `Save`
- [ ] One last step: make the page _public_ by setting `GitHub Pages visibility` to `Public`
  * This step is _required_ for your HTML and CSS to pass validation!

A green box will appear at the top of the page listing the random URL that you've been assigned. This is your
URL!

## Setting up a Heroku app

### Creating an app

To do the server ("back-end") part of this assignment, you'll need to head over to [Heroku](https://www.heroku.com) and create
a free account. Once you've created one:

1. Log in and find the `New` button (it's in the upper left corner)
2. Click `Create new app` and name it: `cmpsc-302-chat-server-YOUR_GITHUB_USERNAME`
3. Click `Create app`
4. On the resulting screen, locate the `Deployment` section
5. Click `GitHub`
6. Connect Heroku to your GitHub account
7. Once you've linked the account, select the `Allegheny-ComputerScience-302-S2022` organization
8. Search for your repository and link it
9. As a final step, set up automatic deploy from the `main` branch

Once you've linked the repository, any `push` you make to your GitHub repository will also build the `app` directory on Heroku
at the address:

```
APP_NAME.herokuapp.com/
```

### Setting up "Buildpacks"

To tell the Heroku app exactly what it is (i.e. that it's a Node app) and that we need to build our app from the `app/` folder
(rather than `docs/` -- the "client" side).

1. Locate the `Settings` menu option near the top of the screen
2. Scroll to the `Buildpacks` section
4. Click `Add buildpack``
3. Add the `https://github.com/timanovsky/subdir-heroku-buildpack.git` repository to the app
4. Also search for and add the `heroku/nodejs` pack

## Accepting the assignment

- [ ] Using either the link posted to our class Discord or the [course schedule](https://cmpsc302.chompe.rs)
- [ ] Click the link provided for the lab assignment and accept it in GitHub classroom
- [ ] Once the assignment finishes building, click the link to go to your personal repository assignment

## "Cloning" a repository

### Using the correct download link

- [ ] On this repository's page, click the `Clone or download` button in the upper right hand corner
* You may need to scroll up to see it
- [ ] In the upper right corner of the box that appears, click `Use SSH`
- [ ] Copy the link that appears in the textbox below the phrase "Use a password with a protected key."

#### Cloning

* [ ] Type `ls` in your terminal window
* You should be in your `~` directory
- [ ] Find the folder you've made to hold class assignments (may involve `cd`ing)
- [ ] Once there, "clone" the repository using the link copied above
  * If I (the instructor) were to clone my own repository, I'd enter (your link will look different):

```
git clone git@github.com:Allegheny-ComputerScience-302-S2022/cmpsc-302-week-3-basic-style-exercises.git
```

## Wrap-up

### Submitting the assignment/saving progress

The GitHub platform is a place to store your work. So, it makes some sense that should be able to _clone_ (download) from it, and push back (upload) to it. Here, we'll learn this second part.

- [ ] `cd` to your `~` folder
- [ ] Locate your `cmpsc-302-week-3-basic-style-exercises` folder and `cd` to it.

Once in this folder, we need to tell git that there have been changes.

- [ ] Type `git add -A` and press `Enter`
* This tells git to look through the _entire_ folder structure for new changes and "stage" them

- [ ] Type `git commit -m "YOUR COMMIT MESSAGE"` to "label" the commit
* This is typically something like `git commit -m "Fixing a typo"` -- the message in quotes should be as descriptive as possible, while still remaining somewhat short

- [ ] To send all changes to the server, type `git push`
- [ ] At the prompt, input the password associated with the `SSH Key` you created earlier in this exercise (yesterday)

Once the process finishes successfully, we're done!

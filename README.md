# `CMPSC 302` Web Development: Chatter & Messages
 _Completed Spring 2022_
 
## Having a chat

This project results in a basic chat server, i.e. an app that allows anyone to join and chat with anyone else present on the app's web page.
Much of this relies on concepts we've been learning over the last three or four weeks, and introduces a new way to use Javascript: via `nodejs`.
While this may seem new -- and, to some extent is -- it's not a new language, just a _server-side_ ("back-end") implentation of Javascript.

### Front- vs. Back-end

The section header appears to set up an oppositional relationship between these two "layers" of a web app. However, they're really the two
complementary layers of anything that calls itself an "app." Developers refer to the various configurations of layers that make up an 
application as that app's "stack."

For this project, we build _both_.

#### Supreme clientele

We think of "front-end," we're really thinking about everything that's _client_-side, that is HTML, CSS, and proper Javascript. Each of these
pieces are rendered (i.e. cobbled together) by the browser. The user accessing the site is referred to as a "client" in this case and all
of this work is, essentially, their responsibility. Thankfully, modern browers take care of this.

#### Behind your back

Any functionality that's rendered by a third-party _server_ is often referred to as "back-end." User browsers aren't responsible for this and
generally this layer is described (in part) as a "listener," waiting for a specific "front-end" client to ask to connect and retrieve information 
or (in our case) _stay connected_ to coordinate events like sending messages to everyone in a chat room.

### Project Requirements

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

# CMPSC 302 Chat Server Feature Description

## In no more than 150 words, describe the chat feature you plan to implement.

The chat feature I plan to implement is one that changes the background of the chat screen. This would allow for "the void" to be a different galaxy at the click of a button. I want to design it that so it would only change for the current user. I do not want it  changing, thus not flashing, for all users of the chat. 

## How do you plan to achieve this?

I plan to code this on the client side so that it does not disturb every users' experience. This will work with an event listener on the escape key. I plan to create a random generator to pick one of the galaxy images to make the background.

## Paste the code used to achieve this between the two "fences" below.

### Javascript

#### `client.js`

```javascript
sendMsg.addEventListener("keydown", (evt) => { 
    if(evt.key == "Escape"){
        chat.post("BLAST-OFF");
        var randNum = Math.floor(Math.random() * 7) + 1;
        var fileName = "g" + randNum;
        var path = `style/img/${fileName}.png`;
        document.body.style.backgroundImage = `url('${path}')`;
    }
});
```


### Other "Spacey" Additions

#### `client.js`

```javascript
setName.addEventListener("click", (evt) => {
    let name = nameEntry.value;
    if(!name) return false;

    chatLogin.setAttribute("hidden","true");
    evt.preventDefault();

    username = `Cadet ${name}`;

    chat.name = username;
    chat.send(`Welcome ${chat.name}`,"greet");
});
```

#### `server.js`

```javascript
const emoji = {
  "greet": ["🧑‍🚀","👽"],
  "normal": ["🚀","⭐","🌟","💫","🌠"],
  "ping": ["👾"],
}
```


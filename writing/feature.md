# CMPSC 302 Chat Server Feature Description

## In no more than 150 words, describe the chat feature you plan to implement.

`TODO`

## How do you plan to achieve this?

`TODO`

## Paste the code used to achieve this between the two "fences" below.

You must use at least one of the entries below.

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


### Other Additions

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

#### CSS

```css
/* TODO */
```

var host = "wss://cmpsc-302-chat-server-katefolk.herokuapp.com"; // TODO: Change to your Heroku host


/* Notes 4.13: ahh serialization and metadata?
let name = message.users; >> let msg = message.text; >> let type = emoji(message.type);

order matters, serialization bruh
    gonna give names, tags etc >> I AM ALL POWERFUL 
    (list needs comma not semi colon)

*/

/*  missing lab w/ help from Maria */

// Collecting username
setName.addEventListener("click", (evt) => {
    let name = nameEntry.value;
    if(!name) return false;
    chat.name = name;
    nameBox.setAttribute("hidden","true");
    evt.preventDefault();
})


// Using enter key as submission option
sendMsg.addEventListener("keydown", (evt) => {
    if(evt.key == "Enter"){
        sendBtn.click();
        evt.preventDefault();
    }
});

// Script WebSocket communication 
var chat = {
    socket: new WebSocket(host), //how we show up
    // FUNCTION TO START CONVERSING
    init: () => { //start chatting
        chat.window = document.getElementById("chat-window");
        //functions to run
        chat.socket.addEventListener("message", (evt) => {
            // let's listen right away
            let msg = evt.data; // let the content be the message (not the id)
            console.log(msg); // temporary test to listen
        });
        // hungry hungry web sockets: need to give something or it will shut off
        setInterval(() => { // "A keep alive" - no name so cant stop wont stop
            chat.send("","ping"); //empty message & type
        }, 1000); 
    }, //start new thing, lets chat (we have content and type to send)
    
    // FUNCTIONs TO CHAT

    scroll: () => {
        let msgs = Array.from(
            document.getElementsByClassName("chat-msg")
        );
        let pos = msgs[msgs.length-1].offsetTop;
        document.getElementById("chat-window").scrollTo({
            top:pos,
            behavior: "smooth"
        });
        return false;
    },

    send: (message, type) => {
        // we can only send one thing (but this can be a package of things)
        let packet = {
            user: chat.name,
            text: sendMsg.value || message,
            type: type
        }
        //prevent blank messages (mostly)
        if(typeof(packet.text) !== "string") return false;

        // now lets give it 
        chat.socket.send(
            JSON.stringify(packet) // blah our package is in java (gross), Json will fix it
        );
        if(type !== "ping") sendMsg.value="";
        return false; // act like it didn't happen, set defaults
    },

    post: (message) => {
        let msg = document.createElement("p");
        let text = document.createElement("span");
        text.className = "chat-msg";
        text.innerText = `${message}`;
        msg.appendChild(text);
        chat.window.appendChild(msg);
        return false;
        chat.scroll();
    },
}

// Start the Chat
chat.init();
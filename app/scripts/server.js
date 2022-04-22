const express = require('express');
const { Server } = require('ws');
const port = process.env.PORT || 8080;

const server = express()
  .listen(port, () => console.log(`Listening on ${port}`));

const socket = new Server({ server });

var users = {};

const emoji = {
  "greet": ["🧑‍🚀","👽"],
  "normal": ["🚀","⭐","🌟","💫","🌠"],
  "ping": ["👾"],
}

socket.on("connection", (sock, request) => {

  let uid = 0;

  while(true) {
    if(!users.hasOwnProperty(uid)) {
      users[uid] = sock;
      break;
    }
    uid++;
  }

  sock.on("close", () => {
    delete users[uid];
  });

  sock.on("message", (message) => {
    message = JSON.parse(message);
    let name = message.user;
    let msg = message.text;
    let type = emoji[message.type];
    let chosenIcon = type[Math.floor(Math.random() * type.length)];
    for (let user in users) {
      if (message.type === "ping") break;
      users[user].send(`${name} ${chosenIcon} ${msg}`);
    }
  });

});

const roomName = JSON.parse(document.getElementById('room-name').textContent);
// getting the user that has authenticated
const itsme = JSON.parse(document.getElementById('user-name').textContent);
const ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
const url = `${ws_scheme}://${window.location.host}/ws/chat/${itsme}/${roomName}/`;

// Creating the WebSocket...

const chatSocket = new WebSocket(url);

// When the WebSocket opens...
chatSocket.onopen = (event) => {
    console.log('Opening socket...');
}

// When the socket receives a message...
chatSocket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    const chatLog = document.querySelector('#chat-log');

    if (data.user === itsme) {
        chatLog.insertAdjacentHTML('beforeend', `<div class="its-me">
            <h1>You</h1>
            <p>${data.message}</p>
        </div>`);
        console.log(itsme);
    } else {
        chatLog.insertAdjacentHTML('beforeend', `<div class="message">
            <h1>${data.user}</h1>
            <p>${data.message}</p>
        </div>`);
    }


    chatLog.scrollTop = chatLog.scrollHeight;

    console.log('DATA: ', data);
    // document.querySelector('#chat-log').value += `${data.user}: ${data.message}\n`;
}

// When the socket closes...
chatSocket.onclose = (event) => {
    console.log('Aborting chat socket...');
}

// Focusing the typing bar
document.querySelector('#chat-message-input').focus();

// Submitting the text typed by the user
document.querySelector('#chat-message-input').onkeyup = (event) => {
    if (event.keyCode === 13) {  // enter, return
        if (event.target.value.trim().length > 0) {
            document.querySelector('#chat-message-submit').click();
        } else {
            event.target.value = "";
        }
    }
}

document.querySelector('#chat-message-submit').onclick = (event) => {
    // getting the message 
    const messageInput = document.querySelector('#chat-message-input');
    const message = messageInput.value.trim();
    // sending it to the WebSocket
    chatSocket.send(JSON.stringify({
        'js-message': 'This is sent by client side JS',
        'message': message,
        'user': itsme
    }));
    // reset the input field
    messageInput.value = "";
}
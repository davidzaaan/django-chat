const user = JSON.parse(document.getElementById('user-name').textContent);
console.log(user);

// Getting the input
document.querySelector('.chat-name').focus();
// If the user press enter...
document.querySelector('.chat-name').onkeyup = (event) => {
    if (event.keyCode === 13) {
        document.querySelector('.submit-message').click(); // submitting the room name
    }
};

document.querySelector('.submit-message').onclick = (event) => {
    let roomName = document.querySelector('.chat-name').value;
    // user redirection
    window.location.pathname = `/chat/${user}/${roomName}/`;
}
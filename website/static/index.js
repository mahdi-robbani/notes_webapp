function deleteNote(noteId){
    /**
     * Takes in a noteID and sends a POST request to the delete-note
     * endpoint. After getting a response from the endpoint, reloads the
     * window.
     */

    // fetch creates a request
    fetch('/delete-note', {
        method: 'POST',
        // convert to string and send data as a json
        body: JSON.stringify({ noteId: noteId})
    }).then((_res) => {
        // redirects to homepage, basically reloads the window
        window.location.href = "/";
    })
}

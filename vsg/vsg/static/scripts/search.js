const button = document.getElementById("submitSearch");
const requestSearch = (e) => {
    e.preventDefault()
    const input = document.getElementById("search");
    const token = document.getElementsByName(
        "csrfmiddlewaretoken"
    )[0].value;
    console.log(input.value, typeof input.value)
    window.location.replace(`http://127.0.0.1:8000/search/${input.value}/1`)
    // fetch('http://127.0.0.1:8000/search/', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json',
    //         'X-CSRFToken': token,
    //     },
    //     credentials: 'same-origin',
    //     body: JSON.stringify({
    //         'query': input.value,
    //     })
    // }).then((response) => {
    //     console.log('Success.')
    // }).catch(
    //     (error) => {
    //         console.error(error);
    //         alert('Error: could not execute query.');
    //     }
    // )
}

console.log('button', button)
if (button) {
    button.onclick = requestSearch;
}
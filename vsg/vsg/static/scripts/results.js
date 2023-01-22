const heartIcons = document.getElementsByClassName('favorite-icon');
const token = document.getElementsByName(
    "csrfmiddlewaretoken"
)[0].value;

const favorite = (element) => {
    fetch('http://127.0.0.1:8000/search/favorite', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': token,
        },
        credentials: 'same-origin',
        body: JSON.stringify({
            'mal_id': element.id,
        })
    }).then((response) => {
        console.log('Success.');
        element.src = element.src.replace('empty', 'full');
    }).catch(
        (error) => {
            console.error(error);
            alert('Error: could not execute query.');
        }
    )
}
const unFavorite = (element) => {
    fetch('http://127.0.0.1:8000/search/favorite', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': token,
        },
        credentials: 'same-origin',
        body: JSON.stringify({
            'mal_id': element.id,
        })
    }).then((response) => {
        console.log('Success.');
        element.src = element.src.replace('full', 'empty');
    }).catch(
        (error) => {
            console.error(error);
            alert('Error: could not execute query.');
        }
    )
}

const heartOnClick = (event) => {
    const element = event.srcElement;
    if (element.src.includes('full')) {
        unFavorite(element);
    } else {
        favorite(element);
    }
}

Array.from(heartIcons).forEach(element => {
    element.onclick = heartOnClick;
});
const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

const csrftoken = getCookie("csrftoken");

function getlikesplace(type, pk) {
    let counter_element;
    if (type === "question") {
        const alllikes = document.getElementById('like_' + pk);
        counter_element = alllikes.querySelector('.like-count');
    } else {
        const alllikes = document.getElementById('likeanswer_' + pk);
        counter_element = alllikes.querySelector('.like-count');
    }
    return counter_element
}


function like() {
    var like = $(this);
    var type = like.data('type');
    var pk = like.data('id');
    var action = like.data('action');
    var dislike = like.next();
    const counter_element = getlikesplace(type, pk);
    /*
        var btn = document.getElementById('likebut_'+pk);
        var list = btn.classList;
        console.log(list)
        btn.classList.add("active");



     */

    $.ajax({
        url: "/api" + "/" + type + "/" + pk + "/" + action + "/",
        type: 'POST',
        data: {
            'obj': pk,
        },
        headers: {'X-CSRFToken': csrftoken},
        success: function (json) {
            like.find("[data-count='like']").text(json.like_count);
            dislike.find("[data-count='dislike']").text(json.dislike_count);
            counter_element.innerText = json.sum_rating;
        }
    });

    return false;
}

function dislike() {
    var dislike = $(this);
    var type = dislike.data('type');
    var pk = dislike.data('id');
    var action = dislike.data('action');
    var like = dislike.prev();
    const counter_element = getlikesplace(type, pk);
    $.ajax({
        url: "/api" + "/" + type + "/" + pk + "/" + action + "/",
        type: 'POST',
        data: {'obj': pk},
        headers: {'X-CSRFToken': csrftoken},
        success: function (json) {
            dislike.find("[data-count='dislike']").text(json.dislike_count);
            like.find("[data-count='like']").text(json.like_count);
            counter_element.innerText = json.sum_rating;
        }
    });

    return false;
}

$(function () {
    $('[data-action="like"]').click(like);
    $('[data-action="dislike"]').click(dislike);
});
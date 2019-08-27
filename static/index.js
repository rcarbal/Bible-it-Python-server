$(document).on('show.bs.modal', '.fade', function (e) {

    console.log('event');
    console.log(e);

    const context = this;
    console.log(context);
    var current_modal = this.getElementsByClassName('#fade');

    var modal = $(this).data('modal');
    var word;

    if (modal == 2) {
        word = $(this).data('word2');
    } else {
        word = $(this).data('word');
    }


    var pos_list = $(this).data('pos');
    var index = $(this).data('index');


    var pos;

    if (modal == "1") {
        pos_list = pos_list.slice(1, pos_list.length - 1);
        pos_replaced = pos_list.split(",");
        pos = pos_replaced[index - 1];
    }
    else if (modal == "2") {
        pos = pos_list;
    }

    element = this.getElementsByClassName("modal-body")[0];
    element.innerHTML = "";

    // create the definition header
    let definitionHeader = document.createElement('h6');
    definitionHeader.innerHTML = "-" + pos + " " + word;

    // create <hr> tag
    let hrTag = document.createElement('hr');


    // create the synonym header
    let synonymHeader = document.createElement('h6');
    synonymHeader.innerHTML = "- Synonyms"

    // create ordered list
    let ol = document.createElement('ol');

    element.appendChild(definitionHeader);
    element.appendChild(ol);
    element.appendChild(hrTag);
    element.appendChild(synonymHeader);

    axios.get("/api/word/definition?word=" + word)
        .then((response) => {

            // get modal div
            const arr = response.data;

            if (arr.hasOwnProperty("definitions")) {
                response.data.definitions.forEach((definition) => {
                    let liItem = document.createElement('li');
                    liItem.innerHTML = definition.definition;
                    ol.appendChild(liItem);
                });

            }

            // get synonym ordered list
            getSynonyms(word, callback);
        });

    // callback
    const callback = (synonymOrderedList) => {
        element.appendChild(synonymOrderedList)

    }

    //    element.appendChild(synOl);


});

// Retrieves Synonnyms

function getSynonyms(word, callback) {
    axios.get("/api/word/synonym?word=" + word)
        .then((response) => {
            let ol = document.createElement('ol');

            response.data.synonyms.forEach((synonym) => {
                let li = document.createElement('li');
                li.innerHTML = synonym;

                ol.appendChild(li);
            });

            callback(ol);
        });
}


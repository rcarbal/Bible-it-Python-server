let element = null;

$(document).on('show.bs.modal', '.fade', function (e) {

    var modal = $(this).data('modal');
    var word;

    if (modal == 2) {

        // sets up the inexact word list
        word = $(this).data('word2');
    } else {

        // sets up the exact word list
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

     // create the definition h6 element
     let headerEl = document.createElement('h6');
     headerEl.innerHTML = "- Definitions"

    // create <hr> tag
    let hrTag = document.createElement('hr');


    // create the synonym header
    let synonymHeader = document.createElement('h6');
    synonymHeader.innerHTML = "- Synonyms"

    // create ordered list
    let ol = document.createElement('ol');

    element.appendChild(definitionHeader);
    element.appendChild(headerEl);
    element.appendChild(ol);
    element.appendChild(hrTag);
    element.appendChild(synonymHeader);

    // callback
    const callback = (synonymOrderedList) => {
        element.appendChild(synonymOrderedList)

    }


    // Call definitions urk
    getDefinitions(word,ol)




});


// Retireves Definitions
function getDefinitions(word, defintionOderedList) {
    axios.get("/api/word/definition?word=" + word)
        .then((response) => {

            // get modal div
            const arr = response.data;

                arr.forEach((definition) => {

                    // loop through the shortdefs
                    let shortdef = definition.shortdef;

                    shortdef.forEach((singelDef) => {
                        // append single definition to the module                        
                        let liItem = document.createElement('li');
                        liItem.innerHTML = singelDef;
                        defintionOderedList.appendChild(liItem);
                    });
                });

            

            // get synonym ordered list
            // getSynonyms(word, callback);
        });
}
// Retrieves Synonnyms
function getSynonyms(word) {
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




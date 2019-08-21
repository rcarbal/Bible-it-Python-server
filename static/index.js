$(document).on('show.bs.modal', '.fade', function(e){
    var word = $(this).data('word');
    var pos_list = $(this).data('pos');
    var index = $(this).data('index');
    var modal = $(this).data('modal');

    var pos;

    if (modal == "1"){
      pos_list = pos_list.slice(1, pos_list.length -1);
      pos_replaced = pos_list.split(",");
      pos = pos_replaced[index - 1];
    }
    else if(modal == "2"){
        pos = pos_list;
    }

    element = this.getElementsByClassName("modal-body")[0];
    element.innerHTML = "";

    // create the definition header
    let definitionHeader = document.createElement('h6');
    definitionHeader.innerHTML = "-"+ pos + " " + word;

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
    .then((response)=>{

       // get modal div
       const arr = response.data;

       response.data.definitions.forEach((definition) => {
            let liItem = document.createElement('li');
            liItem.innerHTML = definition.definition;
            ol.appendChild(liItem);
       });
    });

    // callback
    const callback = (synonymOrderedList) => {
        element.appendChild(synonymOrderedList)

    }

    // get synonym ordered list
    const synOl = getSynonyms(word, callback);

//    element.appendChild(synOl);


});

// Retrieves Synonnyms

function getSynonyms(word, callback){
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


$(document).on('show.bs.modal', '.fade', function (e) {
    var word = $(this).data('word');
    var pos_list = $(this).data('pos');
    var index = $(this).data('index');

    console.log(pos_list);
    console.log(index);

    pos_list = pos_list.slice(1, pos_list.length -1);
    pos_list = pos_list.replace(/''/, "");


    pos_list = pos_list.split(",");
    console.log(pos_list);


    pos = pos_list[index - 1];

    element = this.getElementsByClassName("modal-body")[0];
    element.innerHTML = "";

    // create the definitoin header
    let definitionHeader = document.createElement('h6');
    definitionHeader.innerHTML = "-"+ pos + " " + word;

    // create ordered list
    let ol = document.createElement('ol');

    element.appendChild(definitionHeader)
    element.appendChild(ol)

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

});

function connect(word){
    axios.get("/api/word/definition?word=" + word)

}

function getWordInformation(){

}


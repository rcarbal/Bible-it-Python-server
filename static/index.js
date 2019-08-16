$(document).on('show.bs.modal', '.fade', function (e) {
    var word = $(this).data('word');
    var pos = $(this).data('pos');
    var index = $(this).data('index');

    element = this.getElementsByClassName("modal-body")[0];
    element.innerHTML = "";

    axios.get("/api/word/definition?word=" + word)
    .then((response)=>{
       // get modal div
//       const arr = response.data;
//       console.log(arr);
       response.data.definitions.forEach((definition) => {
        let paragraph = document.createElement('p');
        paragraph.innerHTML = definition.definition;
        element.appendChild(paragraph);
       });
    });

});

function connect(word){
    axios.get("/api/word/definition?word=" + word)

}

function getWordInformation(){

}


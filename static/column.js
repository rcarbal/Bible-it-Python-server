class ColumnChecker{

    constructor(firstYear, lastYear){
        this.firstYear = firstYear;
        this.lastYear = lastYear;
        this.years = {};
        this.setupColumnInfo()
    }

    // retrieves all the column information
    setupColumnInfo(){

        // get elements for year
        for(let i=this.firstYear; i <=this.lastYear; i++){
            // find element
            let element = document.getElementById(`bible-${i}-row`);
            console.log(element);
        }
    }   
}
class ColumnChecker{

    constructor(firstYear, lastYear){
        this.firstYear = firstYear;
        this.lastYear = lastYear;
        this.years = {};
        this.setupColumnInfo()
    }

    getYear(year){
        return this.years[`${year}`];
    }

    // retrieves all the column information
    setupColumnInfo(){
        // get elements for year
        for(let i=this.firstYear; i <=this.lastYear; i++){
            if (i == 0){
                continue;
            }
            // find element
            let element = document.getElementById(`bible-${i}-row`);
            if (element.hasChildNodes() == false){
                this.years[`${i}`] = 0
            } else {
                console.log(element.hasChildNodes());
                console.log(`Found Child NODES at ${i}`)
                console.log(element);
            }
        }
    }
    
    addAYearColumn(year){
        let yearToAddTo = this.years[`${year}`];
        let updatedYearToAdd = yearToAddTo + 1;
        this.years[`${year}`] = updatedYearToAdd;
        console.log();
    }
}
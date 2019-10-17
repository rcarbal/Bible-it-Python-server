function setupHistoricalPeriods(historicalPeriods){
    // remove escape characters
    const correctHistoricalPeriods = JSON.parse(historicalPeriods.replace(/&#34;/g,'"'));

    // place the correct historical period on the timeline.
    for (h in correctHistoricalPeriods){
        // loop through all the years
        
        addClassesToYear(correctHistoricalPeriods[h]['first_year'], 
            correctHistoricalPeriods[h]['last_year'], correctHistoricalPeriods[h]['name']);
        
    }

    alert("DONE");
    console.log("DONE");
}

function addClassesToYear(firstYear, lastYear, period){
    console.log(`The first year is ${firstYear}, the last year is ${lastYear}`);

    // find the years element
    let firstYearElement = document.getElementById(`hist-${firstYear}`);
    firstYearElement.textContent = period;
    let lastYearElement = document.getElementById(`hist-${lastYear}`);

    // add classes to element
    firstYearElement.classList.add("sec-start");
    lastYearElement.classList.add("sec-stop");

    // loop through all years and add classes
    let initialYear = firstYear;

    console.log("Printing Years");
    for(i = firstYear; i < lastYear + 1; i++){
        // console.log(initialYear);
        // console.log(i);

        if (i == 0){
            initialYear++;
            continue;
        }

        // find the years between
        let yearElement = document.getElementById(`hist-${initialYear}`);
        yearElement.classList.add('sec');
        yearElement.classList.add('hist-pad');

        initialYear++;
    }
    let emptyElement = document.createElement('div');
    emptyElement.textContent = 'PERIOD';
}
function setupHistoricalPeriods(historicalPeriods, biblicaPeriods){
    // remove escape characters
    const correctHistoricalPeriods = JSON.parse(historicalPeriods.replace(/&#34;/g,'"'));

    // place the correct historical period on the timeline.
    for (h in correctHistoricalPeriods){
        // loop through all the years
        let periodType = "history";
        addClassesToYear(correctHistoricalPeriods[h]['first_year'], 
            correctHistoricalPeriods[h]['last_year'] - 1, correctHistoricalPeriods[h]['name'], periodType);
        
    }

    // place the correct biblical periods in the timeline
    const correctBiblicalPeriods = JSON.parse(biblicaPeriods.replace(/&#34;/g,'"'));

    for (b in correctBiblicalPeriods){
        const firstYear = correctBiblicalPeriods[b]['first_year'];
        const lastYear =  correctBiblicalPeriods[b]['last_year'] - 1;
        const name = correctBiblicalPeriods[b]['name']; 
        const period = 'biblical'
        addClassesToYear(firstYear, lastYear, name, period);
    }
}

function addClassesToYear(firstYear, lastYear, period, periodType){
    let type;
    let paddingType;

    if (periodType == "history"){
        type = "hist-";
        paddingType = "hist-pad";
    } else {
        type = 'bible-';
        paddingType = 'bible-pad';
    }

    // find the years element
    let firstYearElement = document.getElementById(`${type}${firstYear}`);
    firstYearElement.textContent = period;
    let lastYearElement = document.getElementById(`${type}${lastYear}`);

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
        let yearElement = document.getElementById(`${type}${initialYear}`);
        yearElement.classList.add('sec');
        yearElement.classList.add(paddingType);

        initialYear++;
    }
    let emptyElement = document.createElement('div');
    emptyElement.textContent = 'PERIOD';
}
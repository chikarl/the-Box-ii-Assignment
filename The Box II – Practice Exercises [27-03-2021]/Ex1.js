

function cm() {
    var feet, inches, cm;
    feet = Number(document.cal.feet.value)
    inches = Number(document.cal.inches.value)
    cm = (30.48*feet)+(2.54*inches)
    document.getElementById("outputCM").innerHTML=cm+' cm';
}

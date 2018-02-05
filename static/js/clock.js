function clock()
{
    var today = new Date();
    var day = today.getUTCDate();
    var month = today.getUTCMonth();
    var year = today.getUTCFullYear();

    if (month < 10) {
        month = "0" + month;
    }
    if (day < 10) {
        day = "0" + day;
    }

    var hours = today.getUTCHours();
    var minutes = today.getUTCMinutes();

    if (hours < 10) {
        hours = "0" + hours;
    }
    if (minutes < 10) {
        minutes = "0" + minutes;
    }

    document.querySelector(".clock").innerHTML = "UTC: " + day + "." + month + "." + year + " " + hours + ":" + minutes;

    setTimeout(clock, 60000);
}
window.addEventListener("load", clock);
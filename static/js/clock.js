function clock()
{
    var today = new Date();
    var day = today.getDate();
    var month = today.getMonth();
    var year = today.getFullYear();

    var hours = today.getHours();
    var minutes = today.getMinutes();
    var seconds = today.getSeconds();
    document.querySelector(".clock").innerHTML = "Current time: " + day + "." + month + "." + year + " " + hours + ":" + minutes + ":" + seconds;

    setTimeout(clock, 1000);
}
window.addEventListener("load", clock);
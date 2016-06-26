var Handle_index_html = "Handle_index_html";
var prime_num = "";
var loop_cntl = 0;

$(document).ready(function(){
    $("#id_btnreg").click(function(){
        alert("Hello! I am an alert box!!");
    });
});

var btnGetPrimes = function(){
    loop_cntl = 1;
    loop_cnt = 0
    loopGetPrimes(loop_cntl, loop_cnt)
}

function loopGetPrimes(loop_cntl, loop_cnt) {
    while (loop_cntl) {
        loop_cnt += 1;
        if (loop_cnt > 1)
            loop_cntl = 0;
        else {
            fGetPrimes()
       }
    }
}

function fGetPrimes(){
    $.get("/get_primes", function(data, status){
        var prime_num = data["prime"];
        var m1 = "prime = " + data["prime"] + " status =" + status;
        console.log(m1);
        document.getElementById("id_inp1").value = prime_num;
        document.getElementById("id_inp1").innerHTML(prime_num);
    });
};

function btnFinishPrimes(){
    $.get("/finish_primes", function(data, status){
        document.getElementById("id_inp1").value = "finish primes 1";
        document.getElementById("id_inp1").innerHTML("finish primes 2");
        console.log("finish_promes");
    });
};
//console.log("in func1");
//.- sendform.js     file 
    //$(function() {
    //$('#id_btnreg').click(function() {
//$("#buildyourform").on('click', '#id_btnreg', function () { 
            //setTimeout(loopGetPrimes, 10000); // check again in a second

       //break;   // do it only once

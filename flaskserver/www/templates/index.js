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
        var prime_num = data;
        var m1 = "<b>prime = " + data + " status = " + status +"</b>";
        console.log(m1);
        $("id_inp1").text(data);
        $("id_inp1").html(m1);
    });
};

function btnFinishPrimes(){
    $.get("/finish_primes", function(data, status){
        var result = data["result"];
        var m1 = "<b>result = " + result + " status = " + status +"</b>";
        console.log(m1);
        //$("id_inp1").text(result);
        $("id_inp1").html(m1);
        console.log("finish_primes");
    });
};
//console.log("in func1");
//.- sendform.js     file 
    //$(function() {
    //$('#id_btnreg').click(function() {
//$("#buildyourform").on('click', '#id_btnreg', function () { 
            //setTimeout(loopGetPrimes, 10000); // check again in a second

       //break;   // do it only once

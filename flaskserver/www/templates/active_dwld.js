var Handle_active_download_html = "Handle_active_download_html";
var gmsg1 = "";

$(document).ready(function(){
    $("#id_btnreg").click(function(){
        alert("i am just a punk");
    });
});


//The onload of the page function
function getActiveDwLd(){                   // purl, pidtable){
    var inpInterval = setInterval(function(){
        fGetData();
    }, 10000);    // 20 secondx
};

//ajax get the current dict in the list
function fGetData(){
    $.get("/dashboard", function(data, status){
        curr_active = data["curr_active"];
        //console.log("fDataToTable data,status = " + data + ' ' + status);
        fDataToTable(curr_active);
    });
};

//data tyo the table
function fDataToTable(curr_active){
    $("#id_ip").html(curr_active["ip"]);
    $("#id_s_time").html(curr_active["time_start"]);
    $("#id_cntsent").html(curr_active["count_sent"]);
    $("#id_last").html(curr_active["last_prime"]);
    $("#id_ppmin").html(curr_active["throughput"]);
    //console.log("fDataToTable" + data);
};

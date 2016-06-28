var Handle_active_download_html = "Handle_active_download_html";
var gmsg1 = "";

$(document).ready(function(){
    $("#id_btnreg").click(function(){
        alert("i am just a punk");
    });
});


//var getActiveDwLd = function(purl, pidtable){
function getActiveDwLd(){                   // purl, pidtable){
    fGetData();
};

function fGetData(){
    $.get("/get_active_downloads", function(data, status){
        console.log("fDataToTable data,status = " + data + ' ' + status);
        fDataToTable(data);
    });
};

function fDataToTable(data, pidtable){
    console.log("fDataToTable" + data);
};

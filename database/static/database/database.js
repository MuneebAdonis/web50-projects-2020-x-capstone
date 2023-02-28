function update_min(){ 
    var min_age_chosen = document.getElementById('min_age').value;
    document.getElementById('max_age').min = min_age_chosen;
}

function commentJS(id){
    var slide_id = parseInt(id);
    //console.log(slide_id);
    var comment_text = document.getElementById('char_typed').value;
    //console.log(comment_text);
    fetch(`/comment/${slide_id}`,{method: 'POST',body: JSON.stringify({comment: comment_text})})
    .then(response => response.json())
    .then(comments => {
        //empty comment field and where the comments are, restore char left
        document.getElementById('char_typed').value = "";
        document.getElementById('comments').innerHTML = "";
        document.getElementById("char_left").innerHTML = "5000/5000 characters remaining";
        //console.log(comments)
        comments.forEach(each_comment =>{
            var new_comment = document.createElement('div'); 
            //got this from stack overflow converts .ISO-8601 formatted date returned from server
            var localDate = new Date(each_comment.date);
            var local_time = localDate.toLocaleTimeString()
            new_comment.innerHTML =`${each_comment.comment}<br>
            -<i><a href ="/profile/${each_comment.person_id}"> ${each_comment.person}</i></a>
            (${each_comment.date_formatted}. ${local_time})<hr>`;
        document.getElementById('comments').append(new_comment);})
        });
}

function get_system(){
    var system_selected = document.getElementById('system').value;
    //console.log(system_selected);
    var selectobject = document.getElementById("tissue");
    // no idea how this delete all works
    var i = 0;
    var ob_len = selectobject.options.length - 1;
    for(i = ob_len; i >= 0; i--) {selectobject.remove(i);}
    var option_all = document.createElement("option")
    option_all.text = "All";
    option_all.value = "all";
    selectobject.add(option_all); 
    fetch(`/filter/${system_selected}`)
    .then(response => response.json())
    .then(data => {
    //console.log(data.length)
    data.forEach((obj, j) => {
    //console.log(obj.tissue);
    var option = document.createElement("option");
    option.text = obj.tissue;
    option.value = obj.tissue
    selectobject.add(option);});
    });
}

function char_left(){
var typed = document.getElementById("char_typed").value.length;
var remaining = 5000 - typed;
document.getElementById("char_left").innerHTML = `${remaining}/5000 characters remaining`;
}

function edit_profile(){
    var info = document.getElementById("info")
    var form = document.getElementById("change_deets")
    if (form.style.display == "none")
    {form.style.display = "block"; info.style.display = "none"} 
    else {form.style.display = "none"; info.style.display = "block"}
}

function change_password(){
    var info = document.getElementById("info")
    var form = document.getElementById("pass_change")
    if (form.style.display == "none"){form.style.display = "block"; info.style.display = "none"} 
    else {form.style.display = "none"; info.style.display = "block"}
}

function checkpword(){
    var one = document.getElementById("passone").value
    var two = document.getElementById("passtwo").value
    //var button = document.getElementById("psave")
    var button = document.getElementsByName("save_btn")[0]
    var message = document.getElementById("match")
    if(one == two){message.innerHTML = "Passwords Match"; button.disabled = false;}
    else {message.innerHTML = "Passwords DO NOT Match", button.disabled = true;}
    
}

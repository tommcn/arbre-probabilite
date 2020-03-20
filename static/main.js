document.addEventListener('DOMContentLoaded', (event) => {
    console.log("DOM content loaded");
});

function addChilds(dataN, elemN)
{
    /* ul span
        li span
        li span
    */
    var ul = document.createElement("ul");
    var keys = Object.keys(dataN);
    for (var i = 0; i < keys.length; i++)
    {
        var li = document.createElement("li");
        var span = document.createElement("span");
        var input = document.createElement("input");
        input.setAttribute("class", "input");
        span.appendChild(input)
        li.appendChild(span);
        ul.appendChild(li); 
        elemN.appendChild(ul)

        input.value = keys[i]; // innerHTML
        if (ul.previousElementSibling.classList != "")
        {
            var before = ul.previousElementSibling.classList;
            for (var j = 0; j < before.length; j++)
            {
                span.classList.add(before[j])
            }
        }
        span.classList.add(input.value); // innerHTML
        input.value = input.value + " -- " + dataN[keys[i]]["chance"]
        addChilds(dataN[keys[i]]["enfants"], li);
    }
    var li = document.createElement("li");
    var span = document.createElement("span");
    var button = document.createElement("button");
    button.innerHTML = "+";
    button.classList.add("button");
//    button.setAttribute("onclick", "alert")
/*
    span.appendChild(button);
    li.appendChild(span);
    ul.appendChild(li); 
    elemN.appendChild(ul)
*/
}


function start()
{
    const input = document.getElementsByClassName('input');
    console.log(input);
    for (var i = 0; i < input.length; i++)
    {
        input[i].disabled = true;
        input[i].parentElement.addEventListener("click", updateValue);
    }

    const buttons = document.getElementsByClassName('button');
    console.log(buttons);
    for (var i = 0; i < buttons.length; i++)
    {
        buttons[i].addEventListener("click", clicked);
    }
    
}

function updateValue(e) {
    console.log(e.target.classList);
    console.log(e.target.value);
    socket.emit("update", {data: {from: e.target.parentElement.classList, 
                                  value: e.target.value}});
}

function clicked(e) {
    var parentList = e.target.parentElement.parentElement.parentElement.previousElementSibling.classList
    console.log(parentList);
    socket.emit('add', {data: {parent: parentList}})
}


var socket = io();
socket.on('connect', function() {
    socket.emit('ask', {data: null});
});
socket.on('JSON', function(msg) {
    data = JSON.parse(msg);
    console.log(data);
    
    var elem = document.getElementById("prob");
    elem.innerHTML = "";
    var add = document.createElement("span")
    add.innerHTML = "Debut";
    elem.appendChild(add);

    addChilds(data, elem);

    start();
});

socket.on('answer', function(msg) {
    ans = msg;
    alert(ans);
});


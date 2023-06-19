


function scrolltoend() {
    $('#board').stop().animate({
        scrollTop: $('#board')[0].scrollHeight
    }, 800);
}

function send(sender, receiver, message) {
    $.post('/api/messages/', '{"sender": "'+ sender +'", "receiver": "'+ receiver +'","message": "'+ message +'" }', function (data) {
        // console.log(data);
        let time = parseInt(data.timestamp.slice(11, 13));
        let fullTime = `${(time > 12)? time-12 : time }:${data.timestamp.slice(14, 16)} ${(time > 12)? 'p.m':'a.m'}`
        text_box = `<div class="card-panel right" style="width: 75%; position: relative">
        <div style="position: absolute; top: 0; left:3px; font-weight: bolder" class="title">{sender}</div>
        {message} <div style="position: absolute; bottom: 2px; right:7px; font-size: 0.8em; font-weight:800; color:#888; display:flex">
        <div>${fullTime}</div><div class="isread"><i class='bx bx-check-double' style="font-size:1.5em;"></i></div></div></div>`;
        var box = text_box.replace('{sender}', "You");
        box = box.replace('{message}', message);
        console.log(box);
        $('#board').append(box);
        scrolltoend();
    })
}

function receive() {
    $.get('/api/messages/'+ sender_id + '/' + receiver_id, function (data) {
        console.log(data);
        if (data.length !== 0)
        {   
            console.log(data, "in condition")
            for(var i=0;i<data.length;i++) {
                console.log(data[i]);
                let time = parseInt(data[i].timestamp.slice(11, 13));
                let fullTime = `${(time > 12)? time-12 : time }:${data[i].timestamp.slice(14, 16)} ${(time > 12)? 'p.m':'a.m'}`
                text_box = `<div class="card-panel right" style="width: 75%; position: relative">
                <div style="position: absolute; top: 0; left:3px; font-weight: bolder" class="title">{sender}</div>
                {message} <div style="position: absolute; bottom: 2px; right:7px; font-size: 0.8em; font-weight:800; color:#888">${fullTime}</div></div>`;
                var box = text_box.replace('{sender}', data[i].sender);
                box = box.replace('{message}', data[i].message);
                box = box.replace('right', 'left blue lighten-5');
                box = box.replace(`<div class="isread"><i class='bx bx-check-double' style="font-size:1.5em;"></i></div>`, " ");
                $('#board').append(box);
                scrolltoend();
            }

            let unreadMsg = document.getElementsByClassName('isread');
            for (let i = 0; i < unreadMsg.length; i++) {
                unreadMsg[i].innerHTML = `<i class='bx bx-check-double' style="color:#4fb6ec; font-size:1.5em;"></i>`;
            }
        }
    })
}

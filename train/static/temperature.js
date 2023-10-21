// function myFunction() {
//     alert("Hello from a static file!");
// }

function p_color(people){
    var color = "";
    if (people >= 0 && people <= 10){
        color = "#5def60";
    }
    else if (people >= 11 && people <= 20){
        color = "yellow";
    }
    else{
        color = "red";
    }
    return color;
}

function check_pnumber(){
    var train_people = [];
    var train = ['head', 'left', 'right', 'end'];

    // 生成四个随机数并将它们添加到数组中
    /*for (var i = 0; i < train.length; i++) {
        var randomNumber = Math.floor(Math.random() * 31); // 生成一个0到30之间的随机数
        train_people.push(randomNumber); 
    }*/
    for(var i = 0; i < 4; i++){
        train_people.push(document.getElementById("people" + String(i+1)).innerText);
    }

    console.log(train_people);

    for (var i = 0; i < train.length; i++) {
        document.getElementById(train[i]).style.backgroundColor = p_color(parseInt(train_people[i]));
        //document.getElementById("people" + String(i+1)).innerHTML = String(train_people[i]);
    }
}


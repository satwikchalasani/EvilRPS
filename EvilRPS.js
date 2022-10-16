
function playButton()
{
    document.getElementById("play-button").style.visibility = "hidden";
    document.getElementById("compPic").style.visibility = "visible";
    document.getElementById("videoelement").style.visibility = "visible";
    let video = document.querySelector("#videoelement");
    if(navigator.mediaDevices.getUserMedia) 
    {
        navigator.mediaDevices.getUserMedia({video : true}).then(function (stream) {video.srcObject = stream;}).catch (function (error) {console.log("Momento de Error")});
    } 
    else 
    {
        console.log("getUserMedia not supported")
    }
    const { spawn } = require('child_process');
    const result =  spawn('python', ['evil.py']);
    console.log(result);

}


function genImg(result)
{
    const rock = ["rock1", "rock2", "rock3", "rock4", "rock5"];
    const paper = ["paper1", "paper2", "paper3", "paper4", "paper5"];
    const scissors = ["scissor1", "scissor2", "scissor3", "rock4", "rock5"];

    let path = "Images/";
    let index = Math.random() * 5;
    if (result === "rock")
    {
        path + rock[index];
    } 
    else if (result === paper)
    {
        path + paper[index];
    }
    else
    {
        path + scissors[index];
    }
    return path;
}


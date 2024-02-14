# Course-Tracker
A scuffed course tracker for BootDev
A project I am making to keep track of the assignments I completed and still have yet to complete in boot.Dev

Paste into console on boot.dev courses page:
```Java
let count = document.querySelector("#__nuxt > div > div.static-bgimage > div > div.flex.h-full.flex-1.flex-col.overflow-auto.align-top > div > div > div.max-w-5xl.flex-1 > section > div > div:nth-child(3) > div:nth-child(4)").querySelectorAll("span.mb-1");
let mySum = 0;
let total = 0;
let completed = 0;
for (const i of count){
    let nArr = i.innerHTML.replaceAll(" ","").split('/');
    mySum += parseInt(nArr[1]);
    mySum -= parseInt(nArr[0]);
    total += parseInt(nArr[1]);
    completed += parseInt(nArr[0]);
}
console.log("Still need to do: " + mySum,"Completed: " + completed, "Total: " + total);
```
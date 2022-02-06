const api = "http://127.0.0.1:5000/Predict";
const errors = document.querySelector(".errors");
const loading = document.querySelector(".loading");
const pred = document.querySelector(".pred");
const results = document.querySelector(".result-container");

results.style.display = "none";
loading.style.display = "none";
errors.textContent = "";



document.addEventListener('DOMContentLoaded',function(){
  document.querySelector('button').addEventListener('click',onclick,false)
  function onclick(){
    chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
   function(tab){
      // chrome.tabs.executeScript(tab.id,{code:"temp=document.title = 'My lame title!'"});
      chrome.tabs.getSelected(null,function(tab) { // null defaults to current window
        const temp = tab.title;
        //alert(temp);// ...
        Call(temp);
        console.log(temp);
      });
   }
  );
  }
},false)

// grab the form
// alert(document.title);
const Call = async Name => {
  loading.style.display = "block";
  errors.textContent = "";
  try {
    fetch(`${api}?name=${Name}`)
    // Converting received data to JSON
    .then(response => response.json())
    .then(json => {
      loading.style.display = "none";
      pred.textContent = json.pred1;
      // pred.textContent=temp;
      results.style.display = "block";
        });
  } catch (error) {
    loading.style.display = "none";
    // pred.textContent=temp;
    results.style.display = "none";
    errors.textContent = "RequestFailed";
  }
};

// declare a function to handle form submission


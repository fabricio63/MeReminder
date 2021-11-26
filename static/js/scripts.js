/*!
* Start Bootstrap - Shop Homepage v5.0.3 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/

var sentinel = document.querySelector('#sentinel');
var cub = document.getElementById("cubito");
var scroll = document.getElementById("scroller");
var load = document.getElementById('load').value;
console.log("cubito");
console.log(cub);
console.log("load");
console.log(load);
  
var intersectionObserver = new IntersectionObserver(entries => {
  // If intersectionRatio is 0, the sentinel is out of view Exit the function
    if (entries[0].intersectionRatio <= 0) {
        return;
    }

    // loadItems();
    console.log("hey sentinel");
    show();
});

// Instruct the IntersectionObserver to watch the sentinel
intersectionObserver.observe(sentinel);

function loadItems(tag) {
  load = parseInt(load) +1;
  load.value = load;

  fetch(`/load?value=${load}&tag=${tag}`)
    .then(response => response.json())

    .then((response) => {
      console.log(response);


      // If empty JSON, exit the function
      if (!response.length) {
        sentinel.innerHTML = "No more posts";
        return;
      }

      for (var i = 0; i < response.length; i++) {
        var clon = cub.content.cloneNode(true);
        clon.getElementById("image").src = response[i];
        clon.getElementById("downloadPht").href = response[i];
        clon.getElementById("link").value = response[i]; 
        clon.getElementById("addPht").href = response[i]; 
        scroll.appendChild(clon);
        
      }
    })
}

function show(){
  var clon = cub.content.cloneNode(true);
  // EDITAR EL TEMPLATE
  clon.getElementById("image").src = "https://images.unsplash.com/photo-1542865399-356dc71be382?crop=entropy&cs=srgb&fm=jpg&ixid=MnwyNTcxMTB8MHwxfHNlYXJjaHwxfHxoZXl8ZW58MHx8fHwxNjMwNjE3MTM0&ixlib=rb-1.2.1&q=85"
  scroll.appendChild(clon);

  var tag = document.querySelector("#title").textContent;
  console.log("tag");
  console.log(tag);

  loadItems(tag);
}
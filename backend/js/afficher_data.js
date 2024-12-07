fetch('/data')
    .then(function(response){
        if (response.ok){
            return response.json();
        }
    })
    .then(function(jsonData){

        const userlist = document.getElementById('user-list');

        jsonData.forEach(function(user){
            var listItem = document.createElement('li');
            listItem.textContent = user.name;
            userlist.appendChild(listItem);
        })
    })
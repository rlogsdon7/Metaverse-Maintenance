//This script contains the functions used for Webhook calls

//Gets the map from Losant, using the map name
function importCSV(name) {
    return fetch('https://triggers.losant.com/webhooks/1i27jbPtOB2enOUd8CvuuaLLH82zgN54L0KzeCcd/name?name='+name)
   .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    return myJson;
  })

}

//Updates the map in Losant, using the map name, and node/link lists
function updateCSV(nodeList,linkList,name) {
  //Update nodes first --- DATA GOES IN BODY
  fetch('https://triggers.losant.com/webhooks/6P2vza5hIEabURKX9NUetfu6I-iRbf0YoJnbSCFA/name?name='+name+'&updateType=nodes',
    {
    method: 'POST',
    body: JSON.stringify(nodeList)
    }
  )
   .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    return myJson;
  })
  //Update links second --- DATA GOES IN BODY
  fetch('https://triggers.losant.com/webhooks/6P2vza5hIEabURKX9NUetfu6I-iRbf0YoJnbSCFA/name?name='+name+'&updateType=links',
    {
    method: 'POST',
    body: JSON.stringify(linkList)
    }
  )
   .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    return myJson;
  })
}

//Gets the device attributes of the selected device, using the map name
function updateParams(desc,user) {
    return fetch('https://triggers.losant.com/webhooks/C62vHLFup_xzqwW5ht3IX9n69um97fwd1-AX4RpI/name?desc='+desc+'&user='+user)
    .then(function(response) {
      return response.json();
    })
    .then(function(myJson) {
      return myJson;
    })
}

//Get user logins
function getUser() {
    return fetch('https://triggers.losant.com/webhooks/-UJ0Y5HJYYa6zjjfKjAMF8jwlr-az3e2xwmdUfAd')
   .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    return myJson;
  })

}

//create User
function createUserLosant(username,password,email,access) {
    return fetch('https://triggers.losant.com/webhooks/40KN4NwZrGjRdL6XyC2WCCkbWnjzD9ot4c3Yz7nI/user?username='+username+'&password='+password+'&email='+email+'&access='+access)
   .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    return myJson;
  })

}

//gets items for dropdown
function getDropDownItems(user) {
    return fetch('https://triggers.losant.com/webhooks/AVJS3UCoGRPECsmv6bJBO_VCPANlJBLW8xPAWq_y/user?username='+user)
   .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    return myJson;
  })

}

//registers a vehicle in Losant
function registerVehicle(desc,type) {
    return fetch('https://triggers.losant.com/webhooks/GVaYnhE7ivzgA2lZlOs4NOsYWUaDDmI3rJ_Xozi2/user?desc='+ desc +'&user='+ user +'&type='+ type)
   .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    return myJson;
  })

}

//removes a vehicle in Losant
function deleteVehicle(desc) {
    return fetch('https://triggers.losant.com/webhooks/3rtVOSieh80nQqlHDb5Qb6Pko4Kj2layuhQRDdAs/user?desc='+ desc +'&user='+ user)
   .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    return myJson;
  })

}

//resets a attribute to 0 for a vehicle in Losant
function replacePartCall(desc) {
    return fetch('https://triggers.losant.com/webhooks/BXavSjfW3eFM9fth87_0zl_2vtcXV8BAzUyiUe3k/user?title='+ desc)
   .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    return myJson;
  })

}

//sends an email with device ID
function sendEmail(desc,user) {
    return fetch('https://triggers.losant.com/webhooks/-qXaN3hfy3a7d5Itub-XKAC91E9SXsmQqZWl12Ax/user?desc='+ desc +'&user='+ user)
   .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    return myJson;
  })

}

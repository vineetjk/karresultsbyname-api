const results = require('./data/sample-data.js');

const express = require('express');

const app = express();

app.get('/', function(req, res){
  res.send('Welcome to Our NameWiseResults API')
});

app.get('/api/results', function(req, res){
 
    var response = [];
    if( typeof req.query.Name != 'undefined' ){
        response = results.filter(function(result){
          if(result.Name.toLowerCase().includes(req.query.Name.toLowerCase())){
            return result;
          }
        });
      } else {
        response = results;
      }
    res.json(response);
  });

app.listen(3000, function(){
  console.log('this app is listening on port 3000!')
});
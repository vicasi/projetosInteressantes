// imports
const express = require('express');
const bodyParser = require('body-parser');
const date = require(__dirname + '/date.js')

// initializations
const app = express();

// app uses
app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'))

// globals
let itemsL = [];
let workItem = []

// endpoint
app.get('/', function (req, res, err) {
    let day = date.getday()
    res.render('list', { listTitle: day, newListItem: itemsL });
});

// newListItem: item
app.post('/', function (req, res, err) {
    let item = req.body.newItem;
    if(req.body.list === 'work'){
        workItem.push(item)
        res.redirect('/work')
    }else{
        itemsL.push(item);
        res.redirect('/');
    }
});
app.get('/work', function(req, res, err){
    res.render('list', {newListItem: workItem, listTitle:'work'})
})


// app listen
app.listen(3000, function (req, res, err) {
    console.log('running');
});

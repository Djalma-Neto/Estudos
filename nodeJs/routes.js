var express = require('express')
var app = express()
const Sequelize = require('sequelize')
const router = express.Router()
const bodyParser = require('body-parser')
const handlebars = require('express-handlebars')

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.engine('handlebars', handlebars({defaultLayout: 'main'}))
app.set('view engine', 'handlebars')

router.get('/', function(req, res) {
    res.render('home/index')
})

router.get('/form', function(req, res) {
    res.render('home/insert')
})

router.get('/teste', (req, res) => {
    allUser('select * from usuario', res)
});

router.post('/insert', function(req, res) {
    insertUser(req, res)
})

app.listen(8000, function() {
    console.log('http://localhost:8000')
})


app.use('/', router)

function conectar() {
    const sequelize = new Sequelize('nodejs', 'root', 'password', {host: "127.0.0.1", dialect: "3306"})
    sequelize.authenticate().then(()=> {
        console.log('conected !!')
    }).cath((err)=> {
        console.log('fail: ' + err)
    })
    return sequelize
}

function allUser(query, res) {
    const conect = conectar()

    var resp
    conect.query(query, function(error, results, fields) {
        if (error)
            resp =  error
        else
            resp = results
            res.render('home/list', {user: resp})
        conect.end()
    })
}

function insertUser(req, res) {
    const conect = conectar()
    var resp
    var nome = req.body.nome
    var idade = req.body.idade
    var email = req.body.email
    var query = `insert into usuario (nome, idade, email) values(${nome}, ${idade}, ${email})`
    console.log(query)

    conect.query("insert into usuario (nome) values()", function(error, results, fields) {
        if (error)
            resp =  error
        else
            resp = results
        res.send(resp)
        conect.end()
    })
}
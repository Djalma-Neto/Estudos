var mysql = require('mysql')

var conect = mysql.createConnection({
    host: "127.0.0.1",
    port: "3306",
    user: "root",
    password: "password",
    database: "nodejs"
})
conect.connect(function(err) {
    if (err) throw err
    console.log("Connected!")
})
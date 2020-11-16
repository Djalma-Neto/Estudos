module.exports = app => {
  const mysql = require('mysql2')
 
  const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    database: 'mp3',
    password: '1998'
  })

  return connection
}

module.exports = () => {
  const customerWalletsDB = require('../data/customerWallets.json')
  const connection = require('../../config/db.js')()
  const controller = {}

  controller.listCustomerWallets = (req, res) => {
    res.status(200).json(customerWalletsDB)
  }

  controller.sigin = async (req, res) => {
    console.log(req.body)
    let date = new Date()
    var nome = String(req.body.nome)
    var email = String(req.body.email)
    var password = String(req.body.password)
    if(!nome || !email || !password){
      res.status(200).json({err: 'Falta dados'})
      return
    }
    var created = `${date.getFullYear()}-${date.getMonth()}-${date.getDate()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`
    var updated = `${date.getFullYear()}-${date.getMonth()}-${date.getDate()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`
    var query = `INSERT INTO usuario(nome, email, password, created, updated) values('${nome}', '${email}', '${password}', '${created}', '${updated}')`
    await connection.query(
      query, (err, results, fields) => {
        if(err){
          res.status(200).json(err)
          return
        }
        res.status(200).json(results)
      }
    )
  }

  controller.listar = async (req, res) => {
    console.log(req.body)
    await connection.query(
      'SELECT * FROM usuario',(err, results, fields) => {
        if(err){
          res.status(200).json(err)
          return
        }
        res.status(200).json(results)
      }
    )
  }

  return controller
}
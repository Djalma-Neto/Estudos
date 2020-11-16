module.exports = app => {
  const controller = require('../controllers/controller')()

  app.route('/sigin')
    .post(controller.sigin)

  app.route('/listar')
    .post(controller.listar)

  app.route('/upload')
    .post(controller.listar)
}
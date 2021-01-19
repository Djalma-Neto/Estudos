const { Client } = require('pg')

function connect() {
    const client = new Client({
      user: 'postgres',
      host: 'localhost',
      database: 'teste',
      password: '1998',
      port: 5432,
    })
}

export default connect


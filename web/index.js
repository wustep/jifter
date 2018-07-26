const express = require('express')
const path = require('path')
const app = express()

console.log(path.join(__dirname,'/../','.env'));
require('dotenv').config({path: path.join(__dirname,'/../','.env')})
const port = process.env.WEB_PORT || 8111;

app.use('/', express.static(path.join(__dirname, 'src')))
app.listen(port, () => console.log(`Server: Listening on port ${port}!`))

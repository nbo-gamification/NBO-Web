// server.js

import http from 'http'
import express from 'express'
import bodyParser from'body-parser'
import morgan from 'morgan'
import render from './server/server.js'

const ADDRESS = process.env.NODE_HOST || 'localhost'
const PORT = process.env.NODE_PORT || '3000'

const app = express()
const server = http.Server(app)

function buildInitialState(body) {
  return { user: 'manu'}
}

app.use(bodyParser.json({ limit: '10mb' }))

app.use(morgan('combined'))

app.post('/', function (req, res) {
  res.end('Render server here!')
})

app.post('/render', function (req, res) {
  const body = req.body 
  const result = render(body)

  res.json({
    'html': result.html,
    'props': result.props,
    'finalState': result.finalState
  })
})

server.listen(PORT, ADDRESS, function () {
  console.log('Render server listening at http://' + ADDRESS + ':' + PORT)
})

export default server;
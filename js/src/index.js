// server.js

import http from 'http'
import express from 'express'
import bodyParser from'body-parser'
import morgan from 'morgan'
// import { buildInitalState } from './utils'
import render from './server/server_func.js'

const ADDRESS = process.env.NODE_HOST || 'localhost'
const PORT = process.env.NODE_PORT || '3000'

const app = express()
const server = http.Server(app)

function buildInitialState(body) {
  return { user: 'manu'}
}
// I've increased the limit of the max payload size in case a huge page
// needs to be rendered
app.use(bodyParser.json({ limit: '10mb' }))

// Morgan is the very silly name of some logging middleware.
// It logs requests to the console so that you can tell that
// the server is doing anything.
app.use(morgan('combined'))

app.get('/', function (req, res) {
  res.end('Render server here!')
})

app.post('/render', function (req, res) {
  // We know we'll need a path and the data for our initial state,
  // so let's save this stuff first
  const url = req.body.url
  // This function massages data into the shape of our Redux store
  const initialState = buildInitialState(req.body)  
  
  const result = render(url, initialState)
  console.log(result)

  res.json({
    html: result.html,
    finalState: result.finalState
  })
})

server.listen(PORT, ADDRESS, function () {
  console.log('Render server listening at http://' + ADDRESS + ':' + PORT)
})

export default server;
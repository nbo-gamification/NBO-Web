import React from 'react'
import { Provider } from 'react-redux'
import { match, RouterContext } from 'react-router'
import ReactDOMServer from 'react-dom/server'
import App from '../App';

function getRoutes(store) {
  return [{path: "/", url: "/", isExact: true, params: {}} ]
}

export default function render (url, initialState) {
  // const store = configureStore(initialState)
  const store = initialState

  const routes = getRoutes(store)

  let html, redirect;

  // match({ routes, url }, (error, redirectLocation, renderProps) => {
  //   console.log("------Match----")
  //   console.log("error: ", error)
  //   console.log("url: ", url)
  //   console.log("redirectLocation: ", redirectLocation)
  //   console.log("renderProps: ", renderProps)


  //   if (redirectLocation) {
  //     redirect = redirectLocation.pathname
  //   } else if (renderProps) {
  //     // Here's where the actual rendering happens
  //     html = ReactDOMServer.renderToString(
  //       <Provider store={store}>
  //         <RouterContext {...renderProps} />
  //       </Provider>
  //     )
  //   }
  // })

  // if (redirect) return render(redirect, initialState) // Fun recursion

  // html = App()

  // if (!html) {
  //   html = "<p> Manu </p>"
  // }
  html = "<html><p>Manu</p></html>";


  // const finalState = store.getState()

  const finalState = initialState;

  return {
    html,
    finalState
  }
}


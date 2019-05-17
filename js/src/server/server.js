import React from 'react'
import App from '../App';
import { renderToString } from 'react-dom/server';
import { StaticRouter } from 'react-router-dom';

function getRoutes(store) {
  return [{path: "/login", url: "/", isExact: true, params: {}} ]
}

export default function render (app, props) {
  const context = {
    'props': props
  };
  const markup = (
    <StaticRouter context={context} location={app}>
      <App />
    </StaticRouter>
  );

  const comp = renderToString(
    <body>
      <div id="root">{markup}</div>
    </body>
  );

  return {
    'html': comp,
    'props': markup.props,
    'finalState': markup._store
  }
}


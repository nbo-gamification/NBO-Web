import React from 'react'
import ReactDOM from 'react-dom'

const UserLogin = ({users}) =>{
	return (
		<div>
        	<h1>Login</h1>
		</div>
	)
}
    


ReactDOM.render(
    React.createElement(UserLogin, window.props),
    window.react_mount,                
)

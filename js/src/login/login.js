import React from 'react';
import './login.css';

import InputField from 'eventbrite_design_system/inputField/InputField';
import Password from 'eventbrite_design_system/password/Password';
import Button from 'eventbrite_design_system/button/Button';
import {
  TYPE_SUBMIT,
  STYLE_FILL,
  SIZE_BLOCK,
} from 'eventbrite_design_system/button/constants';

class Login extends React.Component {
  render() {

    return (
      <div>
        {/* <div >
            <InputField
              id="email"
              name="email"
              label='Email address'
              type="email"
              role="textbox"
            />
        </div>
        <div>
            <Password
              name="password"
              id="password"
              role="textbox"
              required={true}
              autoFocus={true}
              label='Password'
              data-automation="signup-password-field"
              isV2={true}
              style="dynamic"
              bottomSpacing={0}
            />
        </div>
        <div>
          <Button
            type={TYPE_SUBMIT}
            style={STYLE_FILL}
            size={SIZE_BLOCK}
            data-automation="signup-submit-button"
          >Log in
          </Button>
        </div> */}
      </div>
    );
  }
}

export default Login;

import "./custom.scss";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import React from "react";
import { store, history } from "./store";

import { Route, Switch } from "react-router-dom";
import { ConnectedRouter } from "react-router-redux";

import App from "./components/App";
import I18n from "redux-i18n";


const translations = {
  en: {
    // header
    "Language": "Language",
    "Sign in": "Sign in",
    "Sign up": "Sign up",
    "French" : "French",
    "English" : "English",
    "New Item" : "New Item",
    "Settings" : "Settings",
    // login
    "Email" : "Email",
    "Password": "Password",
    "Need an account?": "Need an account?",
    "SIGN IN": "SIGN IN",
    // register
    "SIGN UP": "SIGN UP",
    "Username": "Username",
    "Have an account?": "Have an account?"

  },
  fr: {
    'Language': "Langue",
    "Sign in": "S'identifier",
    "Sign up": "S'inscrire",
    "French" : "français",
    "English" : "Anglais",
    "New Item" : "Nouvel article",
    "Settings" : "Paramètres",

    // login
    "Sign In": "S'identifier",
    "SIGN IN": "S'IDENTIFIER",
    "Email" : "E-mail",
    "Password": "Mot de passe",
    "Need an account?": "Besoin d'un compte??",
    
    // register
    "Sign Up": "S'inscrire",
    "SIGN UP": "S'INSCRIRE",
    "Username": "Nom d'utilisateur",
    "Have an account?": "Avoir un compte??"
  },
};



ReactDOM.render(
  <Provider store={store}>
    <I18n translations={translations}>
      <ConnectedRouter history={history}>
        <Switch>
          <Route path="/" component={App} />
        </Switch>
      </ConnectedRouter>
    </I18n>
  </Provider>,

  document.getElementById("root")
);

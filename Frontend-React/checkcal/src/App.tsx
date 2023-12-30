import React from 'react';
import './App.css';
import Navigator from './services/navigator'


function App() {
   return (
   <AccessPage loginState={true}><Navigator/></AccessPage>
  );
}

export default App;

type AccessPageType = {
  loginState: boolean;
  children: any;
}
const AccessPage = (props: AccessPageType) => {
return props.loginState?(props.children):(<></>)

}
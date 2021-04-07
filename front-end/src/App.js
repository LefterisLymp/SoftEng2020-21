import React, { Component } from "react";
import { HashRouter as Router, Route, Redirect } from "react-router-dom";
import Nav from './Nav';
import Main from './Main';
import { Login, Logout } from './Authorization';
import { UserProvider } from './UserContext';
import SeoStatistics from './SeoStatistics';
import BankRead from './BankRead';
import Bank from './Bank';
import SeoStatistics_charts from './SeoStatistics_charts';
import UserStatistics from './UserStatistics';
import ChargingDataStatistics from './ChargingDataStatistics';


class App extends Component {

  constructor(props) {
    super(props)
    this.state = {
      token: props.userData.token,
      username: props.userData.username,
      id: props.userData.id,
      style: {
        backgroundColor:'#F5F5F5',
        height:'100vh'
      },
      setUserData: (token, username, id) => this.setState({
        token: token,
        username: username,
        id: id
      }),
    };
  }

  Protected(ProtectedComponent) {
    if (this.state.username !== null) {
      return  (props) => <ProtectedComponent {...props} />;
    }
    else {
      return (props) => <Redirect to='/login' />;
    }
  }

  render() {
    return (
        <div style={this.state.style}>
          <UserProvider value={this.state}>
            <Router>
              <div className='container'>
                <Nav />
                <Route path="/" exact render={(props) => {
                  return <h1>Welcome {this.state.username === null? '' :'Back '+this.state.username}</h1>;
                }}/>
                <Route path="/main" render={this.Protected(Main)} />
                <Route path="/login" component={Login} />
                <Route path="/logout" render={this.Protected(Logout)} />
                <Route path="/SeoStatistics" render={this.Protected(SeoStatistics)} />
                <Route path="/SeoStatistics_charts" render={this.Protected(SeoStatistics_charts)} />
                <Route path="/BankRead" render={this.Protected(BankRead)} />
                <Route path="/Bank" render={this.Protected(Bank)} />
                <Route path="/UserStatistics" render={this.Protected(UserStatistics)} />
                <Route path="/ChargingDataStatistics" render={this.Protected(ChargingDataStatistics)} />
                <footer>
                  <p>All rights reserved @OrthodoxCoders</p>
                  <p>Find us on <a href="https://github.com/ntua/TL20-66">GitHub
                  </a></p>
                </footer>
              </div>
            </Router>
          </UserProvider>
        </div>
    );
  }
}
export default App;

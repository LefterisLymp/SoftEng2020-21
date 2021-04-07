import React, { Component } from 'react';
import { UserContext } from './UserContext';
import './Authorization.css';
export class Login extends Component {        
    
    static contextType = UserContext;
    constructor(props) {
        super(props);
        this.username = React.createRef();
        this.password = React.createRef();
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    
    handleSubmit(event) {
        const usname = this.username.current.value;
        const pass = this.password.current.value;
        fetch('http://localhost:5000/evcharge/api/login',{
            method: 'POST',
            headers: {
                'Content-Type':'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                "username": usname,
                "password": pass
            })
        }).then((response) => response.json())
        .then(json => {   
            localStorage.setItem('token', json.token);
            localStorage.setItem('id', json.id);
            localStorage.setItem('username', usname);
            this.context.setUserData(json.token,usname.json.id);           
            this.props.history.push('/main');
        }).catch( function(error) {alert("Username or password isn't valid");});
        
        event.preventDefault();
    }
    
    render() {        
        return (         
            <div class="back">                       
            <div class="div-center">  
            <div class="content">
            <form onSubmit={this.handleSubmit}>
                <div class="form-group">
                <label for="username">Όνομα χρήστη:</label>
                <input id="username" class="form-control" type="text" ref={this.username} required/>
                </div>
                <div class="form-group">
                <label for="password">Κωδικός Πρόσβασης: </label>
                <input id="password" class="form-control" type="password" ref={this.password}  required/>
				</div>
                <button class="btn btn-primary" align="center" type="submit">Submit</button>
            </form>
            </div>
            </div>
            </div>
        );
    }   
}
export class Logout extends Component {
    static contextType = UserContext;
    Remove() {
        localStorage.removeItem('username');
        localStorage.removeItem('token');
        localStorage.removeItem('id');
        this.context.setUserData(null, null);        
        this.props.history.push('/');
    }
    componentDidMount() {
        fetch('http://localhost:5000/evcharge/api/logout',{
            method: 'POST',
            headers: {
                'X-OBSERVATORY-AUTH': this.context.token,
                'Content-Type':'application/x-www-form-urlencoded',
            }
        }).then(() => this.Remove());
    }
    render() {
        return (<h2>See you soon</h2>);
    }
}

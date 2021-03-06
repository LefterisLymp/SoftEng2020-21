import React, { Component } from 'react';
import { Link, withRouter } from "react-router-dom";
import { UserConsumer } from './UserContext';
import "./Nav.css";

const css = {fullWidth: {width:'100%'}}

//Based on Bootsrap

const NavLink = props => {    
    const link = <Link className="nav-link" to={props.to}>{props.label}</Link>;
    if (props.to === props.location) {
        return <li className="nav-item active">{link}</li>
    }
    else {
        return <li className="nav-item">{link}</li>
    }    
}

class Menu extends Component {
    render() {
        if (this.props.context.username) {
            return (
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav mr-auto">               
                        <NavLink label="Κεντρική" to="/main" location={this.props.location.pathname} />
                        <NavLink label="Αποσύνδεση" to='/logout' location={this.props.location.pathname} />
                        <NavLink label="ΣΕΟ" to='/SeoStatistics' location={this.props.location.pathname} />
                        <NavLink label="Λογαριασμοί" to='/BankRead' location={this.props.location.pathname} />
                        <NavLink label="Στατιστικά Χρήστη" to='/UserStatistics' location={this.props.location.pathname} />
                    </ul>                                      
                </div>
            );
        }
        else {
            return (
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav mr-auto">               
                        <NavLink label="Είσοδος" to="/login" location={this.props.location.pathname} />                        
                    </ul>                                      
                </div>                
            );
        }
    }
}

const UserAvatar = props => {
    if (props.context.username) {
        return (
            <span className='navbar-text'>{props.context.username}</span>
        );
    }
    else {
        return null;
    }
}

class Nav extends Component {    
    render() {
        return (            
            <div className="row">
                <nav className="navbar navbar-expand-lg navbar-dark bg-dark" style={css.fullWidth}>
                    <Link className="navbar-brand" to="/">EV Charge</Link>
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <UserConsumer>
                    { context => 
                        <React.Fragment>
                            <Menu 
                                location={this.props.location} 
                                context={context}
                            />
                            <UserAvatar context={context} />
                        </React.Fragment>
                    }
                    </UserConsumer>
                </nav>
            </div>
        );
    }
}

export default withRouter(Nav);

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import 'bootstrap';
import App from './App';

const userData = {
    token: localStorage.getItem('token'),
    username: localStorage.getItem('username'),
    id: localStorage.getItem('id')
};
ReactDOM.render(<App userData={userData} />, document.getElementById('root'));

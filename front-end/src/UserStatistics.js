import React, { Component } from 'react';
// import Select, { components } from 'react-select';
// import Dropdown from 'react-dropdown';
//import 'react-dropdown/style.css';
import { UserContext } from './UserContext';
import './Seo.css';

class UserStatistics extends Component {
    static contextType = UserContext;


    constructor(props){
        super(props);
        this.state={from_date: "from_date",
            to_date: "to_date",
            tabletype:"UserToVehicle",
        };
    }

        show=()=> {
        var validation=true;
        let tok = this.context.token;
        console.log(tok);
        let from_date = this.state.from_date.value;
        let to_date = this.state.to_date.value;

        this.setState({validation:true});
        console.log(from_date);
        console.log(to_date);
        var url='http://localhost:5000/evcharge/api/UserToVehicle/' + this.context.id;
        console.log(url);
        console.log(tok);
        console.log(this.context.token);
        if(validation===true){
            fetch(url,{
                method: 'GET',
                headers: {
                    'X-OBSERVATORY-AUTH':tok,
                }
            }).then((response) =>{console.log(response.status);
                if(response.status===402){
                    return response.text().then(resp => alert(resp));
                }
                else{
                    return response.json();
                    }
            }).then((data) => {
                console.log(data);
                var url = 'http://localhost:5000/evcharge/api/SessionsPerEV/'+data[0].id+'/'+this.state.from_date+'/'+this.state.to_date + "?format=json";
                return fetch(url,{
                method: 'GET',
                headers: {
                    'X-OBSERVATORY-AUTH':tok,
                    'verify': false
                },
            })
            }).then((response) =>{console.log(response.status);
            if(response.status===400){
                response.text().then(resp => alert(resp));
            }
            else if(response.status===403) {
                response.text().then(resp => alert(resp));
            }
            else{
                response.text().then(json=>{
                    localStorage.setItem('data',json);
                    localStorage.setItem('dateFrom',this.state.from_date);
                    localStorage.setItem('dateTo',this.state.to_date);
                    this.props.history.push('/ChargingDataStatistics');})}})

        }
    }

    handleChangeFromdateinput=(event)=>{
        this.setState({from_date:event.target.value});
    }

    handleChangeToDateInput=(event)=>{
        this.setState({to_date:event.target.value});
    }
    
    handledateChangetabletype=(event)=>{
        this.setState({tabletype:event.target.value});
    }

    render() {
        return (
            <React.Fragment>
			<div align="center">

                <label>
                    Από:&nbsp;
                </label>
                { <input id="from_date" name="from_date" type="text" placeholder="YYYY-MM-DD" onChange={this.handleChangeFromdateinput}  />}
                <br></br>
                <label>
                    Εως:&nbsp;
                </label>
                {<input id="to_date" name="to_date" type="text" placeholder="YYYY-MM-DD"  onChange={this.handleChangeToDateInput}  />}

                <br></br>
                <form onSubmit={this.show}>
                    <br></br>

                    <button className="btn btn-info" type="submit">
                        Υποβολή
                    </button>
                </form>
            </div>
            </React.Fragment>
        );
    }
    
}

export default UserStatistics;

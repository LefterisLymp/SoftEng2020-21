import React, { Component } from 'react';
// import Select, { components } from 'react-select';
// import Dropdown from 'react-dropdown';
//import 'react-dropdown/style.css';
import { UserContext } from './UserContext';
import './Seo.css';

class SeoStatistics extends Component {
    static contextType = UserContext;

    constructor(props){
        super(props);
        this.state={from_date: "from_date",
            to_date: "to_date",
            station_id: "station_id",
            tabletype:"SessionsPerStation"
        };
    }

        show=()=> {
        var validation=true;
        let tok = this.context.token;
        //let station_id = this.state.station_id.value;
        var arr= this.state.from_date.split('-');
        var year=undefined,month=undefined,day=undefined;
        if(arr.length===3) {
         year=arr[2];
         month=arr[1];
         day=arr[0];
         this.state.from_date=year+'-'+month+'-'+day;
        }
        var to_arr = this.state.to_date.split("-");
        var year=undefined,month=undefined,day=undefined;
        if(to_arr.length===3) {
         year=to_arr[2];
         month=to_arr[1];
         day=to_arr[0];
         this.state.to_date=year+'-'+month+'-'+day;
        }

        console.log(month);
        console.log(day);
        console.log(year);
        this.setState({validation:true});
        var url='http://localhost:5000/evcharge/api/SessionsPerStation/' + this.state.station_id + '/'+ this.state.from_date +'/'+ this.state.to_date+'?format=json';
        console.log(url);
        console.log(tok);
        console.log(this.context.token);
        if(validation===true){
            fetch(url,{
                method: 'GET',
                headers: {
                    'X-OBSERVATORY-AUTH':tok,
                },
            }).then((response) =>{console.log(response.status);
                console.log(response);
                if(response.status===401){
                    response.text().then(resp => alert(resp));
                    this.props.history.push('/Logout');
                }else if(response.status===402){
                    response.text().then(resp => alert(resp));
                }else if(response.status===403){
                    response.text().then(resp => alert(resp));
                }else if(response.status===400){
                    response.text().then(resp => alert(resp));
                }
                else{
                    response.text().then(json=>{
                        console.log(json);
                        localStorage.setItem('data',json);
                    this.props.history.push('/SeoStatistics_charts');
                    })}
                }
            )}}

    handleChangeFrom_date=(event)=>{
        this.setState({from_date:event.target.value});
    }

    handleChangeTo_date=(event)=>{
        this.setState({to_date:event.target.value});
    }
    
    handledateChangetabletype=(event)=>{
        this.setState({tabletype:event.target.value});
    }

    handleChangeStation_id=(event)=>{
        this.setState({station_id:event.target.value});
    }
    render() {
        return (
            <React.Fragment>
			<div align="center">

                <label>
                 <p class="font-weight-bold">Προσθέστε την περίοδο για την οποία θέλετε να ελέγξετε</p>
                </label>

				<br></br>
                <label>Από:</label>
                <br></br>
                {<input id="from_date" name="from_date" type="text" placeholder="DD-MM-YYYY" value={this.state.email} onChange={this.handleChangeFrom_date}  />}
                <br></br>
                <label>Έως:</label>
                <br></br>
                {<input id="to_date" name="to_date" type="text" placeholder="DD-MM-YYYY" value={this.state.email} onChange={this.handleChangeTo_date}  />}
                <br></br>
                <br></br>

                <form onSubmit={this.handleSubmit}>
                    <label>
                    Σταθμός φόρτισης:
                    <br></br>
                    <input type="text" value={this.state.value} onChange={this.handleChangeStation_id}/>
                    </label>
                    </form>

				<br></br>
                <form onSubmit={this.show}>
					<br></br>

                    <button class="btn btn-info" type="submit">
                        Υποβολή 
                    </button>
                </form>
				</div> 
            </React.Fragment>

        );
    }
    
}

export default SeoStatistics;

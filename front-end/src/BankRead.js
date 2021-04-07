import React, { Component } from 'react';
import { UserContext } from './UserContext';

class BankRead extends Component{
    static contextType = UserContext;

    print=()=>{
        let date_from = this.date_from.value;
        let date_to = this.date_to.value;
        var check = false;

        var url='http://localhost:5000/evcharge/api/UserToVehicle/'+this.context.id;
        var tok = this.context.token;
        //Έλεγχος ημερομηνίας από
        var arr1 = date_from.split('-');
        var year=undefined,month=undefined,day=undefined;
        if(arr1.length==3){
         year=arr1[0];
         month=arr1[1];
         day=arr1[2];
        } else{
            check=false
        }
        this.setState({check:false});
        if (day>31 || day<1 || month>12 || month<1 || year>2020 || year <1990 ){
            check=true;
            alert("Η ημερομηνία από: είναι λανθασμένη");
        }
        else if ((day===undefined || month===undefined || year===undefined)){
            check=true;
            alert("Η ημερομηνία από: είναι λανθασμένη");
        }
        //Έλεγχος ημερομηνίας εώς
        var arr2 = date_to.split('-');
        var year=undefined,month=undefined,day=undefined;
        if(arr2.length==3){
         year=arr2[0];
         month=arr2[1];
         day=arr2[2];
        } else{
            check=false
        }
        this.setState({check:false});
        if (day>31 || day<1 || month>12 || month<1 || year>2020 || year <1990 ){
            check=true;
            alert("Η ημερομηνία εώς: είναι λανθασμένη");
        }
        else if ((day===undefined || month===undefined || year===undefined)){
            check=true;
            alert("Η ημερομηνία εώς: είναι λανθασμένη");
        }


        if(check===false){
        
        fetch(url, {
            method: 'GET',
            headers: {
                'X-OBSERVATORY-AUTH':tok,
                },
            }).then(function(response) {
            return response.json(); 
          }).then(function(data) {
            var vehicleID =  data[0].id;
        
            console.log(vehicleID, '\n');
          
            return fetch('http://localhost:5000/evcharge/api/SessionsPerEV/'+vehicleID+'/'+date_from+'/'+date_to, {
                method: 'GET',
                headers: {
                    'X-OBSERVATORY-AUTH':tok,
                    },
                });
          }).then(function(response) {
            return response.text();
          }).then(function(r) {
            localStorage.setItem('data',r);
            this.props.history.push('/Bank');
        }.bind(this));
    }
    }

    render(){
        return (
            <React.Fragment>
                <div align="center">
                    <p class="font-weight-bold" >Προσθέστε την περίοδο για την οποία θέλετε να ελέγξετε τα έξοδα σας...</p>
                    <label>
                        Ημερομηνία Από:
                        <br></br>
                        <input id="date_from" name="date_from" type="text" placeholder="YYYY-MM-DD"  ref = {(input)=> this.date_from = input} required />
                    </label> 
                        <br></br>
                    <label>
                        Ημερομηνία Εώς:
                        <br></br>
                        <input id="date_to" name="date_to" type="text" placeholder="YYYY-MM-DD"  ref = {(input)=> this.date_to = input} required />
                    </label>
                        <br></br>
                    <form onSubmit={this.print}>
                        <br></br>
                        <button class="btn btn-info" type="submit" >Υποβολή</button>
                    </form>
                </div>
            </React.Fragment>
         );
    }
}

export default BankRead;

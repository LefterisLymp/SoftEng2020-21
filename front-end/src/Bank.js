import React, { Component } from 'react';
import './Bank.css';

function getJson_totalCost(arr){
  var p=0;
  for (var i = 0; i < arr.length; i++){
    p = p + parseInt(arr[i].SessionCost);
}return p;}

function getJson_SessionID(arr){
    var si = arr[0].VehicleChargingSessionsList
    return si;
}

function getPoints(x){
    var y = (10*x)/2;
    return y;
}

class Bank extends Component {
    
	constructor(props) {
    super(props)
    this.state = {
      json: [],
  	  TotalCost: getJson_totalCost(this.getdata())
    }
  }

  componentDidMount() {
    this.setState((prevState) => {
      return {
        json: this.getdata()
      }
    })
  }
    getdata=()=>{
        var read = localStorage.getItem('data');
        console.log(JSON.parse(read));
        var fixed = getJson_SessionID(JSON.parse(read));//.split("'").join("\"");
        //console.log(fixread);
        //var fixed = JSON.parse(fixread);
        console.log(fixed);
		    return fixed;
    }

    render() {
		return (
		  <div align="center">
		  <h3 id='title'>Το Συνολικό Κόστος Για Αυτή Τη Περίοδο</h3>
			<table class="table table-striped">
			  <thead class="thead-dark" align="center">
                <tr>
				<th scope="col">Session ID</th>
        <th scope="col">Energy Delivered</th>
				<th scope="col">Payment Method</th>
				<th scope="col">Session Cost</th>
                </tr>
			  </thead>
			  <tbody>
				{this.state.json.map((data, index) => {
				  return (
					<tr key={index}>
					  <td scope="row" align="center">{data.SessionID}</td>
            <td scope="row" align="center">{data.EnergyDelivered}</td>
            <td scope="row" align="center">{data.PricePolicyRef}</td>
            <td scope="row" align="center">{data.SessionCost}</td>
					</tr>
				  )
				})
                }
			  </tbody>
			</table>
      <p class="font-italic">Το συνολικό κόστος για το όχημα σας, τη περίδο αυτή ήταν:<b> {this.state.TotalCost} ευρώ</b></p>
      <p class="font-italic">Οι πόντοι σας, τη περίδο αυτή ήταν:<b> {getPoints(this.state.TotalCost)}</b></p>
      </div>
		);
	}
}
 export default Bank;
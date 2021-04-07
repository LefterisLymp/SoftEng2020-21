import React, { Component } from 'react';

function getTotalEnergyDelivered(arr){console.log(arr[0]); var y = arr[0].TotalEnergyDelivered; console.log(y); return y;}

function getNumberOfChargingSessions(arr){var y = arr[0].NumberOfChargingSessions; console.log(y); return y;}

function getNumberOfActivePoints(arr){var y =  arr[0].NumberOfActivePoints; console.log(y); return y;}

function getSessionsSummaryList(arr){var y = arr[0].SessionsSummaryList; console.log(y); return y;}

function getPointID(arr){
    var c=[];
    for (var i = 0; i < arr.length; i++){
        var b = JSON.parse(arr[i]);
       c.push(b.PointID);
  } return c;}

function getEnergyDelivered(arr){
    var c=[];
    for (var i = 0; i < arr.length; i++){
        var b = JSON.parse(arr[i]);
       c.push(b.EnergyDelivered);
  } console.log(c); return c;}

  function getPointSessions(arr){
    var c=[];
    for (var i = 0; i < arr.length; i++){
        var b = JSON.parse(arr[i]);
       c.push(b.PointSessions);
  } console.log(c); return c;}

function getVehicleID(arr) {
    var d=[];
    console.log(arr)
    for (var i = 0; i < arr.length; i++) {
        var b = JSON.parse(arr[i]);
        var c = b.Vehicles;
        for (var j = 0; j < c.length; j++) {console.log(c[j]); d.push(c[j].VehicleId);
    }} console.log(d); return d;}

function getVehicleBrand(arr) {
    var d=[];
    console.log(arr)
    for (var i = 0; i < arr.length; i++) {
        var b = JSON.parse(arr[i]);
        var c = b.Vehicles;
        for (var j = 0; j < c.length; j++) {console.log(c[j]); d.push(c[j].VehicleBrand);
    }} console.log(d); return d;}


    
class SeoStatistics_charts extends Component {    constructor(props){
    super(props);
    this.state = {
        total_energy_delivered: getTotalEnergyDelivered(this.showdata()),
        number_of_charging_sessions: getNumberOfChargingSessions(this.showdata()),
        number_of_active_points: getNumberOfActivePoints(this.showdata()),
        session_summmary_list: getSessionsSummaryList(this.showdata()),
        vehicle_ids: getVehicleID(this.showdata()[0].SessionsSummaryList),
        vehicle_brands: getVehicleBrand(this.showdata()[0].SessionsSummaryList),
        point_ids: getPointID(this.showdata()[0].SessionsSummaryList),
        energy_delivered: getEnergyDelivered(this.showdata()[0].SessionsSummaryList),
        point_sessions: getPointSessions(this.showdata()[0].SessionsSummaryList)
        }
}
showdata=()=>{
        var read = localStorage.getItem('data');
        var fixed = JSON.parse(read);
        console.log(JSON.parse(read));
		    return fixed;
    }


static defaultProps = {
    displayTitle:true,
}
    render() {
        return (
            <div align="center">
		  <h3 id='title'>Η κατάσταση του σταθμού για αυτή την περίοδο:</h3>
          <p class="font-italic">Η συνολική κατανάλωση ενέργειας για τον σταθμό ήταν:<b> {this.state.total_energy_delivered} kWh</b></p>
          <br></br>
          <p class="font-italic">Τα οχήματα που πέρασαν από τον σταθμό σας είναι:</p>
          <br></br>
        
			<table class="table table-striped">
			  <thead class="thead-dark" align="center">
                <tr>
				<th scope="col">Vehicle ID</th>
            <th scope="col">Vehicle Brand</th>
                </tr>
			  </thead>
			  <tbody>
              {this.state.vehicle_ids.map((vehicle_ids, index) => {
				  return (
					    <tr key={index}>
					    <td scope="row" align="center">{this.state.vehicle_ids[index]}</td>
                        <td scope="row" align="center">{this.state.vehicle_brands[index]}</td>
					</tr>
				  )
				})
                }
                
				
			  </tbody>
			</table>

            <br></br>

            <p class="font-italic">Στατιστικά ανά σημείο φόρτισης</p>

            <table class="table table-striped">
			  <thead class="thead-dark" align="center">
                <tr>
				<th scope="col">Charging Point ID</th>
                <th scope="col">Energy Delivered</th>
                <th scope="col">Number of sessions</th>
            
                </tr>
			  </thead>
			  <tbody>
              {this.state.point_ids.map((vehicle_ids, index) => {
				  return (
					    <tr key={index}>
					    <td scope="row" align="center">{this.state.point_ids[index]}</td>
                        <td scope="row" align="center">{this.state.energy_delivered[index]} kWh</td>
                        <td scope="row" align="center">{this.state.point_sessions[index]}</td>
					</tr>
				  )
				})
                }
                
				
			  </tbody>
			</table>

            </div>
        );
    }
}

 export default SeoStatistics_charts;

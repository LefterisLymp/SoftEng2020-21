import React, { Component } from 'react';
import 'react-dropdown/style.css';
import {Bar} from 'react-chartjs-2';

function getJson_SessionID(arr){
    var si = arr[0].VehicleChargingSessionsList
    return si;
}

function getStartDate(arr){
    var d=[];
    for (var i = 0; i < arr.length; i++){
      if(i == 20)break;
      d.push(arr[i].StartedOn);
      console.log(arr[i].StartedOn)
    }
    return d;
}

function getEnergyDelivered(arr) {
    var d = [];
    for (var i = 0; i < arr.length; i++) {
        if(i == 20)break;
        d.push(arr[i].EnergyDelivered);
        console.log(arr[i].EnergyDelivered)
    }
    return d;
}
function getYearRange(start, end) {
    var d = [];
    for (var i = parseInt(start); i <= parseInt(end); i++) {
        d.push(i);
        console.log(i)
    }
    return d;
}
function getYearCounts(arr, start, end, data) {
    var d = [];
    for (var i = 0; i <= parseInt(end) - parseInt(start); i++) {
        var acc = 0;
        for (var j = 0; j < data.length; j++) {
            if(parseInt(data[j].StartedOn.split('-')[0])  === arr[i]) {
                acc = acc + 1;
            }
        }
        d.push(acc);
    }
    return d;
}

String.prototype.lpad = function(padString, length) {
    var str = this;
    while (str.length < length)
        str = padString + str;
    return str;
}

function getMonthRange(start, end) {
    var d = [];
    for (var i = parseInt(start); i <= parseInt(end); i++) {
        for (var j = 1; j <= 12; j++) {
            d.push(i.toString().lpad("0",2) + "-" + j.toString().lpad("0",2));
            console.log(i)
        }
    }
    return d;
}

    function getMonthCounts(arr, start, end, data) {
        var d = [];
        for (var i = 0; i <= parseInt(end) - parseInt(start); i++) {
            for (var k = 1; k <= 12; k++) {
                var acc = 0;
                for (var j = 0; j < data.length; j++) {
                    if (data[j].StartedOn.split('-')[0] + "-" + data[j].StartedOn.split('-')[1] === arr[i * 12 + k-1]) {
                        acc = acc + 1;
                    }
                }
                d.push(acc);
            }
        }
        return d;
    }

    class ChargingDataStatistics extends Component {
        constructor(props) {
            super(props)
            this.state = {
                json: []
            }
        }

        componentDidMount() {
            this.setState((prevState) => {
                return {
                    json: this.getdata(),
                    startDate: this.getInputStartDate(),
                    endDate: this.getInputEndDate()
                }
            })
        }

        getdata = () => {
            var read = localStorage.getItem('data');
            console.log(JSON.parse(read));
            var fixed = getJson_SessionID(JSON.parse(read));
            console.log(fixed);
            return fixed;
        }
        getInputStartDate = () => {
            var read = localStorage.getItem('dateFrom');
            return read.split('-')[0];
        }
        getInputEndDate = () => {
            var read = localStorage.getItem('dateTo');
            return read.split('-')[0];
        }

        render() {
            return (
                <div className="charts">
                    <Bar
                        data={{
                            labels: getYearRange(this.state.startDate, this.state.endDate),
                            datasets: [
                                {
                                    label: 'Αριθμός φορτίσεων ανά έτος',
                                    data: getYearCounts(getYearRange(this.state.startDate, this.state.endDate), this.state.startDate, this.state.endDate, this.state.json),
                                    backgroundColor: 'rgb(255, 99, 132)'
                                }]
                        }}
                        width={100}
                        height={50}
                        options={{
                            responsive: true,
                            title: {
                                display: true,
                                text: 'Αριθμός φορτίσεων ανά έτος',
                                fontSize: 25
                            },
                            legend: {
                                display: false,
                            }
                        }}
                    />
                    <Bar
                        data={{
                            labels: getMonthRange(this.state.startDate, this.state.endDate),
                            datasets: [
                                {
                                    label: 'Αριθμός φορτίσεων ανά μήνα',
                                    data: getMonthCounts(getMonthRange(this.state.startDate, this.state.endDate), this.state.startDate, this.state.endDate, this.state.json),
                                    backgroundColor: 'rgb(255, 99, 132)'
                                }]
                        }}
                        width={100}
                        height={50}
                        options={{
                            responsive: true,
                            title: {
                                display: true,
                                text: 'Αριθμός φορτίσεων ανά μήνα',
                                fontSize: 25
                            },
                            legend: {
                                display: false,
                            }
                        }}
                    />
                    <Bar
                        data={{
                            labels: getStartDate(this.state.json),
                            datasets: [
                                {
                                    label: 'Ενέργεια φόρτισης',
                                    data: getEnergyDelivered(this.state.json),
                                    backgroundColor: 'rgb(255, 99, 132)'
                                }]
                        }}
                        width={100}
                        height={50}
                        options={{
                            responsive: true,
                            title: {
                                display: true,
                                text: 'Ενέργεια ανα φόρτιση τελευταίων 20 φορτίσεων',
                                fontSize: 25
                            },
                            legend: {
                                display: false,
                            }
                        }}
                    />
                </div>

            );
        }
    }

    export default ChargingDataStatistics;
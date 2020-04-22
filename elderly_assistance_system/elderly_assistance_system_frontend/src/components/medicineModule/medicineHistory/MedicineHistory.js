import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import {getMedicineHistory} from '../../../actions/medicineHistory';

import { ResponsiveCalendar } from '@nivo/calendar';
import medHistoryJson from "./data.js"


const MyResponsiveCalendar = ({inputData}) => (
    <ResponsiveCalendar
        data= {inputData}

        from="2015-03-01"
        to="2016-07-12"
        emptyColor="#eeeeee"
        colors={[  '#f47560' , '#61cdbb']}
        minValue="auto"
        margin={{ top: 40, right: 40, bottom: 40, left: 40 }}
        yearSpacing={40}
        monthBorderColor="#ffffff"
        dayBorderWidth={2}
        dayBorderColor="#ffffff"
        legends={[
            {
                anchor: 'top-right',
                direction: 'row',
                translateY: 36,
                itemCount: 4,
                itemWidth: 42,
                itemHeight: 36,
                itemsSpacing: 14,
                itemDirection: 'right-to-left'
            }
        ]}
    />

)

export class MedicineHistory extends Component {
    static propTypes = {
        medicineHistory: PropTypes.array.isRequired,
        getMedicineHistory: PropTypes.func.isRequired,
    };

    componentDidMount() {
        this.props.getMedicineHistory();
        
    }

    

    render() {

        //After 4 hours finally 
        var results = this.props.medicineHistory.filter(medicine_history => medicine_history.name === "Napa");
        console.log(results);

        return (
            
            <Fragment>
                <h2>Medicine History</h2>
                

                <div style={{height:600}}>
                    <MyResponsiveCalendar inputData={medHistoryJson}  />
                </div>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Date</th>
                            <th>Time</th>
                            <th>Consumed</th>
                            <th>Time of consumption</th>
                            
                        </tr>
                    </thead>
                    <tbody>
                        { this.props.medicineHistory.map( (medicine_history, index) => (
                            <tr key={index}>
                                <td>{medicine_history.id}</td>
                                <td>{medicine_history.name}</td>
                                <td>{medicine_history.date}</td>
                                <td>{medicine_history.time}</td>
                                <td>{medicine_history.consumed}</td>
                                <td>{medicine_history.time_of_consumption}</td>
                                
                            </tr>
                        ))}


                        
                    </tbody>
                </table>
            </Fragment>
        )
    }
}

const mapStateToProps = state => ({
    medicineHistory: state.medicineHistory.medicine_history //here 'medicineHistory' is the reducer in reducer/index.js, and 'medicine_history' is the passed parameter medicineHistory.js file in same folder
})

export default connect(mapStateToProps, { getMedicineHistory })(MedicineHistory);



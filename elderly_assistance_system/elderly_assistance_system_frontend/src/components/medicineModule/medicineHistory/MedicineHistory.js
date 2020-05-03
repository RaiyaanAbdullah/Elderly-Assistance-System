import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import {getMedicineHistory} from '../../../actions/medicineHistory';


import { ResponsiveCalendar } from '@nivo/calendar';
import medHistoryJson from "./data.js"


const MyResponsiveCalendar = ({inputData}) => (
    <ResponsiveCalendar
        data= {inputData}

        from="2020-01-01"
        to="2020-12-31"
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
        getMedicineHistory: PropTypes.func.isRequired
    };

    componentDidMount() {

        
        this.props.getMedicineHistory();
        
    }

    

    render() {

 

        //We aim to show the consumption graph of each medicine for each different time. First we join the names and times of all medicines.
        var name_time = this.props.medicineHistory.map( (medicine_history) => medicine_history.name +' ' + medicine_history.time  );
        //We derive the unique set
        var name_time_unique = name_time.filter((item, index) => name_time.indexOf(item) === index);

        var all_results = this.props.medicineHistory.filter( medicine_history => medicine_history.name  );
        
        console.log(name_time);
        console.log(name_time_unique);
        console.log(all_results);

        //need to clean this code
        const yo=[]
        
        for (const [index, value] of name_time_unique.entries()) {
            const yooo=[]
            for (const [index2, value2] of all_results.entries()) {
                const key1 = "day";
                const key2 = "value";
                const vale1 = value2.date;
                const vale2 = value2.consumed ? 1: 0;
                if (value === value2.name+' '+value2.time) {
                        yooo.push({  [key1]: vale1 , [key2]: vale2  });
                }
            }
            yo.push(
                <div style={{height:600}}>
                    <MyResponsiveCalendar inputData={yooo}  />
                </div>
            )
        }

        

        return (
            
            <Fragment>
                <h2>Medicine History</h2>
                
                {yo}

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



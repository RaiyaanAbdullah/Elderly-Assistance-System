import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import {getMedicine} from '../../../actions/medicine';
import {getMedicineHistory} from '../../../actions/medicineHistory';




export class MedicineHistory extends Component {
    static propTypes = {
        medicineHistory: PropTypes.array.isRequired,
        getMedicineHistory: PropTypes.func.isRequired,
        medicine: PropTypes.array.isRequired,
        getMedicine: PropTypes.func.isRequired

    };

    componentDidMount() {
        this.props.getMedicine();
        this.props.getMedicineHistory();
    }
    render() {
        var medicine_list=this.props.medicine;

        // This code matches the id in medicine with medicine_id in medicineHistory, and provides the name and time for that particular medicine to medicineHistory
        for ( let list_index in this.props.medicine){
            for (let history_index in this.props.medicineHistory){ 
                if (this.props.medicine[list_index].id == this.props.medicineHistory[history_index].medicine_id) {

                    this.props.medicineHistory[history_index].name = this.props.medicine[list_index].name;
                    this.props.medicineHistory[history_index].time = this.props.medicine[list_index].time;
                }
            }
        }

        return (
            
            <Fragment>

                <h2>Medicine History</h2>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Time</th>
                            <th>Date</th>

                            <th>Consumed</th>
                            <th>Time of consumption</th>
                        </tr>
                    </thead>
                    <tbody>
                        { this.props.medicineHistory.map( (medicine_history, index) => (
                            <tr key={index}>
                                <td>{medicine_history.id}</td>
                                <td>{medicine_history.name}</td>
                                <td>{medicine_history.time}</td>
                                
                                <td>{medicine_history.date}</td>

                                <td>{medicine_history.consumed.toString()}</td>
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
    medicineHistory: state.medicineHistory.medicine_history, //here 'medicineHistory' is the reducer in reducer/index.js, and 'medicine_history' is the passed parameter medicineHistory.js file in same folder
    medicine: state.medicine.medicine
})

export default {
    MedicineHistory: connect(mapStateToProps, { getMedicineHistory , getMedicine})(MedicineHistory)
}

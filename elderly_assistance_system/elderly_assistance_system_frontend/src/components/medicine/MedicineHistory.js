import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import {getMedicineHistory} from '../../actions/medicineHistory';

export class MedicineHistory extends Component {
    static propTypes = {
        medicineHistory: PropTypes.array.isRequired,
        getMedicineHistory: PropTypes.func.isRequired
    };

    componentDidMount() {
        this.props.getMedicineHistory();
    }

    render() {
        return (
            <Fragment>
                <h2>Medicine History</h2>
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



import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { updateMedicine} from '../../../actions/medicine';

export class FormUpdate extends Component {

    state = {
        id:'',
        name: '',
        time: '',
        start: '',
        drawer: ''
    }

    static propTypes = {
        updateMedicine: PropTypes.func.isRequired
    }
    onChange = e => this.setState({ [e.target.name] : e.target.value});

    onSubmit = e => {
        e.preventDefault();
        const {id, name, time, started, drawer} = this.state;
        const medicine = {id,name, time, started, drawer};
        this.props.updateMedicine(medicine);
        this.setState({
            name: "",
            time: "",
            //started not added because the next medicine might be started at the same time
            drawer: ""
        })
    }
    render() {
        const {id,name, time, started, drawer} = this.state;
        return (

            <div className="card card-body mb-5">
                <h2>Update Medicine</h2>
                <form onSubmit={this.onSubmit}>
                <div className="form-group">
                    <label>ID</label>
                    <input className="form-control" type="number" name="id" onChange={this.onChange} value={id}/>
                </div>
                <div className="form-group">
                    <label>Name</label>
                    <input className="form-control" type="text" name="name" onChange={this.onChange} value={name}/>
                </div>
                <div className="form-group">
                    <label>Time</label>
                    <input className="form-control" type="time" name="time" onChange={this.onChange} value={time}/>
                </div>
                <div className="form-group">
                    <label>Started</label>
                    <input className="form-control" type="datetime-local" name="started" onChange={this.onChange} value={started}/>
                </div>
                <div className="form-group">
                    <label>Drawer no.</label>
                    <input className="form-control" type="number" name="drawer" onChange={this.onChange} value={drawer}/>
                </div>
                <div className="form-group">
                    <button type="submit" className="btn yellow-background">Update</button>
                </div>
                </form>
            </div>

        )
    }
}

export default connect(null, {updateMedicine})(FormUpdate);

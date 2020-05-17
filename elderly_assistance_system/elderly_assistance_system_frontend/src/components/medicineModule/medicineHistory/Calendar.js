import React, { Component } from "react";
import { Calendar, momentLocalizer } from "react-big-calendar";
import moment from "moment";
import "react-big-calendar/lib/css/react-big-calendar.css";

const localizer = momentLocalizer(moment);

class MyCalendar extends Component {



    render() {
        return (

            <Calendar
                localizer={localizer}
                defaultDate={new Date()}
                defaultView="month"
                events={this.props.MedicineRecords}  //MedicineRecords is received from parent
                style={{ height: "100vh" }}
                eventPropGetter={event => ({
                    style: {
                        backgroundColor: event.consumed ? "#00eb00": "#ff1a1a",
                        color: event.consumed ? "#000": "#fff"
                         
                    }
                })}
            />

        );
    }
}

export default MyCalendar;
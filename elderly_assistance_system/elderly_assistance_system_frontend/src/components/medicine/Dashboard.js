import React, { Fragment } from 'react';
import ReactDom from "react-dom";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";


export default function Dashboard() {
    return (

            <Fragment>
                <div className="row">
                    
                    <div className="col-6">
                        <Link to="/manage-medicine">
                            <div className="homepage-tile vertically-middle black-opaque-border round-border-all">
                                <h2 className="dark-grey text-center w-100">Manage Medicine</h2>
                            </div>
                        </Link>
                    </div>
                    
                    <div className="col-6">
                        <Link to="/medicine-history">
                            <div className="homepage-tile vertically-middle black-opaque-border round-border-all">
                                <h2 className="dark-grey text-center w-100">View Medicine Records</h2>
                            </div>
                        </Link>
                    </div>                    
                    
                </div>
            </Fragment>

        

            
            

    )
}

import {React} from "react";
import './landing.css'
import { Link } from "react-router-dom";
function LandingPage(){
    return(
        <div>
            <div className='hero-img'>
                <div className='heading'>
                    <h1 className="text-right mt-5">Green<span>Global</span></h1>
                    <p className="text-right lead">Connecting Your Local Farmer With The Far-end Buyer!</p>
                    <br />
                    <Link to='/sign-up'className="btn" >Register </Link>
                </div>
                
            </div>

        </div>
        
    )
}
export default LandingPage
import './css/styles.css';
import Navbar from './components/navbar';

function LandingPage(){
    return(
        <div className='landingPage-Container'>
            <Navbar/>
            <div className='heading'>“Welcome to a New Way of Voting!”</div>
        </div>
    );
}

export default LandingPage;
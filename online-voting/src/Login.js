import './css/styles.css';
import votingImage from './images/login.png';

function Login() {
    const handleClick = () => {
        alert("Button clicked!"); // Replace this alert with any action you want
    };

    return (
        <div className='login-container'>
            <div className="container">
                <div className="image-section">
                    <img src={votingImage} alt="Voting Illustration" />
                </div>
                <div className="form-section">
                    <h2>Enter Your Voting ID</h2>
                    <input type="text" placeholder="Enter your ID here" />
                    <a href="#">Click here for face recognition.</a>
                    <div className="button-container">
                        <button onClick={handleClick}>Continue</button>
                    </div>
                </div>
            </div>
        </div>
      );
}

export default Login;
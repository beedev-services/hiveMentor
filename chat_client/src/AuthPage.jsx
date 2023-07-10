import axios from "axios";
let theKey = 'BeeDevServices'

const AuthPage = (props) => {
    const onSubmit = (e) => {
        e.preventDefault();
        const { value } = e.target[0];
        console.log(value)
        axios.post(
            // 'http://localhost:3001/authenticate',
            'http://127.0.0.1:8000/chat/authenticate/',
            { username: value }
        )
        console.log('username', value, 'key', value+theKey)
        props.onAuth({ username: value, secret: value+theKey })
    }

    return (
        <div className="background">
            <form onSubmit={onSubmit} className="form-card">
                <div className="form-title">
                    Welcome 👋
                </div>

                <div className="form-subtitle">
                    Set a username to get started
                </div>

                <div className="auth">
                    <div className="auth-label">Username</div>
                    <input className="auth-input" name="username" />
                    <button className="auth-button" type="submit">Enter</button>
                </div>
            </form>
        </div>
    );
}

export default AuthPage
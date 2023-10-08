import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'


function Main({setTheUser}) {

    const [theUser, setTheUserLocal] = useState('');
    const [theLoggedUser, setTheLoggedUser] = useState('')
    const [version, setVersion] = useState('multi'); // Default to 'multi ' version
    const navigate = useNavigate();
    const [info, setInfo] = useState('')
    const [invalid, setInvalid] = useState('')

    useEffect(() => {
        window.addEventListener('message', function(event) {
        const logUser = event.data.user;
        setTheLoggedUser(logUser)
        })
    },[])

    const handleVersionChange = (event) => {
        setVersion(event.target.value)
    }

    useEffect(() => {
        // GET request using fetch inside useEffect React hook
        if (theLoggedUser) {
            fetch(`http://127.0.0.1:8000/api/loggedUser/${theLoggedUser}/`)
            // fetch(`https://dev.beemindful-buzz.com/api/loggedUser/${theLoggedUser}/`)
            // fetch(`https://beemindful-buzz.com/api/loggedUser/${theLoggedUser}/`)
            .then(response => response.json())
            .then(data => setInfo(data));
        }
    // empty dependency array means this effect will only run once (like componentDidMount in classes)
    }, [theLoggedUser]);
    console.log('useEffect api base',info.user)

    const handleSubmit = (e) => {
        e.preventDefault()
        setTheUser(theUser)
        if(theUser === info.user) {
            if (version === 'multi') {
                navigate('/multi')
            } else {
                navigate('/single')
            } 
        } else {
            setInvalid('Invalid username')
            console.log('updated',invalid)
        }
    }

    return (
        <>
        <h1>Please enter your user name to proceed to chat</h1>
        <span className='messages'>{invalid}</span>
        <form>
            <label>
                Username:
                <input type="text" value={theUser} onChange={(e) => setTheUserLocal(e.target.value)} />
            </label>
            <label>
                Chose Chat Version Single Chat vs Multi (all) Chat:
                <select value={version} onChange={handleVersionChange}>
                    {/* <option value="single">Single</option> */}
                    <option value="multi">Multi</option>
                </select>
            </label>
            <button onClick={handleSubmit}>Submit</button>
        </form>
        </>
    )
}
export default Main

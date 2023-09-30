import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'


function Main({setTheUser}) {

    const [theUser, setTheUserLocal] = useState('');
    const [version, setVersion] = useState('multi'); // Default to 'multi ' version
    const navigate = useNavigate();
    const [loggedUser, setLoggedUser] = useState('')
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        window.addEventListener('message', function(event) {
            const logged = event.data.user
            console.log(event.data)
            setLoggedUser(logged)
        })
    },[])
    useEffect(() => {
        if(loggedUser != '') {
            setIsLoading(false)
        }
    }, [loggedUser])

    const handleVersionChange = (event) => {
        setVersion(event.target.value)
    }
    const handleSubmit = (e) => {
        e.preventDefault()
        setTheUser(theUser)
        if (version === 'multi') {
            navigate('/multi')
        } else {
            navigate('/single')
        }
    }
    console.log("loggedUser", loggedUser, 'isloading', isLoading)
    if(isLoading) {
        return <div>
            <h1>Welcome to the Chat</h1>
            <h2>Page Is Loading ........</h2>
        </div>
    }

    return (
        <>
        <h1>Please enter your user name to proceed to chat</h1>
        {loggedUser}
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

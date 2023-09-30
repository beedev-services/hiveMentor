import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'


function Main({setTheUser}) {

    const [theUser, setTheUserLocal] = useState('');
    const [version, setVersion] = useState('multi'); // Default to 'multi ' version
    const navigate = useNavigate();

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

    return (
        <>
        <h1>Please enter your user name to proceed to chat</h1>
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

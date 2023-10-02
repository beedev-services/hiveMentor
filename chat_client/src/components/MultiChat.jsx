import React, { useEffect, useState } from 'react'
import { useMultiChatLogic, MultiChatSocket, MultiChatWindow } from "react-chat-engine-advanced";
import './key.js'


function MultiChat(props) {
    
    const { theUser } = props;
    // console.log('from props', theUser.theUser)
    const mySecret = process.env.REACT_APP_CHATENGINE_SECRET
    // const proj = '34e251b1-74c5-4888-b1b1-e56e45673e6e'
    const proj = process.env.REACT_APP_CHATENGINE_PROJ
    // const [user, setUser] = useState('')
    const [theMode, setTheMode] = useState("")
    const [isLoading, setIsLoading] = useState(true);
    // setUser(theUser)
    useEffect(() => {
        window.addEventListener('message', function(event) {
        const mode = event.data.mode;
        setTheMode(mode)
        })
    },[])

    useEffect(() => {
        console.log('State has been updated', theMode);
        setIsLoading(false)
    }, [theMode]);

    const projectId = proj
    const username = theUser['theUser']
    const secret = theUser['theUser']+mySecret
    const chatProps = useMultiChatLogic(projectId, username, secret);



    if(isLoading) {
        return <div>
            <h1>Welcome to the Chat</h1>
            <h2>Page Loading ........</h2>
        </div>
    }

    return (
        <>
        <div id="theMode" className={theMode === 'dark' ? 'dark' : ''}>
        <MultiChatSocket {...chatProps} />
        <MultiChatWindow  {...chatProps} style={{ height: '100vh' }} />
        {/* {console.log('theName', theName)} */}
    </div>
        </>
    )
}
export default MultiChat
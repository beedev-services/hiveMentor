import React, { useEffect, useState } from 'react'
import { useMultiChatLogic, MultiChatSocket, MultiChatWindow } from "react-chat-engine-advanced";
import './key.js'


function MultiChat() {
    var VITE_CHATENGINE_PROJ='d8ef4f3b-9aca-42d6-8557-d21979acf880'
    var VITE_CHATENGINE_SECRET='BeeDevTechSquadServices'

    const [theName, setTheName] = useState("")
    const [theSecret, setTheSecret] = useState("")
    const mySecret = VITE_CHATENGINE_SECRET
    // const proj = '34e251b1-74c5-4888-b1b1-e56e45673e6e'
    const proj = VITE_CHATENGINE_PROJ
    const [theMode, setTheMode] = useState("")
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        window.addEventListener('message', function(event) {
        const userId = event.data.user;
        const mode = event.data.mode;
        // console.log('event.data.user = userId', userId)
        setTheName(userId)
        setTheSecret(userId+mySecret)
        setTheMode(mode)
        // console.log('in useEffect', theName, theSecret, theMode)
        setIsLoading(false)
        })
    },[])
    // console.log('in useEffect', theName, theSecret, theMode)

    useEffect(() => {
      // This will run whenever theName, theSecret, or theMode changes
        console.log('State has been updated', theName, theSecret, theMode);
    }, [theName, theSecret, theMode]);

    const projectId = proj
    const username = theName
    const secret = theSecret
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
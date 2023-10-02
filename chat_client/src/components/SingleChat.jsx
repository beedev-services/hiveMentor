import React, { useEffect, useState } from 'react'
import { SingleChatSocket, ChatFeed, useSingleChatLogic } from 'react-chat-engine-advanced';
import { useParams } from 'react-router-dom'

function MultiChat() {

    const [theName, setTheName] = useState("")
    const [theSecret, setTheSecret] = useState("")
    const mySecret = import.meta.env.VITE_CHATENGINE_SECRET
    const proj = import.meta.env.VITE_CHATENGINE_PROJ
    const [theMode, setTheMode] = useState("")
    const [theChat, setTheChat] = useState("")
    const [theChatAccess, setTheChatAccess] = useState("")
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        window.addEventListener('message', function(event) {
        const userId = event.data.user;
        const mode = event.data.mode;
        const chatName = event.data.chatID
        const chatAccess = event.data.chatAccess
        // console.log('event.data.user = userId', userId)
        setTheName(userId)
        setTheSecret(userId+mySecret)
        setTheMode(mode)
        setTheChat(chatName)
        setTheChatAccess(chatAccess)
        // console.log('in useEffect', theName, theSecret, theMode)
        setIsLoading(false)
        })
    },[])
    // console.log('in useEffect', theName, theSecret, theMode)

    useEffect(() => {
      // This will run whenever theName, theSecret, or theMode changes
        console.log('State has been updated', theName, theSecret, theMode, theChat);
    }, [theName, theSecret, theMode, theChat, theChatAccess]);

    const projectId = proj
    const chatAccessKey = theChatAccess
    const chatId = theChat
    const senderUsername = theName
    const chatProps = useSingleChatLogic(projectId, chatId, chatAccessKey);


    if(isLoading) {
        return <div>
            <h1>Welcome to the Chat</h1>
            <h2>Page Loading ........</h2>
        </div>
    }

    return (
        <>
        <div id="theMode" className={theMode === 'dark' ? 'dark' : ''}>
        <ChatFeed {...chatProps} username={senderUsername} />
        <SingleChatSocket  {...chatProps} style={{ height: '100vh' }} />
    </div>
        </>
    )
}
export default MultiChat
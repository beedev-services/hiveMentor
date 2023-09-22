import React, { useEffect, useState } from 'react'
import './App.css'
import { ChatEngine, ChatList } from 'react-chat-engine';
import { useMultiChatLogic, MultiChatSocket, MultiChatWindow } from "react-chat-engine-advanced";
import axios from 'axios'
import loading from './assets/loading.gif';
import IceBreaker from './components/IceBreaker';


function App() {
  
  const [theName, setTheName] = useState("")
  const [theSecret, setTheSecret] = useState("")
  const mySecret = import.meta.env.VITE_CHATENGINE_SECRET
  // const proj = '34e251b1-74c5-4888-b1b1-e56e45673e6e'
  const proj = import.meta.env.VITE_CHATENGINE_PROJ
  const [theMode, setTheMode] = useState("")
  const [isLoading, setIsLoading] = useState(true);


  useEffect(() => {
    window.addEventListener('message', function(event) {
      const userId = event.data.user;
      const mode = event.data.mode;
      console.log('event.data.user = userId', userId)
      setTheName(userId)
      setTheSecret(userId+mySecret)
      setTheMode(mode)
      console.log('in useEffect', theName, theSecret, theMode)
      setIsLoading(false)
    })
  },[])
  console.log('in useEffect', theName, theSecret, theMode)

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
    <div id="theMode" className={theMode === 'dark' ? 'dark' : ''}>
      
        {/* <ChatEngine
          projectID={proj}
          userName={theName}
          userSecret={theSecret}
          height='100vh'

        /> */}
        {/* <MultiChatSocket {...chatProps} />

        <MultiChatWindow 
          chats={chatProps.chats}
          messages={chatProps.messages}
          activeChatId={chatProps.activeChatId}
          username={chatProps.username}
          peopleToInvite={chatProps.peopleToInvite}
          hasMoreChats={chatProps.hasMoreChats}
          hasMoreMessages={chatProps.hasMoreMessages}
          onChatFormSubmit={chatProps.onChatFormSubmit}
          onChatCardClick={chatProps.onChatCardClick}
          onChatLoaderShow={chatProps.onChatLoaderShow}
          onMessageLoaderShow={chatProps.onMessageLoaderShow}
          onMessageLoaderHide={chatProps.onMessageLoaderHide}
          onBottomMessageShow={chatProps.onBottomMessageShow}
          onBottomMessageHide={chatProps.onBottomMessageHide}
          onMessageFormSubmit={chatProps.onMessageFormSubmit}
          onInvitePersonClick={chatProps.onInvitePersonClick}
          onRemovePersonClick={chatProps.onRemovePersonClick}
          onDeleteChatClick={chatProps.onDeleteChatClick}
          style={{ height: '100vh' }} 
        /> */}
        <MultiChatSocket {...chatProps} />
        <MultiChatWindow  {...chatProps} style={{ height: '100vh' }} />
        {console.log('theName', theName)}
    </div>
  )
}

export default App
import React, { useEffect, useState } from 'react'
import './App.css'
import { ChatEngine } from 'react-chat-engine';
import axios from 'axios'
import loading from './assets/loading.gif';
import IceBreaker from './components/IceBreaker';

function App() {
  const [theName, setTheName] = useState("")
  const [theSecret, setTheSecret] = useState("")
  const secret = 'BeeDevTechSquadServices'
  // const proj = '34e251b1-74c5-4888-b1b1-e56e45673e6e'
  const proj = 'd8ef4f3b-9aca-42d6-8557-d21979acf880'
  const [theMode, setTheMode] = useState("")
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    window.addEventListener('message', function(event) {
      const userId = event.data.user;
      const mode = event.data.mode;
      console.log('event.data.user = userId', userId)
      setTheName(userId)
      setTheSecret(userId+secret)
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

  if(isLoading) {
    return <div>
      <h1>Welcome to the Chat</h1>
      <h2>Page Loading ........</h2>
    </div>
  }

  return (
    <div id="theMode" className={theMode === 'dark' ? 'dark' : ''}>
      
        <ChatEngine
          projectID={proj}
          userName={theName}
          // userName='webmaster'
          userSecret={theSecret}
          // userSecret='webmasterBeeDevServices'
          renderIceBreaker={(chat) => {<h1>Welcome to The Buzz, BeeMindful-Buzz 's chat</h1>}}
          renderChatSettings={(chatAppState) => {}}
        />
        {console.log('theName', theName)}
    </div>
  )
}

export default App
import React, { useEffect, useState } from 'react'
import './App.css'
import { ChatEngine } from 'react-chat-engine';
import axios from 'axios'
import loading from './assets/loading.gif';

function App() {
  const [theName, setTheName] = useState("")
  const [theSecret, setTheSecret] = useState("")
  const secret = 'BeeDevServices'
  const proj = '34e251b1-74c5-4888-b1b1-e56e45673e6e'
  const [theMode, setTheMode] = useState("")

  useEffect(() => {
    window.addEventListener('message', function(event) {
      // console.log('i am in event listener function inside useEffect')
      const userId = event.data.user;
      const mode = event.data.mode;
      console.log('event.data.user = userId', userId)
      setTheName(userId)
      // setTheName('webmaster')
      setTheSecret(userId+secret)
      setTheMode(mode)
      // setTheSecret('webmasterBeeDevServices')
    })
  },[])
  // if (!theName || !theSecret) {
  //   return <div class=loading>
  //     <h1>Logging you into Chat</h1>
  //     <img src={loading} alt="Loading" />
  //     </div>; // or any loading indicator
  // }

  return (
    <div id="theMode" className={theMode === 'dark' ? 'dark' : ''}>
      
        <ChatEngine
          projectID={proj}
          // userName={theName}
          userName='webmaster'
          // userSecret={theSecret}
          userSecret='webmasterBeeDevServices'
        />
        {console.log('theName', theName)}
    </div>
  )
}

export default App
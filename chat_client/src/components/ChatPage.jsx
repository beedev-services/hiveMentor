import React, { useEffect, useState } from 'react'
import { ChatEngine } from 'react-chat-engine';
import axios from 'axios'
import {useParams} from 'react-router-dom'

const ChatPage = () => {
    const {userId} = useParams()
    console.log('userid', userId)

  // useEffect(() => {
  //   axios.get(`http://127.0.0.1:8000/chat/authenticate/${userId}/`)
  //     .then(response => {
  //       response
  //       console.log('the results', response)
  //     })
  // })

    return (
        <>
            <ChatEngine
                // projectID='8b626c35-8c33-4491-a1ef-d021890a4fd3'
                projectID='34e251b1-74c5-4888-b1b1-e56e45673e6e'
                // projectId='34e251b1-74c5-4888-b1b1-e56e45673e6e'
                userName='webmaster'
                userSecret='webmasterBeeDevServices'
            />
        </>
    )
}

export default ChatPage
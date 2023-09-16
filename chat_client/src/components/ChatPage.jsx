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
                projectID='d8ef4f3b-9aca-42d6-8557-d21979acf880'
                userName='webmaster'
                userSecret='webmasterBeeDevServices'
            />
        </>
    )
}

export default ChatPage
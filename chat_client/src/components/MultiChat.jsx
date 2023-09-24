import React, {useEffect} from 'react'
import { useMultiChatLogic, MultiChatSocket, MultiChatWindow } from "react-chat-engine-advanced";

function MultiChat(props) {


    useEffect(() => {
        let projectId = props.proj
        let username = props.theName
        let secret = props.theSecret
        let dark = props.theName
        console.log("can you see me?",dark)
    }, [username, secret, projectId, dark])
    

    // const chatProps = useMultiChatLogic(projectId, username, secret);

    return (
        <>
        {/* <MultiChatSocket {...chatProps} />
        <MultiChatWindow  {...chatProps} style={{ height: '100vh' }} /> */}
        </>
    )
}
export default MultiChat
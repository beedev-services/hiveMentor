// import { PrettyChatWindow } from 'react-chat-engine-pretty';
import { ChatEngine } from 'react-chat-engine';

const ChatsPage = (props) => {

    // console.log(import.meta.env.VITE_CHAT_ENGINE_PROJECT_ID, 'progID')
    // console.log('props.username', props.user.username, 'props.secret', props.user.secret)
    return (
        <div className="background">
            <div className='chat-wrapper'>
                {/* <PrettyChatWindow
                    projectId={import.meta.env.VITE_CHAT_ENGINE_PROJECT_ID}
                    username={props.user.username}
                    secret={props.user.secret}
                /> */}
                <ChatEngine
                    projectId={import.meta.env.VITE_CHAT_ENGINE_PROJECT_ID}
                    username={props.user.username}
                    secret={props.user.secret}
                    
                />
            </div>
        </div>
    );
}

export default ChatsPage
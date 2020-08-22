import React, {useEffect} from 'react';
import {useHistory} from 'react-router-dom';

export default function Landing(){
    let history = useHistory();
    useEffect(() => {
        setTimeout(()=>{
            history.push("/home")
        }, 5000)
    },)
    return(
        <contact>
            <h1>Welcome to my GIF-MACHINE!</h1>
            <iframe src="https://giphy.com/embed/OkJat1YNdoD3W" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
        </contact>
    )
}
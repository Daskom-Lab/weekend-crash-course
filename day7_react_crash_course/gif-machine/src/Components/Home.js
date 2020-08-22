import React, {useState} from 'react';

function Home(props){
    const [query, setQuery] = useState('');
    const [gif, setGif] = useState(null);
    const search = () => fetch(`https://api.giphy.com/v1/gifs/search?api_key=fQnWynoTtSQlNyYhw5bKsv7Q7iHGnNKZ&q=${query}&limit=10&offset=0&rating=g&lang=en`)
    .then((respon) => respon.json())
    .then((data) => setGif(data))
    console.log(gif)
    return(
        <home>
            <h1>
                What GIF are you looking for, {props.name}?
            </h1>
            <div className="input-bar">
                <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Cari GIF disini!"/>
                <button onClick={search}>Cari GIF!</button>
            </div>
            <div className="gif-bar">
                {gif && gif.data.map((item) => {
                    return(
                        <div style={{display: "flex", alignItems: "center", margin: "1rem"}}>
                            <video src={item.images.preview.mp4} autoPlay loop/>
                        </div>
                    )
                })}
            </div>
        </home>
    )
}

export default Home;
import React, { Fragment } from 'react'
import axios from 'axios'
// import Auth from '../../lib/Auth'
import { Link } from  'react-router-dom'
import AudioPlayer from 'react-h5-audio-player'

class SongsShow extends React.Component {
  constructor() {
    super()

    this.state = { song: null , comment: {} }

  }

  componentDidMount() {
    this.getData()
  }

  getData() {
    axios.get(`/api/songs/${this.props.match.params.id}`)
      .then(res => this.setState({ song: res.data, comment: {} }))
      .catch(err => console.log(err))
  }


  render() {
    if (!this.state.song) return null
    console.log(this.state)
    const { song } = this.state
    return (
      <section className="songsshowbg" style={{backgroundImage: `url(${song.image})`}}>

        <div className="container">
          <Fragment>
            <div className="columns is-block">
              <div className="column is-12">
                <h2 className="sstitle">{song.title}</h2>

                <AudioPlayer
                  autoPlay
                  src={song.music}
                />

              </div>
              <div className="columns is-block">
                <div className="column is-5 is-offset-7">
                  <h4 className="sslyric">{song.lyric}</h4>
                  <div className="sscategories">
                    {song.categories.map(category => {
                      return `${category.name} `
                    })}
                  </div>
                  <div className="ssinfo">
                    <h4>{song.album}</h4>
                    <h4><a href={song.review_link} target="_blank" rel="noopener noreferrer">Review</a></h4>
                    <h4><a href={song.external} target="_blank" rel="noopener noreferrer">Music Video</a></h4>
                  </div>
                  <Link to="/songs" className="float-right">Back to Songs</Link>
                </div>
              </div>
            </div>







          </Fragment>
        </div>

      </section>
    )
  }
}

export default SongsShow

// this.addLike = this.addLike.bind(this)

// <figure className="image">
//   <img className="songshowimage" src={song.image} alt={song.name} />
// </figure>

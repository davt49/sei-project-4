import React, { Fragment } from 'react'
import axios from 'axios'
// import Auth from '../../lib/Auth'
import { Link } from  'react-router-dom'

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
              </div>
              <div className="columns is-block">
                <div className="column is-5 is-offset-7">
                  <h4 className="sslyric">{song.lyric}</h4>
                  <div className="sscategories">
                    {song.categories.map(category => {
                      return `${category.name} `
                    })}
                  </div>
                  <p>{song.description}</p>
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

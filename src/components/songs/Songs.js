import React from 'react'
import axios from 'axios'
import Song from './Song'
import Auth from '../../lib/Auth'
// import { Link } from  'react-router-dom'

class SongIndex extends React.Component {
  constructor() {
    super()

    this.state = { data: null, filterCategory: '', checked: null }
    this.handleChange = this.handleChange.bind(this)
  }

  getData() {
    axios.get('/api/songs', {
      headers: { Authorization: `Bearer ${Auth.getToken()}` }
    })
      .then(res => this.setState({ data: res.data }))
      .catch(err => console.log(err))
  }

  componentDidMount() {
    this.getData()
  }

  handleChange(e, n) {
    const category = e.target.value
    this.setState({ filterCategory: category, checked: n })
  }

  filterSongs() {
    return  this.state.data.filter(song => {
      return this.state.filterCategory === '' ||
      song.categories.some(cat => cat.name === this.state.filterCategory)
    })
  }

  render() {
    return (
      <div className="songindex">
        <div className="hero">
          <div className="hero-body ">
            <div className="container has-text-centered">
              <h1 className="indextitle">Feeling Radiohead</h1>
            </div>
          </div>

        </div>
        {
          !this.state.data &&
          <img src='https://media.giphy.com/media/spcf2UJICfAs/giphy.gif' />
        }
        {
          this.state.data &&
          <div>
            <h1 className="songsifeel has-text-centered">Today I feel</h1>
            <div className="hero">
              <div className="hero-body">
                <div className="container">
                  <div className="songs-nav">


                    <div className="filter">
                      <input
                        type="radio"
                        id="tag-0"
                        className="filter-tag"
                        name="category"
                        value=""
                        onChange={(e) => {
                          this.handleChange(e, 0)
                        }
                        }
                        hidden/>
                      <input
                        type="radio"
                        id="tag-1"
                        className="filter-tag"
                        name="category"
                        value="Melancholy"
                        onChange={(e) => {
                          this.handleChange(e, 1)
                        }
                        }
                        hidden />
                      <input
                        type="radio"
                        id="tag-2"
                        className="filter-tag"
                        name="category"
                        value="Erratic"
                        onChange={(e) => {
                          this.handleChange(e, 2)
                        }
                        }
                        hidden />
                      <input
                        type="radio"
                        id="tag-3"
                        className="filter-tag"
                        name="category"
                        value="Smash"
                        onChange={(e) => {
                          this.handleChange(e, 3)
                        }
                        }
                        hidden />
                      <input
                        type="radio"
                        id="tag-4"
                        className="filter-tag"
                        name="category"
                        value="Radiant"
                        onChange={(e) => {
                          this.handleChange(e, 4)
                        }
                        }
                        hidden
                      />
                      <div className="filter-nav has-text-centered">
                        <label
                          className={`filtertag chip ${this.state.checked === 0 ? 'has-text-info' : ''}`}
                          htmlFor="tag-0">
                            Avant-Garde
                        </label>
                        <label
                          className={`filtertag chip ${this.state.checked === 1 ? 'has-text-info' : ''}`}
                          htmlFor="tag-1">
                            Melancholy
                        </label>
                        <label
                          className={`filtertag chip ${this.state.checked === 2 ? 'has-text-info' : ''}`}
                          htmlFor="tag-2">
                            Erratic
                        </label>
                        <label
                          className={`filtertag chip ${this.state.checked === 3 ? 'has-text-info' : ''}`}
                          htmlFor="tag-3">
                            Smash
                        </label>
                        <label
                          className={`filtertag chip ${this.state.checked === 4 ? 'has-text-info' : ''}`}
                          htmlFor="tag-4">
                            Radiant
                        </label>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="container">
              <div className='songsbunch columns is-multiline'>
                {this.filterSongs().map(song =>
                  <Song key={song.id} {...song} />
                )}
              </div>
            </div>
            <footer className="navbar is-fixed-bottom footersection">
              <section className="navbar-start ">
              </section>
              <section className="navbar">
              </section>
              <section className="navbar-end ">
                <p>Made by [</p>
                <a href="https://github.com/davt49"> David </a>
                <p>] @GA with React + Flask</p>
              </section>
            </footer>
          </div>

        }


      </div>
    )
  }
}

export default SongIndex

import React from 'react'
import { Link } from  'react-router-dom'

const About = () => (
  <section className="aboutpage">
    <div className="container">
      <div className="columns">
        <div className="column is-3"></div>
        <div className="column is-6 has-text-centered">
          <div className="abouttext has-text-centered">
            <h3>About </h3>
            <p>Radiohead had been the soundtrack to my growing up. </p>
            <p>I remember in the offtimes of high school, where I was arranging songs from all their different albums- by their mood, pace and intensity- into different playlists. I would spend hours and have a lot of fun just doing that.</p>
            <p>The style category is of course my personal opinion and I appreciate that different fans might have a different opinion.</p>
            <p>I had a lot of fun making this small site :)</p>
            <p>Hope you enjoy it!</p>
            <br/>
            <Link to="/songs" className="">Back to Songs</Link>
          </div>
        </div>
        <div className="column is-3"></div>
        <div className="columns">
        </div>
      </div>
    </div>
  </section>
)

export default About

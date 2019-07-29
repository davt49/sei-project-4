import React from 'react'
import { Link } from  'react-router-dom'

const Song = ({ image, title, id }) => {
  return (
    <div className="column is-3 songs-card">

      <div className="card songs-card">
        <Link to={`/songs/${id}`} >
          <div className="card-image">
            <img src={image} className="img-responsive"/>
          </div>
          <div className=" has-text-centered">
            <div className="card-title">{title}</div>
          </div>
        </Link>

      </div>

    </div>
  )
}

export default Song

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
          <div className="card-header">
            <div className="card-title h5">{title}</div>
          </div>
        </Link>

      </div>

    </div>
  )
}

export default Song
//
// <div className="card-body">
//   <div className="card-subtitle text-gray">
//     <div className="chip">
//       <Link to={`/users/${user._id}`} aria-label="Close" role="button">
//         <img src={user.image} className="avatar avatar-sm" />
//         {user.username}
//         <span> {user.userType === 'Local' ? ' 🇻🇳 ' : ' ✈️ '} </span>
//       </Link>
//     </div>
//   </div>
// </div>

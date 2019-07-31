import React from 'react'
import ReactDOM from 'react-dom'
import 'bulma'
import './styles/style.scss'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import 'react-h5-audio-player'
import Login from './components/auth/Login'
import Register from './components/auth/Register'
import Songs from './components/songs/Songs'
import SongsShow from './components/songs/SongsShow'
import About from './components/common/About'

const App = () => {
  return (
    <BrowserRouter>
      <main>
        <Switch>
          <Route path='/about' component={About}/>
          <Route path='/songs/:id' component={SongsShow}/>
          <Route path='/songs' component={Songs}/>
          <Route path='/register' component={Register}/>
          <Route exact path='/' component={Login} />
        </Switch>

      </main>
    </BrowserRouter>
  )
}
ReactDOM.render(
  <App />,
  document.getElementById('root')
)

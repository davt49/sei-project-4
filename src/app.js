import React from 'react'
import ReactDOM from 'react-dom'
import 'bulma'
import './styles/style.scss'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import 'react-h5-audio-player'
import Login from './components/auth/login'
import Register from './components/auth/register'
import Songs from './components/songs/songs'
import SongsShow from './components/songs/SongsShow'

const App = () => {
  return (
    <BrowserRouter>
      <main>
        <Switch>
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



// <Switch>
//   <Route path='/chats/:chatId' component={ChatShow}/>
//   <Route path='/chats' component={Chats}/>
//   <Route path='/gems/new' component={GemCreate}/>
//   <Route path='/gems/:gemId/edit' component={GemEdit}/>
//   <Route path='/gems/:gemId' component={GemsShow}/>
//   <Route path='/gems' component={Gems}/>
//   <Route path='/profile' component={Profile}/>
//   <Route path='/users/:userId' component={UserShow}/>
//   <Route path='/register' component={Register}/>
//   <Route exact path='/' component={Login} />
// </Switch>
// <Navbar />
// <Footer/>

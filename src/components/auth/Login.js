import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
import { Link } from  'react-router-dom'

class Login extends React.Component {
  constructor() {
    super()

    this.state = { data: {}, error: '' }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange({ target: { name, value } }) {
    const data = { ...this.state.data, [name]: value }
    this.setState({ data, error: '' })
  }

  handleSubmit(e) {
    e.preventDefault()

    axios.post('/api/login', this.state.data)
      .then(res => {
        Auth.setToken(res.data.token)
        this.props.history.push('/songs')
      })
      .catch(() => this.setState({ error: 'Invalid Crendentials' }))
  }

  render(){
    return(
      <section className="loginbackground">
        <div >

          <h1 className='logintitle has-text-centered'>Feeling Radiohead</h1>

          <div className="columns has-text-centered">
            <div className="column is-5"></div>
            <div className="column loginbox is-2">
              <form className="field" onSubmit={this.handleSubmit}>
                <h2 className="label is-medium">Login Here</h2>
                {this.state.error && <small className="help is-danger">{this.state.error}</small>}
                <div className="form-group">
                  <label className="form-label" htmlFor="name"></label>
                  <input
                    className={`form-input ${this.state.error ? 'is-error' : ''} `}
                    name="email"
                    placeholder="Email"
                    onChange={this.handleChange}
                  />
                </div>
                <div className="form-group">
                  <label className="form-label" htmlFor="email"></label>
                  <input
                    className={`form-input ${this.state.error ? 'is-error' : ''} `}
                    type="password"
                    name="password"
                    placeholder="Password"
                    onChange={this.handleChange}
                  />
                </div>

                <br/>

                <button className="button">Login</button>
                <p> Dont have an account? </p>
                <Link to="/register" className="c-hand">Register here</Link>
              </form>
            </div>
            <div className="column is-5"></div>
            <footer className="navbar is-fixed-bottom footersection">
              <section className="navbar-end ">
                <p>Made by [</p>
                <a href="https://github.com/davt49"> David </a>
                <p>] @GA with React + Flask</p>
              </section>
            </footer>
          </div>
        </div>
      </section>
    )
  }
}

export default Login

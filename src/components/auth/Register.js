import React from 'react'
import axios from 'axios'
import { Link } from  'react-router-dom'

class Register extends React.Component {
  constructor() {
    super()

    this.state = { data: {}, errors: {} }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {

  }

  handleChange({ target: { name, value } }) {
    const data = { ...this.state.data, [name]: value }
    const errors = { ...this.state.errors, [name]: '' }
    this.setState({ data, errors })
  }

  handleSubmit(e) {
    e.preventDefault()
    axios.post('/api/register', this.state.data)
      .then(() => this.props.history.push('/'))
      .catch(() => this.setState({ errors: 'Invalid Input or Already Registered' }))
  }

  render() {
    return (
      <section >
        <div className="registersection">
          <h1 className='registertitle has-text-centered'>Feeling Radiohead</h1>

          <div className="columns">
            <div className="column is-5"></div>
            <div className="column is-2 registerbox">
              <form onSubmit={this.handleSubmit}>
                <div className="form-group has-text-centered">
                  <h2 className="label is-medium">Sign Up</h2>
                  <input
                    className={`form-input ${this.state.errors ? 'is-danger' : ''} `}
                    name="username"
                    placeholder="Username"
                    onChange={this.handleChange}
                  />
                  {this.state.errors && <small className="help is-danger">{this.state.errors.username}</small>}

                  <input
                    className={`form-input ${this.state.errors ? 'is-danger' : ''} `}
                    name="email"
                    placeholder="Email"
                    onChange={this.handleChange}
                  />
                  {this.state.errors && <small className="help is-danger">{this.state.errors.email}</small>}

                  <input
                    className={`form-input ${this.state.errors ? 'is-danger' : ''} `}
                    name="password"
                    placeholder="Password"
                    type="password"
                    onChange={this.handleChange}
                  />
                  {this.state.errors && <small className="help is-danger">{this.state.errors.password}</small>}

                  <div className="form-group">
                    <input
                      className={`form-input ${this.state.errors ? 'is-danger' : ''} `}
                      name="password_confirmation"
                      placeholder="Password Confirmation"
                      type="password"
                      onChange={this.handleChange}
                    />
                  </div>
                  <br/>
                  {this.state.errors && <small className="help is-danger">{this.state.errors.password_confirmation}</small>}
                  <button type="submit" className="button">Submit</button>
                  <p>Already Registered?</p>
                  <Link to="/" className="has-text-centered">Back to Login</Link>
                </div>
              </form>

            </div>
            <div className="column is-5"></div>
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
        </div>

      </section>
    )
  }
}

export default Register

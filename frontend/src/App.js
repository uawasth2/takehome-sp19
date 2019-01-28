import React, { Component } from 'react'
import Instructions from './Instructions'
import Show from './Show'

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      shows: [
        {id: 1, name: "Game of Thrones", episodes_seen: 0},
        {id: 2, name: "Naruto", episodes_seen: 220},
        {id: 3, name: "Black Mirror", episodes_seen: 3},
      ],
      nextID: 4,
      input: ''
    }

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({input: event.target.value});
  }
  handleSubmit(event) {
    this.setState({
      shows: this.state.shows.concat({id: this.state.nextID, name: this.state.input, episodes_seen:0}),
      input: '',
      nextID: this.state.nextID + 1
    });
    event.preventDefault();
  }

  render() {
    return (
      <div className="App">
        <Instructions complete={true}/>
        {this.state.shows.map(x => (
          <Show id={x.id} name={x.name} episodes_seen={x.episodes_seen} />
        ))}

          <div>
            <form onSubmit={this.handleSubmit}>
              <input type='text' value={this.state.input} placeholder='Add New Show&apos;s Name' onChange={this.handleChange} />
              <input type="submit" value="Submit" />
            </form>
          </div>
      </div>
    )
  }
}

export default App

import React, { Component } from 'react'
import Counter from './Counter'

class App extends Component {
  // YOUR CODE GOES BELOW
  constructor(props) {
    super(props)
  }
  render() {
    return (
      <div>
        <div>
          ID: {this.props.id}
        </div>
        <div>
          Name: {this.props.name}
        </div>
        <div>
          Episodes Seen: <Counter count={this.props.episodes_seen}/>
          <br/>
        </div>
      </div>
    )
  }
}

export default App

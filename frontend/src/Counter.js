import React, { Component } from 'react'

class Counter extends Component {
  // YOUR CODE GOES BELOW
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    }
  }
  render() {
    return (
      <div> 
        <button onClick={this.incrementCount}>Increment</button>
        {this.state.count}
        <button onClick={this.decrementCount}>Decrement</button>
      </div> 
    )
  }
  incrementCount = () => {
    var val = this.state.count + 1;
    this.setState({count: val});
  }
  decrementCount = () => {
    var val = this.state.count - 1;
    this.setState({count: val});
  }
}

export default Counter

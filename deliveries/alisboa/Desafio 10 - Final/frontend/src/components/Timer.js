import React, { Component } from 'react'

const inicialState = {
    minutes: 1,
    seconds: 40,
}

export default class Timer extends Component {
    state = inicialState

    componentDidMount() {
        this.myInterval = setInterval(() => {
            if(this.props.reset[this.props.reset.length - 1]){
                this.clear();
                return;
            }
            const { seconds, minutes } = this.state

            if (seconds > 0) {
                this.setState(({ seconds }) => ({
                    seconds: seconds - 1
                }))
            }
            if (seconds === 0) {
                if (minutes === 0) {
                    clearInterval(this.myInterval)
                } else {
                    this.setState(({ minutes }) => ({
                        minutes: minutes - 1,
                        seconds: 59
                    }))
                }
            } 
        }, 1000)
    }

    componentWillUnmount() {
        clearInterval(this.myInterval)
    }

    clear(){
        this.setState(inicialState);
    }

    render() {
        const { minutes, seconds } = this.state
        return (
            <div>
                { minutes === 0 && seconds === 0
                    ? <h2>Time is up!</h2>
                    : <h3>{minutes}:{seconds < 10 ? `0${seconds}` : seconds}</h3>
                }
            </div>
        )
    }
}
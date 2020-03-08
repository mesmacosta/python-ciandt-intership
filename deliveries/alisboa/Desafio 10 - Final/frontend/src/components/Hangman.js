import React, { Component } from "react";

import step0 from "./images/0.jpg";
import step1 from "./images/1.jpg";
import step2 from "./images/2.jpg";
import step3 from "./images/3.jpg";
import step4 from "./images/4.jpg";
import step5 from "./images/5.jpg";
import step6 from "./images/6.jpg";

import Timer from "./Timer"

class Hangman extends Component {
	static defaultProps = {
		maxWrong: 6,
		images: [step0, step1, step2, step3, step4, step5, step6]
	};

	constructor(props) {
		super(props);
		this.state = { mistake: 0, guessed: new Set(), answer: '' };
		this.handleGuess = this.handleGuess.bind(this);
		this.state.guessed.add(" ");
		this.resetTimer = false
	}

	componentDidMount() {
		fetch('/api/v1/new/')
			.then(res => res.json())
			.then((result) => {
				this.setState({
					isLoaded: true,
					gameId: result.game_id
				});
				//console.log('New '+ this.state.gameId)
			},
			(error) => {
				console.error('error to fetch start game')
				console.log(JSON.stringify(error))	
			}).then(() => {
				fetch('/api/v1/start/'+ this.state.gameId, { method:'POST'})
					.then(res => res.json())
					.then((result) => {
						this.setState(st => ({
							game: result.data,
						}));
						this.resetTime()
					}, 
				(error) => {
					console.error('error to fetch start game!')
					console.log(JSON.stringify(error))
				})
			});
	}

	guessedWord() {
		return this.state.game ? this.state.game.find.toUpperCase() : [];
	}

	handleGuess(evt) {
		let letter = evt.target.value.toUpperCase();
		console.log('val: '+ evt.target.value)
		fetch('/api/v1/gess/' + this.state.gameId + '?gess=' + letter, { method: 'POST'})
		.then(res => res.json())
		.then((result) => {
			this.setState(st => ({
				isLoaded: true,
				gameId: result.game_id,
				game: result.data,
				guessed: st.guessed.add(letter),
				mistake: result.data.tries,
				//Answer só chega se o jogo for perdido ou ganhado
				answer: result.data.word ? result.data.word.toUpperCase() : ''
			}));
		},
		(error) => {
			console.error('error to fetch start game')
		})
	}

	generateButtons() {
		return "abcdefghijklmnopqrstuvwxyz ".split("").map(letter => (
			<button
				key={letter}
				value={letter}
				onClick={this.handleGuess}
				disabled={this.state.guessed.has(letter.toUpperCase())}
			>
				{letter}
			</button>
		));
	}


	resetButton = () => {
		fetch(`/api/v1/reset/${this.state.gameId}`, { method: 'POST'})
		.then(res => res.json())
		.then(result => {
			if(result.success){
				let guessed = new Set();
				guessed.add(" ")
				this.componentDidMount()
				this.setState({
					mistake: 0,
					guessed: guessed
				});
			}
			else {
				console.error('error to fetch reset game');
			}
		},
		error => {
			console.error('error to fetch reset game');
		});
	};

	resetTime = () => {
		this.resetTimer = !this.resetTimer;
	}

	render() {

		let gameOver = false;
		let altText = '0 wrong guesses';
		let isWinner = false;

		if (this.state.game !== undefined) {
			gameOver = this.state.game.result === 'lose';
			altText = `${this.state.game.tries} wrong guesses`;
			isWinner = this.state.game.result === 'win';
		}
		
		
		let gameStat = this.generateButtons();
		if (isWinner) {
			gameStat = "YOU WON";
		}
		if (gameOver) {
			gameStat = "YOU LOST";
		}
		
		return (
			<div className='Hangman'>
				<nav className='navbar navbar-expand-lg'>
					<a className='navbar-brand text-light' href='/'>
						Hangman. <small>Do (or) Die</small>
					</a>
					<span className='d-xl-none d-lg-none text-primary'>
						Guessed wrong: {this.state.mistake}
					</span>
					<button
						className='navbar-toggler sr-only'
						type='button'
						data-toggle='collapse'
						data-target='#navbarText'
						aria-controls='navbarText'
						aria-expanded='false'
						aria-label='Toggle navigation'
					>
						<span className='navbar-toggler-icon'></span>
					</button>
					<div className='collapse navbar-collapse' id='navbarText'>
						<ul className='navbar-nav mr-auto'>
							<li className='nav-item '></li>
							<li className='nav-item'></li>
							<li className='nav-item'></li>
						</ul>
						<span className='navbar-text text-primary'>Guessed wrong: {this.state.mistake}</span>
					</div>
				</nav>
				<p className='text-center'>
					<img src={this.props.images[this.state.mistake]} alt={altText} />
				</p>
				{!(gameOver || isWinner) ? 
					<div className = "text-center text-light">
						<Timer reset = {this.resetTimer} />
					</div>
					:
					""
				}
				<p className='text-center text-light'>Guess Ciandt University Content ?</p>
				<p className='Hangman-word text-center'>
					{!gameOver ? this.guessedWord() : this.state.answer}{" "}
				</p>

				<p className='text-center text-warning mt-4'>{gameStat}</p>
				<div>
					<p className='text-center'>
						<button className='Hangman-reset' onClick={this.resetButton}>
							Reset
						</button>
					</p>
				</div>
			</div>
		);
	}
}

export default Hangman;

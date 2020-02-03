import '../config';
import { withRouter, Link } from 'react-router-dom';
import $ from 'jquery';
import React, { Component } from 'react';
import './detail.css';
import { Button, Card  } from 'antd';


class List extends Component{
	state = {
	}
	getTeamInfo = () => {
		let url = global.constants.server + 'api/team/' + this.props.match.params.teamID + '/';
		$.get({
			url: url,
			async: true,
			success: function (result) {
				this.setState({team: result})
			}.bind(this)
		})
	}
	componentWillMount(){
		this.getTeamInfo();
	}
	render(){
		if (this.state.team == null){
			return (
				<div  id = "root">
					Loading...
				</div>
			)
		}
		return (
			<div  id = "root">
				<div  id = "name">
					{this.state.team.name}
				</div>
				<div  id = "introduction">
					{this.state.team.introduction}
				</div>
			</div>
		)
	}
}

export default List;
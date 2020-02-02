import './config';
import { withRouter, Link } from 'react-router-dom';
import $ from 'jquery';
import React, { Component } from 'react';
import './information.css';
import { Form, Icon, Input, Button, Checkbox, Alert, Descriptions  } from 'antd';


class Informathion extends Component{
	render(){
		const { user } = this.props
		if (user == null) {
			this.props.history.push('/')
			return (
				<div  id = 'root' >
					<div  id = 'username' > 
						Please log in.
					</div>
				</div>
			)
		}
		let userTeam = { tips : 'Team', content : 'None'}
		if (user.team){
			userTeam.content = <Link to='user/{user.team.id}'>{user.team.name}</Link>
			if (!user.isMember){
				userTeam.tips = 'Team (applying)'
			}
		}
		return (
			<div  id = "root">
				<Descriptions  id = "information" title={user.username} bordered>
					<Descriptions.Item label={userTeam.tips}> {userTeam.content} </Descriptions.Item>
					<Descriptions.Item label="Name"> {user.name} </Descriptions.Item>
					<Descriptions.Item label="Class"> {user.class} </Descriptions.Item>
					<Descriptions.Item label="Department"> {user.department} </Descriptions.Item>
					<Descriptions.Item label="ID"> {user.id} </Descriptions.Item>
				</Descriptions>
			</div>
		)
	}
}

export default Informathion;
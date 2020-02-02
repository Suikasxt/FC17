import './config';
import $ from 'jquery';
import { withRouter, Link } from 'react-router-dom';
import React, { Component } from 'react';
import './login.css';
import { Form, Icon, Input, Button, Checkbox, Alert } from 'antd';


class Login extends Component{
	state = {
		message : null,
	}
	componentWillReceiveProps(nextProps){
		if (nextProps.unLogin === false){
			this.props.history.push('/');
		}
	}
	componentWillMount(){
		if (this.props.unLogin === false){
			this.props.history.push('/');
		}
	}
	handleSubmit = (e) => {
		e.preventDefault();
		this.props.form.validateFields((err, values) => {
			if (!err) {
				let url = global.constants.server + 'api/user/login/';
				this.serverRequest = $.post({
					url: url,
					data: values,
					crossDomain: true,
					xhrFields: {
						withCredentials: true
					},
					success: function (result) {
						if (result.result === 0){
							this.setState({'message' : result.message})
						}else{
							this.props.tryLogin(result)
						}
					}.bind(this)
				});
			}
		});
	};

	render(){
		const { getFieldDecorator } = this.props.form;
		let alert = null
		if (this.state.message != null){
			alert = <Alert message={this.state.message} type="error" />
		}
		return (
			<div style={{ padding: 24, background: '#fff', minHeight: 500, alignItems : 'center', justifyContent: 'center', display : 'flex', flexDirection: 'column' }}>
				{alert}
				<Form onSubmit={this.handleSubmit} className="login-form">
					<Form.Item>
						{getFieldDecorator('username', {
							rules: [{ required: true, message: 'Please input your username!' }],
						})(
							<Input
								prefix={<Icon type="user" style={{ color: 'rgba(0,0,0,.25)' }} />}
								placeholder="Username"
							/>,
						)}
					</Form.Item>
					<Form.Item>
						{getFieldDecorator('ID', {
							rules: [{ required: true, message: 'Please input your ID!' }],
						})(
							<Input
								prefix={<Icon type="idcard" style={{ color: 'rgba(0,0,0,.25)' }} />}
								placeholder="ID"
							/>,
						)}
					</Form.Item>
					<Form.Item>
						{getFieldDecorator('password', {
							rules: [{ required: true, message: 'Please input your Password!' }],
						})(
							<Input
								prefix={<Icon type="lock" style={{ color: 'rgba(0,0,0,.25)' }} />}
								type="password"
								placeholder="Password"
							/>,
						)}
					</Form.Item>
					<Form.Item>
						{getFieldDecorator('remember', {
							valuePropName: 'checked',
							initialValue: true,
						})(<Checkbox>Remember me</Checkbox>)}
						<Button type="primary" htmlType="submit" className="login-form-button">
							Log in
						</Button>
					</Form.Item>
				</Form>
			</div>
		)
	}
}

export default Form.create({ name: 'normal_login' })(Login);
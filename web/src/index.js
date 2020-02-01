import './config';
import React, { Component } from 'react';
import { HashRouter as Router, Link, Route } from 'react-router-dom';
import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import './index.css';
import $ from 'jquery';
import { Layout, Menu, Breadcrumb, Icon } from 'antd';
import Home from './home.js'
import Login from './login.js'

const { Header, Content, Footer, Sider } = Layout;
const { SubMenu } = Menu;



class SiderDemo extends React.Component {
	constructor(props) {
		super(props);
		this.tryLogin();
	}
	state = {
		collapsed: false,
		user: null,
	};
	
	onCollapse = collapsed => {
		console.log(collapsed);
		this.setState({ collapsed });
	};
	
	tryLogin = () => {
		if (this.state.user != null) return;
		let url = global.constants.server + 'api/user/';
		this.loginRequest = $.get({
			url: url,
			crossDomain: true,
			xhrFields: {
                withCredentials: true
            },
			success: function (result) {
				if (result.id){
					this.setState({'user' : result});
					window.location.href = "#/";
				}
			}.bind(this)
		});
	};
	logout = (e) => {
		let url = global.constants.server + 'api/user/logout/';
		this.logoutRequest = $.get({
			url: url,
			crossDomain: true,
			xhrFields: {
                withCredentials: true
            },
			success: function (result) {
				this.setState({'user' : null});
			}.bind(this)
		});
	}

	render() {
		let user = null
		if (this.state.user != null){
			user = (
			<SubMenu
				key="user"
				title={
					<span>
						<Icon type="user" />
						<span>User</span>
					</span>
				}
			>
				<Menu.Item key="personal" >
					<Link to="personal">
						<span>Personal Data</span>
					</Link>
				</Menu.Item>
				<Menu.Item key="logout" onClick={this.logout}>Logout</Menu.Item>
			</SubMenu>)
		}else{
			user = (
			<Menu.Item key="login">
				<Link to="/login">
					<Icon type="user" />
					<span>Login</span>
				</Link>
			</Menu.Item>)
		}
		
		
		return (
			<Router>
				<Layout style={{ minHeight: '100vh' }}>
					<Sider collapsible collapsed={this.state.collapsed} onCollapse={this.onCollapse}>
						<div className="logo" />
						<Menu theme="dark" defaultSelectedKeys={['1']} mode="inline">
							<Menu.Item key="home">
								<Link to="/">
									<Icon type="pie-chart" />
									<span>Home</span>
								</Link>
							</Menu.Item>
							{user}
						</Menu>
					</Sider>
					<Layout>
						<Header style={{ background: '#fff', padding: 0}} >
							<h1 style={{ textAlign : 'center' }}>FC17</h1>
						</Header>
						<Content style={{ margin: '10px 16px' }}>
							<Route path="/" exact component={Home}/>
							<Route path="/login" render={props => <Login tryLogin={this.tryLogin.bind(this)} {...props} />}/>
						</Content>
						<Footer style={{ textAlign: 'center' }}>FC17</Footer>
					</Layout>
				</Layout>
			</Router>
		);
	}
}

ReactDOM.render(<SiderDemo />, document.getElementById('container'));
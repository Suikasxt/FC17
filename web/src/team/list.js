import '../config';
import { withRouter, Link } from 'react-router-dom';
import $ from 'jquery';
import React, { Component } from 'react';
import { Form, Icon, Input, Button, Checkbox, Alert, Descriptions, Card  } from 'antd';


class List extends Component{
	state = {
	}
	getTeamList = () => {
		let url = global.constants.server + 'api/team/list/';
		this.teamListRequest = $.get({
			url: url,
			success: function (result) {
				this.setState({list : result});
			}.bind(this)
		})
	}
	componentWillMount(){
		this.getTeamList();
	}
	render(){
		if (this.state.list == null){
			return (
				<div  id = "root">
					Loading...
				</div>
			)
		}
		return (
			<div  id = "root">
				{
					this.state.list.map((item, index) => {
						return (
							<Card title={item.name} key={item.id} extra={
										<Link to={"/team/detail/" + item.id}>
											<Button type="primary">Detail</Button>
										</Link>
									} style={{ width: 300 }}>
								<p>{item.introduction}</p>
							</Card>
						)
					})
				}
			</div>
		)
	}
}
export default List;
